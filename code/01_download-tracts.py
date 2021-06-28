from pathlib import Path
import zipfile
import requests

proj_dir = Path(__file__).parent.parent

file_url = 'https://data.cityofnewyork.us/api/geospatial/fxpq-c8ku?method=export&format=Original'

raw_dir = proj_dir / 'data' / 'raw'
clean_dir = proj_dir / 'data' / 'clean'

raw_dir.mkdir(parents=True, exist_ok=True)
clean_dir.mkdir(parents=True, exist_ok=True)

zip_file = raw_dir / 'nyc-tracts-2010.zip'
shp_file = raw_dir / 'nyc-tracts-2010.shp'

if not zip_file.exists() and not shp_file.exists():
	r = requests.get(file_url)
	with open('data/raw/nyc-tracts-2010.zip', 'wb') as f:
		f.write(r.content)

if not shp_file.exists():
	zipfile.ZipFile(zip_file).extractall(raw_dir)

zip_file.unlink()
