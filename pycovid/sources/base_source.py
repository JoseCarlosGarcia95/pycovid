import requests

class CovidDataSource:
    def pullData(self):
        raise "Method not implemented"

    def requestApi(self, endpoint, method = 'get', body = None):
        return getattr(requests, method)(endpoint, data = body)

    def requestJSON(self, endpoint, method = 'get', body = None):
        response = self.requestApi(endpoint, method, body)
        return response.json()

class CovidDataResult:
    def __init__(self, country, updated, total_deaths, total_hospital):
        self.country = country
        self.updated = updated
        self.total_deaths = total_deaths
        self.total_hospital = total_hospital

    def dump(self):
        return {
            'country': self.country,
            'updated': self.updated,
            'total_deaths': self.total_deaths,
            'total_hospital': self.total_hospital
        }