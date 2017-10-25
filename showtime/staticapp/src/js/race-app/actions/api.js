import * as ormActions from './orm';

const headers = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const GET = Object.assign({}, headers, { method: 'GET' });

export const fetchContext = () =>
  dispatch => fetch('/static/showtime/context.json', GET)
    .then(
      response => response.json())
    .then(
      data => 
       Promise.all([
        addDivisions(data.division, dispatch),
        addOffices(data.elections, dispatch),
        addApMetas(data.elections, dispatch),
        addParties(data.parties, dispatch),
        addCandidates(data.elections, dispatch),
        addElections(data.elections, dispatch),
      ])
    )
    .catch((error) => {
      console.log('API ERROR', error);
    });

function addDivisions(division, dispatch) {
  const parent = Object.assign({}, parent, division);
  const parent_obj = {
    id: parent.code,
    level: parent.level,
    label: parent.label,
    shortLabel: parent.short_label,
    codeComponents: parent.code_components,
    parent: null,
  }

  dispatch(ormActions.createDivision(parent_obj));
  division.children.map(d => {
    const child_obj = {
      id: d.code,
      level: d.level,
      label: d.label,
      shortLabel: d.short_label,
      codeComponents: d.code_components,
      parent: parent_obj.id,
    }

    dispatch(ormActions.createDivision(child_obj));
  });
}

function addOffices(elections, dispatch) {
  elections.map(d => {
    dispatch(ormActions.createOffice(d.office));
  });
}

function addApMetas(elections, dispatch) {
  elections.map(d => {
    const meta = {
      id: d.ap_election_id,
      called: d.called,
      overrideApCall: d.override_ap_call,
      overrideApVotes: d.override_ap_votes,
      tabulated: d.tabulated,
    }

    dispatch(ormActions.createApMeta(meta));
  })
}

function addParties(parties, dispatch) {
  parties.map(d => {
    const party_obj = {
      id: d.ap_code,
      label: d.label,
      shortLabel: d.short_label,
      slug: d.slug,
    }

    dispatch(ormActions.createParty(party_obj));
  });
}

function addCandidates(elections, dispatch) {
  elections.map(d => {
    d.candidates.map(e => {
      const candidate_obj = {
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
      }

      dispatch(ormActions.createCandidate(candidate_obj));
    });
  })  
}

function addElections(elections, dispatch) {
  elections.map(d => {
    const candidates = [];
    d.candidates.forEach((candidate) => {
      candidates.push(candidate.ap_candidate_id);
    });

    const election_obj = {
      id: d.id,
      date: d.date,
      office: d.office.id,
      party: d.primary_party,
      candidates: candidates,
      division: d.division.code,
      apMeta: d.ap_election_id
    }

    setTimeout(() => {
      dispatch(ormActions.createElection(election_obj)) 
    }, 1000);
  });
}