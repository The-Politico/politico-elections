import _ from 'lodash';
import * as ormActions from './orm';

const headers = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const GET = _.assign({}, headers, { method: 'GET' });

function addDivisions(division, dispatch) {
  const parent = _.assign({}, division);
  const parentObj = {
    id: parent.postal_code ? parent.postal_code : parent.code,
    code: parent.code,
    level: parent.level,
    label: parent.label,
    shortLabel: parent.short_label,
    codeComponents: parent.code_components,
    parent: null,
    postalCode: parent.postal_code,
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
    };

    dispatch(ormActions.createDivision(childObj));
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
        winner: e.winner,
        incumbent: e.incumbent,
        uncontested: e.uncontested,
        image: e.image,
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

export const fetchContext = () =>
  dispatch => fetch(window.appConfig.api.context, GET)
    .then(response => response.json())
    .then(data =>
      Promise.all([
        addDivisions(data.division, dispatch),
        addOffices(data.elections, dispatch),
        addApMetas(data.elections, dispatch),
        addParties(data.parties, dispatch),
        addCandidates(data.elections, dispatch),
        addElections(data.elections, dispatch),
      ])).catch((error) => {
      console.log('API ERROR', error);
    });

function addResults(results, dispatch) {
  results.forEach((d) => {
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

    dispatch(ormActions.createResult(resultObj));
  });
}


export const fetchResults = () =>
  dispatch => fetch(window.appConfig.api.results, GET)
    .then(response => response.json())
    .then(data =>
      Promise.all([
        addResults(data, dispatch),
      ])).catch((error) => {
      console.log('API ERROR', error);
    });
