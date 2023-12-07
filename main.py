from fastapi import FastAPI
import json
from controllers.data_accesor import get_nerds_by_year, get_nceds_by_year, \
	merge_data, agg_nceds, get_agg_data, get_data_json
from models.schema import NCEDItem, NCEDNerdItem
from typing import List
from data.datamap import state_id_file

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello World"}
@app.get("/data/json/{year}")
async def data_json(year: str):

	return get_data_json(year)
@app.get("/state/{stateid}")
async def district_json(stateid: str):
	# with open('data/tl_2019_45_unsd.json') as f:
	# with open('data/testalabama.json') as f:
	if stateid in state_id_file:
		with open('data/district_topojson/' + state_id_file[stateid]) as f:
			d = json.load(f)
	return {"data": d, "key": state_id_file[stateid][:-5]}
