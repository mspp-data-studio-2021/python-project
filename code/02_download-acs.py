from pathlib import Path
import shutil
import requests

proj_dir = Path(__file__).parent.parent

raw_dir = proj_dir / 'data' / 'raw'

raw_dir.mkdir(parents=True, exist_ok=True)

file_path = raw_dir / 'acs-2018-nyc-tracts.feather'

file_url = 'http://github.com/wagner-mspp-2020/r-project/raw/master/data/raw/acs-2018-nyc-tracts.feather'

if not file_path.exists():
	r = requests.get(file_url)
	with open('acs-2018-nyc-tracts.feather', 'wb') as f:
		f.write(r.content)
