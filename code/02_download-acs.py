import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# since we retrieved all the data from the API in the R process, we don't 
# actually need to access our Census API key, but to illustrate the process 
# this is how you would use dotenv library for this

load_dotenv()  # take environment variables from .env

api_key = os.environ.get('CENSUS_API_KEY', '')


proj_dir = Path(__file__).parent.parent

raw_dir = proj_dir / 'data' / 'raw'

raw_dir.mkdir(parents=True, exist_ok=True)

file_path = raw_dir / 'acs-2018-nyc-tracts.feather'

file_url = 'http://github.com/wagner-mspp-2020/r-project/raw/master/data/raw/acs-2018-nyc-tracts.feather'

if not file_path.exists():
	r = requests.get(file_url)
	with open('acs-2018-nyc-tracts.feather', 'wb') as f:
		f.write(r.content)
