import assign from 'lodash/assign';
import * as ormActions from './orm';
import * as fetchActions from './fetch';
import {createPageTypeContentBlock, createPageContentBlock} from './content';

const headers = {
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  },
};

const GET = assign({}, headers, { method: 'GET' });

function addDivisions(division, dispatch) {
  const parent = assign({}, division);
  const parentObj = {
    id: parent.postal_code ? parent.postal_code : parent.code,
    code: parent.code,
    level: parent.level,
    label: parent.label,
    shortLabel: parent.short_label,
    codeComponents: parent.code_components,
    parent: null,
    postalCode: parent.postal_code,
    topojson: null,
  };

  dispatch(ormActions.createDivision(parentObj));
  division.children.forEach((d) => {
    const childObj = {
      id: d.code,
      code: d.code,
      level: d.level,
      label: d.label,
      shortLabel: d.short_label,
      codeComponents: d.code_components,
      parent: parentObj.id,
      postalCode: d.postal_code,
      topojson: null,
    };

    return dispatch(ormActions.createDivision(childObj));
  });
}

function addOffices(elections, dispatch) {
  elections.forEach((d) => {
    d.office.id = d.office.uid;
    delete d.office.uid;
    dispatch(ormActions.createOffice(d.office));
  });
}

function addApMetas(elections, dispatch) {
  elections.forEach((d) => {
    const meta = {
      id: d.ap_election_id,
      called: d.called,
      overrideApCall: d.override_ap_call,
      overrideApVotes: d.override_ap_votes,
      tabulated: d.tabulated,
    };

    dispatch(ormActions.createApMeta(meta));
  });
}

function addParties(parties, dispatch) {
  parties.forEach((d) => {
    const partyObj = {
      id: d.ap_code,
      label: d.label,
      shortLabel: d.short_label,
      slug: d.slug,
    };

    dispatch(ormActions.createParty(partyObj));
  });
}

function addCandidates(elections, dispatch) {
  elections.forEach((d) => {
    d.candidates.forEach((e) => {
      const candidateObj = {
        id: e.ap_candidate_id,
        firstName: e.first_name,
        lastName: e.last_name,
        suffix: e.suffix,
        party: e.party,
        aggregable: e.aggregable,
        overrideWinner: e.override_winner,
        incumbent: e.incumbent,
        uncontested: e.uncontested,
        images: e.images,
      };

      dispatch(ormActions.createCandidate(candidateObj));
    });
  });
}

function addElections(elections, dispatch) {
  elections.forEach((d) => {
    const candidates = [];
    d.candidates.forEach((candidate) => {
      candidates.push(candidate.ap_candidate_id);
    });

    const electionObj = {
      id: d.uid,
      date: d.date,
      office: d.office.id,
      party: d.primary_party,
      candidates,
      division: d.division.code,
      apMeta: d.ap_election_id,
    };

    dispatch(ormActions.createElection(electionObj));
  });
}

function createResultObj(d) {
  const divisionID = d.fipscode ? d.fipscode : d.statepostal;
  const candidateID = d.polid ? `polid-${d.polid}` : `polnum-${d.polnum}`;
  const resultObj = {
    id: `${d.raceid}-${divisionID}-${candidateID}`,
    voteCount: d.votecount,
    votePct: d.votepct,
    precinctsReporting: d.precinctsreporting,
    precinctsTotal: d.precinctstotal,
    precinctsReportingPct: d.precinctsreportingpct,
    winner: d.winner,
    division: divisionID,
    candidate: candidateID,
  };

  return resultObj;
}

function addOverrideResults(elections, dispatch) {
  elections.forEach((d) => {
    if (!d.override_votes) {
      return;
    }
    d.override_votes.forEach((e) => {
      const resultObj = createResultObj(e);
      dispatch(ormActions.createOverrideResult(resultObj));
    });
  });
}

function addResults(results, dispatch) {
  results.forEach((d) => {
    const resultObj = createResultObj(d);
    dispatch(ormActions.createResult(resultObj));
  });
}

const addPageContent = (content, dispatch) =>
  dispatch(createPageContentBlock(content));
const addPageTypeContent = (content, dispatch) =>
  dispatch(createPageTypeContentBlock(content));

let compareContext = null;

export const fetchContext = modifiedTime =>
  dispatch => fetch(
    window.appConfig.api.context,
    assign({}, GET, { 'If-Modified-Since': modifiedTime }),
  )
    .then(response => response.json())
    // Checks if we can skip an upsert.
    .then((data) => {
      const context = JSON.stringify(data);
      // If context is same, bug out.
      if (context === compareContext) return null;
      // If not, reset Modified Time and return new data.
      compareContext = context;
      dispatch(fetchActions.setContextModifiedTime(new Date().toUTCString()));
      return data;
    })
    .then((data) => {
      if (!data) return null;
      return Promise.all([
        addDivisions(data.division, dispatch),
        addOffices(data.elections, dispatch),
        addApMetas(data.elections, dispatch),
        addParties(data.parties, dispatch),
        addCandidates(data.elections, dispatch),
        addElections(data.elections, dispatch),
        addOverrideResults(data.elections, dispatch),
        addPageContent(data.content.page, dispatch),
        addPageTypeContent(data.content.page_type, dispatch),
      ]);
    })
    .catch((error) => {
      console.log('API ERROR', error);
    });

let compareResults = null;

export const fetchResults = modifiedTime =>
  dispatch => fetch(
    window.appConfig.api.results,
    assign({}, GET, { 'If-Modified-Since': modifiedTime }),
  )
    .then(response => response.json())
    // Checks if we can skip an upsert.
    .then((data) => {
      const results = JSON.stringify(data);
      // If results are same, bug out.
      if (results === compareResults) return null;
      // If not, reset Modified Time and return new data.
      compareResults = results;
      dispatch(fetchActions.setResultsModifiedTime(new Date().toUTCString()));
      dispatch(fetchActions.notifyNewResults());
      return data;
    })
    .then((data) => {
      if (!data) return null;
      return addResults(data, dispatch);
    })
    .catch((error) => {
      console.log('API ERROR', error);
    });

function updateGeo(geoData, dispatch) {
  const fips = window.appConfig.stateFips;
  dispatch(ormActions.updateGeo(fips, geoData));
}

export const fetchGeo = () =>
  dispatch => fetch(window.appConfig.api.geo, GET)
    .then(response => response.json())
    .then(data => Promise.all([
      updateGeo(data, dispatch),
    ])).catch((error) => {
      console.log('API ERROR', error);
    });

export const fetchInitialData = () =>
  dispatch => Promise.all([
    dispatch(fetchContext()),
    dispatch(fetchResults()),
  ])
    .then(() => dispatch(fetchGeo()));
