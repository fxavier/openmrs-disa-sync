import requests

from core.utils.constants import Constants
from core.models import Patient


class OpenMRSData:

    def fetch_patient_data(self, endpoint):
        url = Constants.BASE_URL + endpoint
        try:
            response = requests.get(url, auth=('admin', 'eSaude123'))
            json_data = response.json()['rows']
            print(json_data)
            for data in json_data:
                patient, created = Patient.objects.get_or_create(
                    patient_uuid=data['uuid'],
                    # patient_id=data['person_id'],
                    nid=data['NID'],
                    patient_name=data['NomeCompleto']
                )
                patient.save()

        except requests.exceptions.RequestException as err:
            print(err)
