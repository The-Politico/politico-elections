--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.4
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO jmcclure;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO jmcclure;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO jmcclure;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO jmcclure;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO jmcclure;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO jmcclure;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO jmcclure;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO jmcclure;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO jmcclure;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO jmcclure;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO jmcclure;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO jmcclure;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: demographic_censusestimate; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE demographic_censusestimate (
    id integer NOT NULL,
    estimate double precision NOT NULL,
    division_id character varying(500) NOT NULL,
    variable_id integer NOT NULL
);


ALTER TABLE demographic_censusestimate OWNER TO jmcclure;

--
-- Name: demographic_censusestimate_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE demographic_censusestimate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE demographic_censusestimate_id_seq OWNER TO jmcclure;

--
-- Name: demographic_censusestimate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE demographic_censusestimate_id_seq OWNED BY demographic_censusestimate.id;


--
-- Name: demographic_censuslabel; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE demographic_censuslabel (
    id integer NOT NULL,
    label character varying(100) NOT NULL,
    aggregation character varying(1) NOT NULL,
    table_id integer NOT NULL
);


ALTER TABLE demographic_censuslabel OWNER TO jmcclure;

--
-- Name: demographic_censuslabel_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE demographic_censuslabel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE demographic_censuslabel_id_seq OWNER TO jmcclure;

--
-- Name: demographic_censuslabel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE demographic_censuslabel_id_seq OWNED BY demographic_censuslabel.id;


--
-- Name: demographic_censustable; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE demographic_censustable (
    id integer NOT NULL,
    series character varying(4) NOT NULL,
    year character varying(4) NOT NULL,
    code character varying(10) NOT NULL,
    title character varying(100)
);


ALTER TABLE demographic_censustable OWNER TO jmcclure;

--
-- Name: demographic_censustable_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE demographic_censustable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE demographic_censustable_id_seq OWNER TO jmcclure;

--
-- Name: demographic_censustable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE demographic_censustable_id_seq OWNED BY demographic_censustable.id;


--
-- Name: demographic_censusvariable; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE demographic_censusvariable (
    id integer NOT NULL,
    code character varying(4) NOT NULL,
    label_id integer,
    table_id integer NOT NULL
);


ALTER TABLE demographic_censusvariable OWNER TO jmcclure;

--
-- Name: demographic_censusvariable_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE demographic_censusvariable_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE demographic_censusvariable_id_seq OWNER TO jmcclure;

--
-- Name: demographic_censusvariable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE demographic_censusvariable_id_seq OWNED BY demographic_censusvariable.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO jmcclure;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO jmcclure;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO jmcclure;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO jmcclure;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO jmcclure;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO jmcclure;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO jmcclure;

--
-- Name: election_ballotanswer; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_ballotanswer (
    id uuid NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    answer text NOT NULL,
    winner boolean NOT NULL,
    ballot_measure_id character varying(500) NOT NULL
);


ALTER TABLE election_ballotanswer OWNER TO jmcclure;

--
-- Name: election_ballotmeasure; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_ballotmeasure (
    uid character varying(500) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    question text NOT NULL,
    number character varying(3) NOT NULL,
    division_id character varying(500) NOT NULL,
    election_day_id character varying(500) NOT NULL
);


ALTER TABLE election_ballotmeasure OWNER TO jmcclure;

--
-- Name: election_candidate; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_candidate (
    uid character varying(500) NOT NULL,
    ap_candidate_id character varying(255) NOT NULL,
    aggregable boolean NOT NULL,
    winner boolean NOT NULL,
    incumbent boolean NOT NULL,
    uncontested boolean NOT NULL,
    gender character varying(50),
    image character varying(200),
    party_id character varying(500) NOT NULL,
    person_id character varying(500) NOT NULL,
    race_id character varying(500) NOT NULL,
    top_of_ticket_id character varying(500)
);


ALTER TABLE election_candidate OWNER TO jmcclure;

--
-- Name: election_candidate_elections; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_candidate_elections (
    id integer NOT NULL,
    candidate_id character varying(500) NOT NULL,
    election_id character varying(500) NOT NULL
);


ALTER TABLE election_candidate_elections OWNER TO jmcclure;

--
-- Name: election_candidate_elections_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE election_candidate_elections_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE election_candidate_elections_id_seq OWNER TO jmcclure;

--
-- Name: election_candidate_elections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE election_candidate_elections_id_seq OWNED BY election_candidate_elections.id;


--
-- Name: election_election; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_election (
    uid character varying(500) NOT NULL,
    division_id character varying(500) NOT NULL,
    election_day_id character varying(500) NOT NULL,
    election_type_id character varying(500) NOT NULL,
    party_id character varying(500),
    race_id character varying(500) NOT NULL
);


ALTER TABLE election_election OWNER TO jmcclure;

--
-- Name: election_electioncycle; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_electioncycle (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE election_electioncycle OWNER TO jmcclure;

--
-- Name: election_electionday; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_electionday (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    date date NOT NULL,
    cycle_id character varying(500) NOT NULL
);


ALTER TABLE election_electionday OWNER TO jmcclure;

--
-- Name: election_electiontype; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_electiontype (
    uid character varying(500) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    ap_code character varying(1) NOT NULL
);


ALTER TABLE election_electiontype OWNER TO jmcclure;

--
-- Name: election_party; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_party (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    ap_code character varying(3) NOT NULL,
    aggregate_candidates boolean NOT NULL
);


ALTER TABLE election_party OWNER TO jmcclure;

--
-- Name: election_race; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE election_race (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    cycle_id character varying(500) NOT NULL,
    office_id character varying(500) NOT NULL
);


ALTER TABLE election_race OWNER TO jmcclure;

--
-- Name: entity_body; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE entity_body (
    uid character varying(500) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    slug character varying(255) NOT NULL,
    jurisdiction_id character varying(500) NOT NULL,
    parent_id character varying(500)
);


ALTER TABLE entity_body OWNER TO jmcclure;

--
-- Name: entity_jurisdiction; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE entity_jurisdiction (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    division_id character varying(500),
    parent_id character varying(500)
);


ALTER TABLE entity_jurisdiction OWNER TO jmcclure;

--
-- Name: entity_office; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE entity_office (
    uid character varying(500) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    slug character varying(255) NOT NULL,
    body_id character varying(500),
    division_id character varying(500) NOT NULL,
    jurisdiction_id character varying(500)
);


ALTER TABLE entity_office OWNER TO jmcclure;

--
-- Name: entity_person; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE entity_person (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    first_name character varying(255),
    middle_name character varying(255),
    last_name character varying(255) NOT NULL,
    suffix character varying(10)
);


ALTER TABLE entity_person OWNER TO jmcclure;

--
-- Name: geography_division; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE geography_division (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    label character varying(255) NOT NULL,
    short_label character varying(50),
    effective boolean NOT NULL,
    effective_start timestamp with time zone,
    effective_end timestamp with time zone,
    code character varying(200) NOT NULL,
    code_components jsonb,
    level_id character varying(500) NOT NULL,
    parent_id character varying(500)
);


ALTER TABLE geography_division OWNER TO jmcclure;

--
-- Name: geography_divisionlevel; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE geography_divisionlevel (
    uid character varying(500) NOT NULL,
    slug character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    parent_id character varying(500)
);


ALTER TABLE geography_divisionlevel OWNER TO jmcclure;

--
-- Name: geography_geography; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE geography_geography (
    id uuid NOT NULL,
    effective boolean NOT NULL,
    effective_start timestamp with time zone,
    effective_end timestamp with time zone,
    simplification double precision NOT NULL,
    topojson jsonb NOT NULL,
    division_id character varying(500) NOT NULL,
    subdivision_level_id character varying(500) NOT NULL
);


ALTER TABLE geography_geography OWNER TO jmcclure;

--
-- Name: geography_intersectrelationship; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE geography_intersectrelationship (
    id integer NOT NULL,
    intersection numeric(7,6),
    from_division_id character varying(500) NOT NULL,
    to_division_id character varying(500) NOT NULL
);


ALTER TABLE geography_intersectrelationship OWNER TO jmcclure;

--
-- Name: geography_intersectrelationship_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE geography_intersectrelationship_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE geography_intersectrelationship_id_seq OWNER TO jmcclure;

--
-- Name: geography_intersectrelationship_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE geography_intersectrelationship_id_seq OWNED BY geography_intersectrelationship.id;


--
-- Name: vote_apelectionmeta; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_apelectionmeta (
    id uuid NOT NULL,
    ap_election_id character varying(10) NOT NULL,
    called boolean NOT NULL,
    tabulated boolean NOT NULL,
    override_ap_call boolean NOT NULL,
    override_ap_votes boolean NOT NULL,
    precincts_reporting integer,
    precincts_total integer,
    precincts_reporting_pct numeric(5,3),
    ballot_measure_id character varying(500),
    election_id character varying(500),
    CONSTRAINT vote_apelectionmeta_precincts_reporting_check CHECK ((precincts_reporting >= 0)),
    CONSTRAINT vote_apelectionmeta_precincts_total_check CHECK ((precincts_total >= 0))
);


ALTER TABLE vote_apelectionmeta OWNER TO jmcclure;

--
-- Name: vote_delegates; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_delegates (
    id uuid NOT NULL,
    count integer NOT NULL,
    pct numeric(5,3) NOT NULL,
    total integer,
    superdelegates boolean NOT NULL,
    candidate_id character varying(500),
    division_id character varying(500) NOT NULL,
    election_id character varying(500) NOT NULL,
    CONSTRAINT vote_delegates_count_check CHECK ((count >= 0)),
    CONSTRAINT vote_delegates_total_check CHECK ((total >= 0))
);


ALTER TABLE vote_delegates OWNER TO jmcclure;

--
-- Name: vote_electoralvotes; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_electoralvotes (
    id uuid NOT NULL,
    count integer NOT NULL,
    pct numeric(5,3) NOT NULL,
    total integer,
    winning boolean NOT NULL,
    candidate_id character varying(500),
    division_id character varying(500) NOT NULL,
    election_id character varying(500) NOT NULL,
    CONSTRAINT vote_electoralvotes_count_check CHECK ((count >= 0)),
    CONSTRAINT vote_electoralvotes_total_check CHECK ((total >= 0))
);


ALTER TABLE vote_electoralvotes OWNER TO jmcclure;

--
-- Name: vote_elexresult; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_elexresult (
    id integer NOT NULL,
    elexid character varying(80) NOT NULL,
    raceid character varying(5),
    racetype text,
    racetypeid character varying(1),
    ballotorder smallint,
    candidateid text,
    description text,
    delegatecount integer,
    electiondate date,
    electtotal smallint,
    electwon smallint,
    fipscode character varying(5),
    first text,
    incumbent boolean NOT NULL,
    initialization_data boolean NOT NULL,
    is_ballot_measure boolean NOT NULL,
    last text,
    lastupdated timestamp with time zone,
    level text,
    "national" boolean NOT NULL,
    officeid character varying(1),
    officename text,
    party character varying(3),
    polid text,
    polnum text,
    precinctsreporting smallint,
    precinctsreportingpct numeric(7,6),
    precinctstotal smallint,
    reportingunitid text,
    reportingunitname text,
    runoff boolean NOT NULL,
    seatname text,
    seatnum smallint,
    statename text,
    statepostal character varying(2),
    test boolean NOT NULL,
    uncontested boolean NOT NULL,
    votecount integer,
    votepct numeric(7,6),
    winner boolean NOT NULL,
    resultrun_id integer NOT NULL,
    CONSTRAINT vote_elexresult_ballotorder_check CHECK ((ballotorder >= 0)),
    CONSTRAINT vote_elexresult_electtotal_check CHECK ((electtotal >= 0)),
    CONSTRAINT vote_elexresult_electwon_check CHECK ((electwon >= 0)),
    CONSTRAINT vote_elexresult_precinctsreporting_check CHECK ((precinctsreporting >= 0)),
    CONSTRAINT vote_elexresult_precinctstotal_check CHECK ((precinctstotal >= 0)),
    CONSTRAINT vote_elexresult_seatnum_check CHECK ((seatnum >= 0)),
    CONSTRAINT vote_elexresult_votecount_check CHECK ((votecount >= 0))
);


ALTER TABLE vote_elexresult OWNER TO jmcclure;

--
-- Name: vote_elexresult_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE vote_elexresult_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE vote_elexresult_id_seq OWNER TO jmcclure;

--
-- Name: vote_elexresult_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE vote_elexresult_id_seq OWNED BY vote_elexresult.id;


--
-- Name: vote_resultrun; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_resultrun (
    id integer NOT NULL,
    run_time timestamp with time zone NOT NULL
);


ALTER TABLE vote_resultrun OWNER TO jmcclure;

--
-- Name: vote_resultrun_id_seq; Type: SEQUENCE; Schema: public; Owner: jmcclure
--

CREATE SEQUENCE vote_resultrun_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE vote_resultrun_id_seq OWNER TO jmcclure;

--
-- Name: vote_resultrun_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jmcclure
--

ALTER SEQUENCE vote_resultrun_id_seq OWNED BY vote_resultrun.id;


--
-- Name: vote_votes; Type: TABLE; Schema: public; Owner: jmcclure
--

CREATE TABLE vote_votes (
    id uuid NOT NULL,
    count integer NOT NULL,
    pct numeric(5,3) NOT NULL,
    total integer,
    winning boolean NOT NULL,
    ballot_answer_id uuid,
    candidate_id character varying(500),
    division_id character varying(500) NOT NULL,
    election_id character varying(500) NOT NULL,
    CONSTRAINT vote_votes_count_check CHECK ((count >= 0)),
    CONSTRAINT vote_votes_total_check CHECK ((total >= 0))
);


ALTER TABLE vote_votes OWNER TO jmcclure;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: demographic_censusestimate id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusestimate ALTER COLUMN id SET DEFAULT nextval('demographic_censusestimate_id_seq'::regclass);


--
-- Name: demographic_censuslabel id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censuslabel ALTER COLUMN id SET DEFAULT nextval('demographic_censuslabel_id_seq'::regclass);


--
-- Name: demographic_censustable id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censustable ALTER COLUMN id SET DEFAULT nextval('demographic_censustable_id_seq'::regclass);


--
-- Name: demographic_censusvariable id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusvariable ALTER COLUMN id SET DEFAULT nextval('demographic_censusvariable_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: election_candidate_elections id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate_elections ALTER COLUMN id SET DEFAULT nextval('election_candidate_elections_id_seq'::regclass);


--
-- Name: geography_intersectrelationship id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_intersectrelationship ALTER COLUMN id SET DEFAULT nextval('geography_intersectrelationship_id_seq'::regclass);


--
-- Name: vote_elexresult id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_elexresult ALTER COLUMN id SET DEFAULT nextval('vote_elexresult_id_seq'::regclass);


--
-- Name: vote_resultrun id; Type: DEFAULT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_resultrun ALTER COLUMN id SET DEFAULT nextval('vote_resultrun_id_seq'::regclass);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: demographic_censusestimate demographic_censusestimate_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusestimate
    ADD CONSTRAINT demographic_censusestimate_pkey PRIMARY KEY (id);


--
-- Name: demographic_censuslabel demographic_censuslabel_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censuslabel
    ADD CONSTRAINT demographic_censuslabel_pkey PRIMARY KEY (id);


--
-- Name: demographic_censustable demographic_censustable_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censustable
    ADD CONSTRAINT demographic_censustable_pkey PRIMARY KEY (id);


--
-- Name: demographic_censusvariable demographic_censusvariable_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusvariable
    ADD CONSTRAINT demographic_censusvariable_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: election_ballotanswer election_ballotanswer_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_ballotanswer
    ADD CONSTRAINT election_ballotanswer_pkey PRIMARY KEY (id);


--
-- Name: election_ballotmeasure election_ballotmeasure_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_ballotmeasure
    ADD CONSTRAINT election_ballotmeasure_pkey PRIMARY KEY (uid);


--
-- Name: election_candidate_elections election_candidate_elect_candidate_id_election_id_0fc51333_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate_elections
    ADD CONSTRAINT election_candidate_elect_candidate_id_election_id_0fc51333_uniq UNIQUE (candidate_id, election_id);


--
-- Name: election_candidate_elections election_candidate_elections_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate_elections
    ADD CONSTRAINT election_candidate_elections_pkey PRIMARY KEY (id);


--
-- Name: election_candidate election_candidate_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate
    ADD CONSTRAINT election_candidate_pkey PRIMARY KEY (uid);


--
-- Name: election_election election_election_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_pkey PRIMARY KEY (uid);


--
-- Name: election_electioncycle election_electioncycle_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electioncycle
    ADD CONSTRAINT election_electioncycle_pkey PRIMARY KEY (uid);


--
-- Name: election_electioncycle election_electioncycle_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electioncycle
    ADD CONSTRAINT election_electioncycle_slug_key UNIQUE (slug);


--
-- Name: election_electionday election_electionday_date_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electionday
    ADD CONSTRAINT election_electionday_date_key UNIQUE (date);


--
-- Name: election_electionday election_electionday_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electionday
    ADD CONSTRAINT election_electionday_pkey PRIMARY KEY (uid);


--
-- Name: election_electionday election_electionday_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electionday
    ADD CONSTRAINT election_electionday_slug_key UNIQUE (slug);


--
-- Name: election_electiontype election_electiontype_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electiontype
    ADD CONSTRAINT election_electiontype_pkey PRIMARY KEY (uid);


--
-- Name: election_party election_party_ap_code_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_party
    ADD CONSTRAINT election_party_ap_code_key UNIQUE (ap_code);


--
-- Name: election_party election_party_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_party
    ADD CONSTRAINT election_party_pkey PRIMARY KEY (uid);


--
-- Name: election_party election_party_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_party
    ADD CONSTRAINT election_party_slug_key UNIQUE (slug);


--
-- Name: election_race election_race_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_race
    ADD CONSTRAINT election_race_pkey PRIMARY KEY (uid);


--
-- Name: election_race election_race_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_race
    ADD CONSTRAINT election_race_slug_key UNIQUE (slug);


--
-- Name: entity_body entity_body_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_body
    ADD CONSTRAINT entity_body_pkey PRIMARY KEY (uid);


--
-- Name: entity_jurisdiction entity_jurisdiction_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_jurisdiction
    ADD CONSTRAINT entity_jurisdiction_pkey PRIMARY KEY (uid);


--
-- Name: entity_jurisdiction entity_jurisdiction_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_jurisdiction
    ADD CONSTRAINT entity_jurisdiction_slug_key UNIQUE (slug);


--
-- Name: entity_office entity_office_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_office
    ADD CONSTRAINT entity_office_pkey PRIMARY KEY (uid);


--
-- Name: entity_person entity_person_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_person
    ADD CONSTRAINT entity_person_pkey PRIMARY KEY (uid);


--
-- Name: entity_person entity_person_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_person
    ADD CONSTRAINT entity_person_slug_key UNIQUE (slug);


--
-- Name: geography_division geography_division_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_division
    ADD CONSTRAINT geography_division_pkey PRIMARY KEY (uid);


--
-- Name: geography_division geography_division_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_division
    ADD CONSTRAINT geography_division_slug_key UNIQUE (slug);


--
-- Name: geography_divisionlevel geography_divisionlevel_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_divisionlevel
    ADD CONSTRAINT geography_divisionlevel_pkey PRIMARY KEY (uid);


--
-- Name: geography_divisionlevel geography_divisionlevel_slug_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_divisionlevel
    ADD CONSTRAINT geography_divisionlevel_slug_key UNIQUE (slug);


--
-- Name: geography_geography geography_geography_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_geography
    ADD CONSTRAINT geography_geography_pkey PRIMARY KEY (id);


--
-- Name: geography_intersectrelationship geography_intersectrelat_from_division_id_to_divi_68c24f3c_uniq; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_intersectrelationship
    ADD CONSTRAINT geography_intersectrelat_from_division_id_to_divi_68c24f3c_uniq UNIQUE (from_division_id, to_division_id);


--
-- Name: geography_intersectrelationship geography_intersectrelationship_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_intersectrelationship
    ADD CONSTRAINT geography_intersectrelationship_pkey PRIMARY KEY (id);


--
-- Name: vote_apelectionmeta vote_apelectionmeta_ballot_measure_id_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_apelectionmeta
    ADD CONSTRAINT vote_apelectionmeta_ballot_measure_id_key UNIQUE (ballot_measure_id);


--
-- Name: vote_apelectionmeta vote_apelectionmeta_election_id_key; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_apelectionmeta
    ADD CONSTRAINT vote_apelectionmeta_election_id_key UNIQUE (election_id);


--
-- Name: vote_apelectionmeta vote_apelectionmeta_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_apelectionmeta
    ADD CONSTRAINT vote_apelectionmeta_pkey PRIMARY KEY (id);


--
-- Name: vote_delegates vote_delegates_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_delegates
    ADD CONSTRAINT vote_delegates_pkey PRIMARY KEY (id);


--
-- Name: vote_electoralvotes vote_electoralvotes_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_electoralvotes
    ADD CONSTRAINT vote_electoralvotes_pkey PRIMARY KEY (id);


--
-- Name: vote_elexresult vote_elexresult_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_elexresult
    ADD CONSTRAINT vote_elexresult_pkey PRIMARY KEY (id);


--
-- Name: vote_resultrun vote_resultrun_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_resultrun
    ADD CONSTRAINT vote_resultrun_pkey PRIMARY KEY (id);


--
-- Name: vote_votes vote_votes_pkey; Type: CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_votes
    ADD CONSTRAINT vote_votes_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: demographic_censusestimate_division_id_e77ae190; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censusestimate_division_id_e77ae190 ON demographic_censusestimate USING btree (division_id);


--
-- Name: demographic_censusestimate_division_id_e77ae190_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censusestimate_division_id_e77ae190_like ON demographic_censusestimate USING btree (division_id varchar_pattern_ops);


--
-- Name: demographic_censusestimate_variable_id_50968bb8; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censusestimate_variable_id_50968bb8 ON demographic_censusestimate USING btree (variable_id);


--
-- Name: demographic_censuslabel_table_id_0d941c71; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censuslabel_table_id_0d941c71 ON demographic_censuslabel USING btree (table_id);


--
-- Name: demographic_censusvariable_label_id_cd2557b4; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censusvariable_label_id_cd2557b4 ON demographic_censusvariable USING btree (label_id);


--
-- Name: demographic_censusvariable_table_id_2abc469e; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX demographic_censusvariable_table_id_2abc469e ON demographic_censusvariable USING btree (table_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: election_ballotanswer_ballot_measure_id_45550296; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotanswer_ballot_measure_id_45550296 ON election_ballotanswer USING btree (ballot_measure_id);


--
-- Name: election_ballotanswer_ballot_measure_id_45550296_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotanswer_ballot_measure_id_45550296_like ON election_ballotanswer USING btree (ballot_measure_id varchar_pattern_ops);


--
-- Name: election_ballotmeasure_division_id_4807f20c; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotmeasure_division_id_4807f20c ON election_ballotmeasure USING btree (division_id);


--
-- Name: election_ballotmeasure_division_id_4807f20c_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotmeasure_division_id_4807f20c_like ON election_ballotmeasure USING btree (division_id varchar_pattern_ops);


--
-- Name: election_ballotmeasure_election_day_id_42bb0148; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotmeasure_election_day_id_42bb0148 ON election_ballotmeasure USING btree (election_day_id);


--
-- Name: election_ballotmeasure_election_day_id_42bb0148_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotmeasure_election_day_id_42bb0148_like ON election_ballotmeasure USING btree (election_day_id varchar_pattern_ops);


--
-- Name: election_ballotmeasure_uid_52f6e220_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_ballotmeasure_uid_52f6e220_like ON election_ballotmeasure USING btree (uid varchar_pattern_ops);


--
-- Name: election_candidate_elections_candidate_id_098a7b8d; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_elections_candidate_id_098a7b8d ON election_candidate_elections USING btree (candidate_id);


--
-- Name: election_candidate_elections_candidate_id_098a7b8d_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_elections_candidate_id_098a7b8d_like ON election_candidate_elections USING btree (candidate_id varchar_pattern_ops);


--
-- Name: election_candidate_elections_election_id_98bca152; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_elections_election_id_98bca152 ON election_candidate_elections USING btree (election_id);


--
-- Name: election_candidate_elections_election_id_98bca152_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_elections_election_id_98bca152_like ON election_candidate_elections USING btree (election_id varchar_pattern_ops);


--
-- Name: election_candidate_party_id_697ae37b; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_party_id_697ae37b ON election_candidate USING btree (party_id);


--
-- Name: election_candidate_party_id_697ae37b_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_party_id_697ae37b_like ON election_candidate USING btree (party_id varchar_pattern_ops);


--
-- Name: election_candidate_person_id_bef631e2; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_person_id_bef631e2 ON election_candidate USING btree (person_id);


--
-- Name: election_candidate_person_id_bef631e2_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_person_id_bef631e2_like ON election_candidate USING btree (person_id varchar_pattern_ops);


--
-- Name: election_candidate_race_id_a54486a4; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_race_id_a54486a4 ON election_candidate USING btree (race_id);


--
-- Name: election_candidate_race_id_a54486a4_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_race_id_a54486a4_like ON election_candidate USING btree (race_id varchar_pattern_ops);


--
-- Name: election_candidate_top_of_ticket_id_85022767; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_top_of_ticket_id_85022767 ON election_candidate USING btree (top_of_ticket_id);


--
-- Name: election_candidate_top_of_ticket_id_85022767_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_top_of_ticket_id_85022767_like ON election_candidate USING btree (top_of_ticket_id varchar_pattern_ops);


--
-- Name: election_candidate_uid_7913da55_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_candidate_uid_7913da55_like ON election_candidate USING btree (uid varchar_pattern_ops);


--
-- Name: election_election_division_id_5ca34d14; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_division_id_5ca34d14 ON election_election USING btree (division_id);


--
-- Name: election_election_division_id_5ca34d14_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_division_id_5ca34d14_like ON election_election USING btree (division_id varchar_pattern_ops);


--
-- Name: election_election_election_day_id_c1294a4c; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_election_day_id_c1294a4c ON election_election USING btree (election_day_id);


--
-- Name: election_election_election_day_id_c1294a4c_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_election_day_id_c1294a4c_like ON election_election USING btree (election_day_id varchar_pattern_ops);


--
-- Name: election_election_election_type_id_88f62089; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_election_type_id_88f62089 ON election_election USING btree (election_type_id);


--
-- Name: election_election_election_type_id_88f62089_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_election_type_id_88f62089_like ON election_election USING btree (election_type_id varchar_pattern_ops);


--
-- Name: election_election_party_id_9dac0c71; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_party_id_9dac0c71 ON election_election USING btree (party_id);


--
-- Name: election_election_party_id_9dac0c71_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_party_id_9dac0c71_like ON election_election USING btree (party_id varchar_pattern_ops);


--
-- Name: election_election_race_id_0cd827da; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_race_id_0cd827da ON election_election USING btree (race_id);


--
-- Name: election_election_race_id_0cd827da_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_race_id_0cd827da_like ON election_election USING btree (race_id varchar_pattern_ops);


--
-- Name: election_election_uid_e5ed3092_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_election_uid_e5ed3092_like ON election_election USING btree (uid varchar_pattern_ops);


--
-- Name: election_electioncycle_slug_17fd442b_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electioncycle_slug_17fd442b_like ON election_electioncycle USING btree (slug varchar_pattern_ops);


--
-- Name: election_electioncycle_uid_841c929a_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electioncycle_uid_841c929a_like ON election_electioncycle USING btree (uid varchar_pattern_ops);


--
-- Name: election_electionday_cycle_id_348ac829; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electionday_cycle_id_348ac829 ON election_electionday USING btree (cycle_id);


--
-- Name: election_electionday_cycle_id_348ac829_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electionday_cycle_id_348ac829_like ON election_electionday USING btree (cycle_id varchar_pattern_ops);


--
-- Name: election_electionday_slug_c00db7e8_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electionday_slug_c00db7e8_like ON election_electionday USING btree (slug varchar_pattern_ops);


--
-- Name: election_electionday_uid_7d300a12_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electionday_uid_7d300a12_like ON election_electionday USING btree (uid varchar_pattern_ops);


--
-- Name: election_electiontype_uid_7601a7e9_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_electiontype_uid_7601a7e9_like ON election_electiontype USING btree (uid varchar_pattern_ops);


--
-- Name: election_party_ap_code_8db21d2b_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_party_ap_code_8db21d2b_like ON election_party USING btree (ap_code varchar_pattern_ops);


--
-- Name: election_party_slug_91bc78a6_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_party_slug_91bc78a6_like ON election_party USING btree (slug varchar_pattern_ops);


--
-- Name: election_party_uid_030c865e_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_party_uid_030c865e_like ON election_party USING btree (uid varchar_pattern_ops);


--
-- Name: election_race_cycle_id_dbcab3e5; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_cycle_id_dbcab3e5 ON election_race USING btree (cycle_id);


--
-- Name: election_race_cycle_id_dbcab3e5_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_cycle_id_dbcab3e5_like ON election_race USING btree (cycle_id varchar_pattern_ops);


--
-- Name: election_race_office_id_5e1acca2; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_office_id_5e1acca2 ON election_race USING btree (office_id);


--
-- Name: election_race_office_id_5e1acca2_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_office_id_5e1acca2_like ON election_race USING btree (office_id varchar_pattern_ops);


--
-- Name: election_race_slug_bc165c6e_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_slug_bc165c6e_like ON election_race USING btree (slug varchar_pattern_ops);


--
-- Name: election_race_uid_c47d7eb4_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX election_race_uid_c47d7eb4_like ON election_race USING btree (uid varchar_pattern_ops);


--
-- Name: entity_body_jurisdiction_id_57cf432e; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_jurisdiction_id_57cf432e ON entity_body USING btree (jurisdiction_id);


--
-- Name: entity_body_jurisdiction_id_57cf432e_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_jurisdiction_id_57cf432e_like ON entity_body USING btree (jurisdiction_id varchar_pattern_ops);


--
-- Name: entity_body_parent_id_8765253d; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_parent_id_8765253d ON entity_body USING btree (parent_id);


--
-- Name: entity_body_parent_id_8765253d_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_parent_id_8765253d_like ON entity_body USING btree (parent_id varchar_pattern_ops);


--
-- Name: entity_body_slug_e6e4f843; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_slug_e6e4f843 ON entity_body USING btree (slug);


--
-- Name: entity_body_slug_e6e4f843_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_slug_e6e4f843_like ON entity_body USING btree (slug varchar_pattern_ops);


--
-- Name: entity_body_uid_d079e34c_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_body_uid_d079e34c_like ON entity_body USING btree (uid varchar_pattern_ops);


--
-- Name: entity_jurisdiction_division_id_fede494a; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_division_id_fede494a ON entity_jurisdiction USING btree (division_id);


--
-- Name: entity_jurisdiction_division_id_fede494a_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_division_id_fede494a_like ON entity_jurisdiction USING btree (division_id varchar_pattern_ops);


--
-- Name: entity_jurisdiction_parent_id_19e3019f; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_parent_id_19e3019f ON entity_jurisdiction USING btree (parent_id);


--
-- Name: entity_jurisdiction_parent_id_19e3019f_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_parent_id_19e3019f_like ON entity_jurisdiction USING btree (parent_id varchar_pattern_ops);


--
-- Name: entity_jurisdiction_slug_f192be30_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_slug_f192be30_like ON entity_jurisdiction USING btree (slug varchar_pattern_ops);


--
-- Name: entity_jurisdiction_uid_97f513d5_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_jurisdiction_uid_97f513d5_like ON entity_jurisdiction USING btree (uid varchar_pattern_ops);


--
-- Name: entity_office_body_id_24f1e6ca; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_body_id_24f1e6ca ON entity_office USING btree (body_id);


--
-- Name: entity_office_body_id_24f1e6ca_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_body_id_24f1e6ca_like ON entity_office USING btree (body_id varchar_pattern_ops);


--
-- Name: entity_office_division_id_aa90b53d; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_division_id_aa90b53d ON entity_office USING btree (division_id);


--
-- Name: entity_office_division_id_aa90b53d_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_division_id_aa90b53d_like ON entity_office USING btree (division_id varchar_pattern_ops);


--
-- Name: entity_office_jurisdiction_id_60779ef4; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_jurisdiction_id_60779ef4 ON entity_office USING btree (jurisdiction_id);


--
-- Name: entity_office_jurisdiction_id_60779ef4_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_jurisdiction_id_60779ef4_like ON entity_office USING btree (jurisdiction_id varchar_pattern_ops);


--
-- Name: entity_office_slug_1d922551; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_slug_1d922551 ON entity_office USING btree (slug);


--
-- Name: entity_office_slug_1d922551_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_slug_1d922551_like ON entity_office USING btree (slug varchar_pattern_ops);


--
-- Name: entity_office_uid_f7d2ebc5_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_office_uid_f7d2ebc5_like ON entity_office USING btree (uid varchar_pattern_ops);


--
-- Name: entity_person_slug_3f5e89ce_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_person_slug_3f5e89ce_like ON entity_person USING btree (slug varchar_pattern_ops);


--
-- Name: entity_person_uid_cd5b2592_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX entity_person_uid_cd5b2592_like ON entity_person USING btree (uid varchar_pattern_ops);


--
-- Name: geography_division_level_id_70e99489; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_level_id_70e99489 ON geography_division USING btree (level_id);


--
-- Name: geography_division_level_id_70e99489_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_level_id_70e99489_like ON geography_division USING btree (level_id varchar_pattern_ops);


--
-- Name: geography_division_parent_id_409a2e13; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_parent_id_409a2e13 ON geography_division USING btree (parent_id);


--
-- Name: geography_division_parent_id_409a2e13_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_parent_id_409a2e13_like ON geography_division USING btree (parent_id varchar_pattern_ops);


--
-- Name: geography_division_slug_68bf73d1_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_slug_68bf73d1_like ON geography_division USING btree (slug varchar_pattern_ops);


--
-- Name: geography_division_uid_de77c60a_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_division_uid_de77c60a_like ON geography_division USING btree (uid varchar_pattern_ops);


--
-- Name: geography_divisionlevel_parent_id_33ab82a2; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_divisionlevel_parent_id_33ab82a2 ON geography_divisionlevel USING btree (parent_id);


--
-- Name: geography_divisionlevel_parent_id_33ab82a2_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_divisionlevel_parent_id_33ab82a2_like ON geography_divisionlevel USING btree (parent_id varchar_pattern_ops);


--
-- Name: geography_divisionlevel_slug_3af941a9_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_divisionlevel_slug_3af941a9_like ON geography_divisionlevel USING btree (slug varchar_pattern_ops);


--
-- Name: geography_divisionlevel_uid_a851ab0e_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_divisionlevel_uid_a851ab0e_like ON geography_divisionlevel USING btree (uid varchar_pattern_ops);


--
-- Name: geography_geography_division_id_c69612c9; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_geography_division_id_c69612c9 ON geography_geography USING btree (division_id);


--
-- Name: geography_geography_division_id_c69612c9_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_geography_division_id_c69612c9_like ON geography_geography USING btree (division_id varchar_pattern_ops);


--
-- Name: geography_geography_subdivision_level_id_d93ecd15; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_geography_subdivision_level_id_d93ecd15 ON geography_geography USING btree (subdivision_level_id);


--
-- Name: geography_geography_subdivision_level_id_d93ecd15_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_geography_subdivision_level_id_d93ecd15_like ON geography_geography USING btree (subdivision_level_id varchar_pattern_ops);


--
-- Name: geography_intersectrelationship_from_division_id_88e70af4; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_intersectrelationship_from_division_id_88e70af4 ON geography_intersectrelationship USING btree (from_division_id);


--
-- Name: geography_intersectrelationship_from_division_id_88e70af4_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_intersectrelationship_from_division_id_88e70af4_like ON geography_intersectrelationship USING btree (from_division_id varchar_pattern_ops);


--
-- Name: geography_intersectrelationship_to_division_id_fccce1ba; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_intersectrelationship_to_division_id_fccce1ba ON geography_intersectrelationship USING btree (to_division_id);


--
-- Name: geography_intersectrelationship_to_division_id_fccce1ba_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX geography_intersectrelationship_to_division_id_fccce1ba_like ON geography_intersectrelationship USING btree (to_division_id varchar_pattern_ops);


--
-- Name: vote_apelectionmeta_ballot_measure_id_e3dc7910_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_apelectionmeta_ballot_measure_id_e3dc7910_like ON vote_apelectionmeta USING btree (ballot_measure_id varchar_pattern_ops);


--
-- Name: vote_apelectionmeta_election_id_516d6916_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_apelectionmeta_election_id_516d6916_like ON vote_apelectionmeta USING btree (election_id varchar_pattern_ops);


--
-- Name: vote_delegates_candidate_id_5d3a58d4; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_candidate_id_5d3a58d4 ON vote_delegates USING btree (candidate_id);


--
-- Name: vote_delegates_candidate_id_5d3a58d4_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_candidate_id_5d3a58d4_like ON vote_delegates USING btree (candidate_id varchar_pattern_ops);


--
-- Name: vote_delegates_division_id_aceab9bf; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_division_id_aceab9bf ON vote_delegates USING btree (division_id);


--
-- Name: vote_delegates_division_id_aceab9bf_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_division_id_aceab9bf_like ON vote_delegates USING btree (division_id varchar_pattern_ops);


--
-- Name: vote_delegates_election_id_839a511c; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_election_id_839a511c ON vote_delegates USING btree (election_id);


--
-- Name: vote_delegates_election_id_839a511c_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_delegates_election_id_839a511c_like ON vote_delegates USING btree (election_id varchar_pattern_ops);


--
-- Name: vote_electoralvotes_candidate_id_7173db64; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_candidate_id_7173db64 ON vote_electoralvotes USING btree (candidate_id);


--
-- Name: vote_electoralvotes_candidate_id_7173db64_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_candidate_id_7173db64_like ON vote_electoralvotes USING btree (candidate_id varchar_pattern_ops);


--
-- Name: vote_electoralvotes_division_id_b02db950; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_division_id_b02db950 ON vote_electoralvotes USING btree (division_id);


--
-- Name: vote_electoralvotes_division_id_b02db950_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_division_id_b02db950_like ON vote_electoralvotes USING btree (division_id varchar_pattern_ops);


--
-- Name: vote_electoralvotes_election_id_3d5db6c9; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_election_id_3d5db6c9 ON vote_electoralvotes USING btree (election_id);


--
-- Name: vote_electoralvotes_election_id_3d5db6c9_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_electoralvotes_election_id_3d5db6c9_like ON vote_electoralvotes USING btree (election_id varchar_pattern_ops);


--
-- Name: vote_elexresult_resultrun_id_7e1dad1e; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_elexresult_resultrun_id_7e1dad1e ON vote_elexresult USING btree (resultrun_id);


--
-- Name: vote_votes_ballot_answer_id_d6b69f87; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_ballot_answer_id_d6b69f87 ON vote_votes USING btree (ballot_answer_id);


--
-- Name: vote_votes_candidate_id_c2ee861f; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_candidate_id_c2ee861f ON vote_votes USING btree (candidate_id);


--
-- Name: vote_votes_candidate_id_c2ee861f_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_candidate_id_c2ee861f_like ON vote_votes USING btree (candidate_id varchar_pattern_ops);


--
-- Name: vote_votes_division_id_06c95b13; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_division_id_06c95b13 ON vote_votes USING btree (division_id);


--
-- Name: vote_votes_division_id_06c95b13_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_division_id_06c95b13_like ON vote_votes USING btree (division_id varchar_pattern_ops);


--
-- Name: vote_votes_election_id_17b78187; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_election_id_17b78187 ON vote_votes USING btree (election_id);


--
-- Name: vote_votes_election_id_17b78187_like; Type: INDEX; Schema: public; Owner: jmcclure
--

CREATE INDEX vote_votes_election_id_17b78187_like ON vote_votes USING btree (election_id varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demographic_censusestimate demographic_censuses_division_id_e77ae190_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusestimate
    ADD CONSTRAINT demographic_censuses_division_id_e77ae190_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demographic_censusestimate demographic_censuses_variable_id_50968bb8_fk_demograph; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusestimate
    ADD CONSTRAINT demographic_censuses_variable_id_50968bb8_fk_demograph FOREIGN KEY (variable_id) REFERENCES demographic_censusvariable(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demographic_censuslabel demographic_censusla_table_id_0d941c71_fk_demograph; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censuslabel
    ADD CONSTRAINT demographic_censusla_table_id_0d941c71_fk_demograph FOREIGN KEY (table_id) REFERENCES demographic_censustable(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demographic_censusvariable demographic_censusva_label_id_cd2557b4_fk_demograph; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusvariable
    ADD CONSTRAINT demographic_censusva_label_id_cd2557b4_fk_demograph FOREIGN KEY (label_id) REFERENCES demographic_censuslabel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: demographic_censusvariable demographic_censusva_table_id_2abc469e_fk_demograph; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY demographic_censusvariable
    ADD CONSTRAINT demographic_censusva_table_id_2abc469e_fk_demograph FOREIGN KEY (table_id) REFERENCES demographic_censustable(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_ballotanswer election_ballotanswe_ballot_measure_id_45550296_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_ballotanswer
    ADD CONSTRAINT election_ballotanswe_ballot_measure_id_45550296_fk_election_ FOREIGN KEY (ballot_measure_id) REFERENCES election_ballotmeasure(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_ballotmeasure election_ballotmeasu_division_id_4807f20c_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_ballotmeasure
    ADD CONSTRAINT election_ballotmeasu_division_id_4807f20c_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_ballotmeasure election_ballotmeasu_election_day_id_42bb0148_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_ballotmeasure
    ADD CONSTRAINT election_ballotmeasu_election_day_id_42bb0148_fk_election_ FOREIGN KEY (election_day_id) REFERENCES election_electionday(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate_elections election_candidate_e_candidate_id_098a7b8d_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate_elections
    ADD CONSTRAINT election_candidate_e_candidate_id_098a7b8d_fk_election_ FOREIGN KEY (candidate_id) REFERENCES election_candidate(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate_elections election_candidate_e_election_id_98bca152_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate_elections
    ADD CONSTRAINT election_candidate_e_election_id_98bca152_fk_election_ FOREIGN KEY (election_id) REFERENCES election_election(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate election_candidate_party_id_697ae37b_fk_election_party_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate
    ADD CONSTRAINT election_candidate_party_id_697ae37b_fk_election_party_uid FOREIGN KEY (party_id) REFERENCES election_party(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate election_candidate_person_id_bef631e2_fk_entity_person_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate
    ADD CONSTRAINT election_candidate_person_id_bef631e2_fk_entity_person_uid FOREIGN KEY (person_id) REFERENCES entity_person(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate election_candidate_race_id_a54486a4_fk_election_race_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate
    ADD CONSTRAINT election_candidate_race_id_a54486a4_fk_election_race_uid FOREIGN KEY (race_id) REFERENCES election_race(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_candidate election_candidate_top_of_ticket_id_85022767_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_candidate
    ADD CONSTRAINT election_candidate_top_of_ticket_id_85022767_fk_election_ FOREIGN KEY (top_of_ticket_id) REFERENCES election_candidate(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_election election_election_division_id_5ca34d14_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_division_id_5ca34d14_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_election election_election_election_day_id_c1294a4c_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_election_day_id_c1294a4c_fk_election_ FOREIGN KEY (election_day_id) REFERENCES election_electionday(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_election election_election_election_type_id_88f62089_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_election_type_id_88f62089_fk_election_ FOREIGN KEY (election_type_id) REFERENCES election_electiontype(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_election election_election_party_id_9dac0c71_fk_election_party_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_party_id_9dac0c71_fk_election_party_uid FOREIGN KEY (party_id) REFERENCES election_party(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_election election_election_race_id_0cd827da_fk_election_race_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_election
    ADD CONSTRAINT election_election_race_id_0cd827da_fk_election_race_uid FOREIGN KEY (race_id) REFERENCES election_race(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_electionday election_electionday_cycle_id_348ac829_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_electionday
    ADD CONSTRAINT election_electionday_cycle_id_348ac829_fk_election_ FOREIGN KEY (cycle_id) REFERENCES election_electioncycle(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_race election_race_cycle_id_dbcab3e5_fk_election_electioncycle_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_race
    ADD CONSTRAINT election_race_cycle_id_dbcab3e5_fk_election_electioncycle_uid FOREIGN KEY (cycle_id) REFERENCES election_electioncycle(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: election_race election_race_office_id_5e1acca2_fk_entity_office_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY election_race
    ADD CONSTRAINT election_race_office_id_5e1acca2_fk_entity_office_uid FOREIGN KEY (office_id) REFERENCES entity_office(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_body entity_body_jurisdiction_id_57cf432e_fk_entity_jurisdiction_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_body
    ADD CONSTRAINT entity_body_jurisdiction_id_57cf432e_fk_entity_jurisdiction_uid FOREIGN KEY (jurisdiction_id) REFERENCES entity_jurisdiction(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_body entity_body_parent_id_8765253d_fk_entity_body_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_body
    ADD CONSTRAINT entity_body_parent_id_8765253d_fk_entity_body_uid FOREIGN KEY (parent_id) REFERENCES entity_body(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_jurisdiction entity_jurisdiction_division_id_fede494a_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_jurisdiction
    ADD CONSTRAINT entity_jurisdiction_division_id_fede494a_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_jurisdiction entity_jurisdiction_parent_id_19e3019f_fk_entity_ju; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_jurisdiction
    ADD CONSTRAINT entity_jurisdiction_parent_id_19e3019f_fk_entity_ju FOREIGN KEY (parent_id) REFERENCES entity_jurisdiction(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_office entity_office_body_id_24f1e6ca_fk_entity_body_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_office
    ADD CONSTRAINT entity_office_body_id_24f1e6ca_fk_entity_body_uid FOREIGN KEY (body_id) REFERENCES entity_body(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_office entity_office_division_id_aa90b53d_fk_geography_division_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_office
    ADD CONSTRAINT entity_office_division_id_aa90b53d_fk_geography_division_uid FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: entity_office entity_office_jurisdiction_id_60779ef4_fk_entity_ju; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY entity_office
    ADD CONSTRAINT entity_office_jurisdiction_id_60779ef4_fk_entity_ju FOREIGN KEY (jurisdiction_id) REFERENCES entity_jurisdiction(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_division geography_division_level_id_70e99489_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_division
    ADD CONSTRAINT geography_division_level_id_70e99489_fk_geography FOREIGN KEY (level_id) REFERENCES geography_divisionlevel(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_division geography_division_parent_id_409a2e13_fk_geography_division_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_division
    ADD CONSTRAINT geography_division_parent_id_409a2e13_fk_geography_division_uid FOREIGN KEY (parent_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_divisionlevel geography_divisionle_parent_id_33ab82a2_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_divisionlevel
    ADD CONSTRAINT geography_divisionle_parent_id_33ab82a2_fk_geography FOREIGN KEY (parent_id) REFERENCES geography_divisionlevel(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_geography geography_geography_division_id_c69612c9_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_geography
    ADD CONSTRAINT geography_geography_division_id_c69612c9_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_geography geography_geography_subdivision_level_id_d93ecd15_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_geography
    ADD CONSTRAINT geography_geography_subdivision_level_id_d93ecd15_fk_geography FOREIGN KEY (subdivision_level_id) REFERENCES geography_divisionlevel(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_intersectrelationship geography_intersectr_from_division_id_88e70af4_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_intersectrelationship
    ADD CONSTRAINT geography_intersectr_from_division_id_88e70af4_fk_geography FOREIGN KEY (from_division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: geography_intersectrelationship geography_intersectr_to_division_id_fccce1ba_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY geography_intersectrelationship
    ADD CONSTRAINT geography_intersectr_to_division_id_fccce1ba_fk_geography FOREIGN KEY (to_division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_apelectionmeta vote_apelectionmeta_ballot_measure_id_e3dc7910_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_apelectionmeta
    ADD CONSTRAINT vote_apelectionmeta_ballot_measure_id_e3dc7910_fk_election_ FOREIGN KEY (ballot_measure_id) REFERENCES election_ballotmeasure(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_apelectionmeta vote_apelectionmeta_election_id_516d6916_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_apelectionmeta
    ADD CONSTRAINT vote_apelectionmeta_election_id_516d6916_fk_election_ FOREIGN KEY (election_id) REFERENCES election_election(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_delegates vote_delegates_candidate_id_5d3a58d4_fk_election_candidate_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_delegates
    ADD CONSTRAINT vote_delegates_candidate_id_5d3a58d4_fk_election_candidate_uid FOREIGN KEY (candidate_id) REFERENCES election_candidate(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_delegates vote_delegates_division_id_aceab9bf_fk_geography_division_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_delegates
    ADD CONSTRAINT vote_delegates_division_id_aceab9bf_fk_geography_division_uid FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_delegates vote_delegates_election_id_839a511c_fk_election_election_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_delegates
    ADD CONSTRAINT vote_delegates_election_id_839a511c_fk_election_election_uid FOREIGN KEY (election_id) REFERENCES election_election(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_electoralvotes vote_electoralvotes_candidate_id_7173db64_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_electoralvotes
    ADD CONSTRAINT vote_electoralvotes_candidate_id_7173db64_fk_election_ FOREIGN KEY (candidate_id) REFERENCES election_candidate(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_electoralvotes vote_electoralvotes_division_id_b02db950_fk_geography; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_electoralvotes
    ADD CONSTRAINT vote_electoralvotes_division_id_b02db950_fk_geography FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_electoralvotes vote_electoralvotes_election_id_3d5db6c9_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_electoralvotes
    ADD CONSTRAINT vote_electoralvotes_election_id_3d5db6c9_fk_election_ FOREIGN KEY (election_id) REFERENCES election_election(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_elexresult vote_elexresult_resultrun_id_7e1dad1e_fk_vote_resultrun_id; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_elexresult
    ADD CONSTRAINT vote_elexresult_resultrun_id_7e1dad1e_fk_vote_resultrun_id FOREIGN KEY (resultrun_id) REFERENCES vote_resultrun(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_votes vote_votes_ballot_answer_id_d6b69f87_fk_election_; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_votes
    ADD CONSTRAINT vote_votes_ballot_answer_id_d6b69f87_fk_election_ FOREIGN KEY (ballot_answer_id) REFERENCES election_ballotanswer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_votes vote_votes_candidate_id_c2ee861f_fk_election_candidate_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_votes
    ADD CONSTRAINT vote_votes_candidate_id_c2ee861f_fk_election_candidate_uid FOREIGN KEY (candidate_id) REFERENCES election_candidate(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_votes vote_votes_division_id_06c95b13_fk_geography_division_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_votes
    ADD CONSTRAINT vote_votes_division_id_06c95b13_fk_geography_division_uid FOREIGN KEY (division_id) REFERENCES geography_division(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vote_votes vote_votes_election_id_17b78187_fk_election_election_uid; Type: FK CONSTRAINT; Schema: public; Owner: jmcclure
--

ALTER TABLE ONLY vote_votes
    ADD CONSTRAINT vote_votes_election_id_17b78187_fk_election_election_uid FOREIGN KEY (election_id) REFERENCES election_election(uid) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

