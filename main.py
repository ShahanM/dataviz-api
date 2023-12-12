from fastapi import FastAPI
import json
from controllers.data_accesor import get_data_json
from data.datamap import state_id_file, state_id_datafile
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    root_path='/dataviz/api/',
)


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


@app.get("/data/{stateid}")
async def state_data(stateid: str):
	if stateid in state_id_datafile:
		with open('data/states/' + state_id_datafile[stateid]) as f:
			d = json.load(f)
		return {'data': d, 'key': state_id_datafile[stateid][:-5]}
	return {'data': {}, 'key': stateid}


@app.get("/state/{stateid}")
async def district_json(stateid: str):
	if stateid in state_id_file:
		with open('data/district_topojson/' + state_id_file[stateid]) as f:
			d = json.load(f)
		return {"data": d, "key": state_id_file[stateid][:-5]}
	return {'data': {}, 'key': stateid}
