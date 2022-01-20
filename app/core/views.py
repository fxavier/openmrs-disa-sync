from django.shortcuts import render
from core.forms import ExcelForm
from core.models import CsvFile, ExcelFile, ViralLoad
from core.utils.data_convertion import DataConversion
from core.service.data_from_openmrs import OpenMRSData
from core.service.post_labdata import LabData


import csv
import pandas as pd


def upload_excel_file(request):
    form = ExcelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExcelForm()
        excel_file = ExcelFile.objects.get(activated=False)
        with open(excel_file.file_name.path, 'rb') as file:
            df = pd.read_excel(
                file, sheet_name='Resultados da Análise', skiprows=[0, 1, 2])
            df.to_csv(r'laboratorio.csv', index=None,
                      header=True, encoding='utf-8')
            excel_file.activated = True
            excel_file.save()

        with open('laboratorio.csv', 'r') as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                if str(row[56]).startswith('<'):
                    viral_load_data = ''
                    viral_load_qualitative_data = row[56]
                elif str(row[56]) is None:
                    viral_load_qualitative_data = row[58]
                else:
                    viral_load_data = row[56]
                    viral_load_qualitative_data = row[58]
                viralLoad = ViralLoad.objects.create(
                    laboratory_id=row[0],
                    sector=row[5],
                    number_orig_lab=row[7],
                    province=row[9],
                    district=row[11],
                    health_facility=row[12],
                    patient_name=row[14],
                    gender=row[22],
                    reference=row[23],
                    capture_date=DataConversion.convert_to_datetime(
                        str(row[32])),
                    access_date=DataConversion.convert_to_datetime(
                        str(row[34])),
                    nid=DataConversion.format_nid(str(row[41])),
                    viral_load=viral_load_data,
                    viral_load_qualitative=viral_load_qualitative_data
                )
                viralLoad.save()
                ViralLoad.objects.filter(nid="").delete()
                ViralLoad.objects.filter(viral_load__contains="NAME").delete()

            patients = OpenMRSData()
            patients.fetch_patient_data(
                'ws/rest/v1/reportingrest/dataSet/00796d15-890f-4cec-95d3-046caebe00db')
            LabData().post_data('http://197.218.241.174:8080/hpt/ws/rest/v1/encounter')

    return render(request, 'app/upload.html', {'form': form})
