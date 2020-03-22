from datetime import datetime
import pycovid.sources.base_source

WHO_API_URL = 'https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Cases_by_country_pt_V3/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&maxAllowableOffset=78271&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100&resultType=tile'

class Who(pycovid.sources.base_source.CovidDataSource):
    def pullData(self):
        results = []
        who_data = self.requestJSON(WHO_API_URL)

        for feature in who_data['features']:
            attributes = feature['attributes']
            results.append(pycovid.sources.base_source.CovidDataResult(
                attributes['ADM0_NAME'], 
                datetime.fromtimestamp(attributes['DateOfReport'] / 1000),
                attributes['cum_death'],
                attributes['cum_conf']
            ))

        return results