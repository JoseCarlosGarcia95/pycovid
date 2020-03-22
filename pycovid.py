#!/usr/bin/env python 

from pycovid import PyCovid
from pycovid.sources.who import Who


covid = PyCovid()
dataByCountries = covid.pullDataFromSource(Who())

bydeath = covid.sortByHospital(dataByCountries)

print(covid.exportJSON(bydeath))