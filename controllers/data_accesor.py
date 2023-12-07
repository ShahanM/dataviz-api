def get_data_json(year: str) -> str:
	json_path = f'{DATA_PATHS[year]}/agg_merged.json'

	if Path(json_path).exists():

		with open(json_path) as f:
			d = json.load(f)

		return d

	return ''
