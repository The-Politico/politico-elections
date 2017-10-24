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
        addCandidates(data.elections, dispatch)
      ])
    )
    .catch((error) => {
      console.log('API ERROR', error);
    });

function addDivisions(division, dispatch) {
  const parent = Object.assign({}, parent, division);
  delete parent.children;
  dispatch(ormActions.createDivision(parent));
  division.children.map(d => {
    d.parent = parent.id;
    dispatch(ormActions.createDivision(d));
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
      apElectionId: d.ap_election_id,
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
    dispatch(ormActions.createParty(d));
  });
}

function addCandidates(elections, dispatch) {
  elections.map(d => {
    d.candidates.map(e => {
      dispatch(ormActions.createCandidate(e));
    });
  })  
}

function addElections(elections) {
  elections.map(d => {
    // get your fks
  });
}