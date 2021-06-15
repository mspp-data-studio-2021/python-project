python-project
==============

This is an example project to illustrate some organization and reproducability concepts for the _Policy & Data Studio_ course in Summer 2021. 

## Getting Started

You will first need to download and install [Python3](https://realpython.com/installing-python/).

Then clone this project repository, and open a command prompt/terminal window and naviate to the project directory. 

Now you can create a virtual environment for python. On Mac OS you can use the following steps:

```
pip3 install virtualenv # if you don't already have this installed
virtualenv env
source env/bin/activate
which python # confirm you are using the virtual env
pip3 install -r requirements.txt
python -m ipykernel install --user --name=env
jupyter notebook
```

## Replicating the Analysis

To recreate all the results you will need to run all of the numbered scripts and notebooks in [`/code`](/code):

Alternatively, you can run each step individually following the numbered ordering of files:

* [`01_download-tracts.py`](code/01_download-tracts.py)
  * This downloads a shapefile for all NYC census tracts (2010) from NYC's Open Data portal, and saves the files in [`/data/raw`](/data/raw)
* [`02_download-acs.py`](code/02_download-acs.py)
  * This downloads ACS summary file data for NYC tracts from a [separate project](https://github.com/mspp-data-studio-2021/r-project), where it was originally downloaded with R using the [`tidycensus`](https://walker-data.com/tidycensus/) package to access the Census API. 
* [`03_clean-join-tract-data.ipynb`](code/03_clean-join-tract-data.ipynb)
  * This reads in the two raw data files created above, and claculates some new ACS variables and joins the ACS data with the tract geometries from the shapefile. The final clean tract-level dataset with geometries is saved to [`/data/clean`](/data/clean)
* [`99-1_tract-maps.ipynb`](code/99-1_tract-maps.ipynb)
  * This notebook reads in the clean tract dataset and produces some maps. The map files are saved to [`/img`](/img) and the rendered notebook is saved to [`/docs`](/docs)
