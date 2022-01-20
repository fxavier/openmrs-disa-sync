from django.urls import path
from core.views import upload_excel_file

app_name = 'core'

urlpatterns = [
    path('', upload_excel_file, name='upload-file'),
]
