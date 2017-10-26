import { ORM } from 'redux-orm';

import Election from './election';
import Office from './office';
import Division from './division';
import Candidate from './candidate';
import Party from './party';
import Result from './result';
import APMeta from './apMeta';


const orm = new ORM();

orm.register(
  Election,
  Office,
  Division,
  Candidate,
  Party,
  APMeta,
  Result,
);

export default orm;
