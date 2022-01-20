import requests
from datetime import datetime

from core.models import ViralLoad, Patient
from core.utils.constants import Constants
from core.utils.data_convertion import DataConversion


class LabData:

    def post_data(self, base_url):
        payload = {}
        obs = {}
        #viralLoad = ViralLoad.objects.filter(synced=False)
        viralLoad = ViralLoad.objects.filter(nid='0107070701/2021/00255')
        for vl in viralLoad:
            patient = Patient.objects.get(nid=vl.nid)
            if patient is not None:
                payload['encounterDatetime'] = DataConversion.format_datetime(
                    datetime.now())
                payload['patient'] = patient.patient_uuid
                payload['encounterType'] = Constants().get_uuids().get(
                    'encounter_type')
                # TODO: Get Location according to the data comming from excel file
                payload['location'] = Constants().get_uuids().get('hpt')
                provider = {
                    'provider': Constants().get_uuids().get('provider')}
                encounterRole = {
                    'encounterRole': Constants().get_uuids().get('encounter_role')}
                payload['encounterProviders'] = [provider, encounterRole]
                obs['person'] = patient.patient_uuid
                obs['obsDateTime'] = DataConversion.format_datetime(
                    datetime.now())
                obs['concept'] = Constants().get_uuids().get('data_pedido_obs')
                obs['value'] = str(DataConversion.format_datetime(
                    datetime.now()))  # vl.capture_date
                obs_list = []
                obs_list.append(obs)
                obs['person'] = patient.patient_uuid
                obs['obsDateTime'] = DataConversion.format_datetime(
                    datetime.now())
                obs['concept'] = Constants().get_uuids().get(
                    'data_colheita_obs')
                obs['value'] = str(DataConversion.format_datetime(
                    datetime.now()))  # vl.access_date
                obs_list.append(obs)
                if vl.viral_load:
                    obs['person'] = patient.patient_uuid
                    obs['obsDateTime'] = DataConversion.format_datetime(
                        datetime.now())
                    obs['concept'] = Constants().get_uuids().get(
                        'valor_carga_concept')
                    obs['value'] = str(vl.viral_load)
                    obs_list.append(obs)
                elif vl.viral_load_qualitative:
                    obs['person'] = patient.patient_uuid
                    obs['obsDateTime'] = DataConversion.format_datetime(
                        datetime.now())
                    obs['concept'] = Constants().get_uuids().get(
                        'qualidade_carga_question')
                    obs['value'] = 'Indectetavel'
                    obs_list.append(obs)
                payload['obs'] = obs_list
                payload['form'] = Constants().get_uuids().get('form')
                try:
                    response = requests.post(
                        base_url, data=payload, auth=Constants.AUTH)
                    print(f' STATUS: {response.status_code}')
                    print(f'Response: {response.text}')
                    print(f'Payload: {payload}')
                except requests.exceptions.RequestException as err:
                    print(err)
            else:
                print('No patient with specified NID')
