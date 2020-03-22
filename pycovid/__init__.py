
class PyCovid:
    
    def __init__(self):
        pass

    def pullDataFromSource(self, source):
        return source.pullData()        

    def sortByDeaths(self, data):
        return sorted(data, key = lambda e: e.total_deaths, reverse = True)

    def sortByHospital(self, data):
        return sorted(data, key = lambda e: e.total_hospital, reverse = True)

    def exportJSON(self, data):
        data_to_export = {}

        for all_data in data:
            data_to_export[all_data.country] = all_data.dump()

        return data_to_export