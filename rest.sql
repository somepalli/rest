--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.10
-- Dumped by pg_dump version 9.3.10
-- Started on 2016-01-12 14:31:40 IST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 175 (class 1259 OID 855660)
-- Name: master_repayment_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE master_repayment_type (
    id bigint NOT NULL,
    repayment_type_name character varying NOT NULL,
    fk_status_id bigint NOT NULL,
    last_modified_date timestamp with time zone NOT NULL,
    last_modified_by bigint NOT NULL,
    master_repayment_type_json text
);


--
-- TOC entry 174 (class 1259 OID 855658)
-- Name: master_repayment_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE master_repayment_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1990 (class 0 OID 0)
-- Dependencies: 174
-- Name: master_repayment_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE master_repayment_type_id_seq OWNED BY master_repayment_type.id;


--
-- TOC entry 173 (class 1259 OID 855650)
-- Name: master_status; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE master_status (
    id bigint NOT NULL,
    type character varying(10) NOT NULL,
    last_updated_date timestamp with time zone NOT NULL
);


--
-- TOC entry 172 (class 1259 OID 855648)
-- Name: master_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE master_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1991 (class 0 OID 0)
-- Dependencies: 172
-- Name: master_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE master_status_id_seq OWNED BY master_status.id;


--
-- TOC entry 1871 (class 2604 OID 855663)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY master_repayment_type ALTER COLUMN id SET DEFAULT nextval('master_repayment_type_id_seq'::regclass);


--
-- TOC entry 1870 (class 2604 OID 855653)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY master_status ALTER COLUMN id SET DEFAULT nextval('master_status_id_seq'::regclass);


--
-- TOC entry 1877 (class 2606 OID 855668)
-- Name: master_repayment_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY master_repayment_type
    ADD CONSTRAINT master_repayment_type_pkey PRIMARY KEY (id);


--
-- TOC entry 1873 (class 2606 OID 855655)
-- Name: master_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY master_status
    ADD CONSTRAINT master_status_pkey PRIMARY KEY (id);


--
-- TOC entry 1875 (class 2606 OID 855657)
-- Name: master_status_type_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY master_status
    ADD CONSTRAINT master_status_type_key UNIQUE (type);


--
-- TOC entry 1878 (class 2606 OID 855669)
-- Name: master_repayment_type_fk_status_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY master_repayment_type
    ADD CONSTRAINT master_repayment_type_fk_status_fkey FOREIGN KEY (fk_status_id) REFERENCES master_status(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


-- Completed on 2016-01-12 14:31:40 IST

--
-- PostgreSQL database dump complete
--

