from fastapi import FastAPI
import json
from controllers.data_accesor import get_data_json
from models.schema import NCEDItem, NCEDNerdItem
from typing import List
from data.datamap import state_id_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    root_path='/dataviz/api/',
)

# contact={
#     'name': '',
#     'url': '',
#     'email': '',
# },
# license_info={
#     'name': '',
#     'url': '',
# }


origins = [
    'http://localhost:3000',
    'http://localhost:3000/*',
    'http://localhost:3001/*',
	'https://shahanm.github.io/math-factors/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


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
