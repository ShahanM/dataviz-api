from typing import List, Optional, Literal, Union
from pydantic import BaseModel


class NCEDItem(BaseModel):
	nced_id: str
	state_name: str
	fpist: str
	schoolname: str
	state_school_id: str
	state_nced_id: str
	num_students: int
	total_proficient: int
	raw_percent_proficient: str


class NCEDNerdItem(BaseModel):
	nced_id: str
	state_name: str
	fpist: str
	schoolname: str
	state_school_id: str
	state_nced_id: str
	num_students: int
	total_proficient: int
	raw_percent_proficient: str
	state: str
	year: str
	distid_stateassigned: str
	schoolid_stateassigned: str
	distname: str
	census_id: str
	ncesid: str
	pp_stloc_raw: str
	pp_fed_raw: str
	pp_total_raw: str