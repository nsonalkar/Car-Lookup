from django import forms

from django.contrib.auth import get_user_model

# class ExcelForm(forms.Form):
#     files = forms.FileField(label= "Choose excel to upload")
from django import forms
import request
import csv
from .models import Upload
# from .models import Upload
# class UploadFileForm(forms.Form):
#     #title = forms.CharField(max_length=50)
#     file  = forms.FileField()

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Upload
# class UploadFileForm(forms.ModelForm):
#     csv_file = forms.FileField()
#
#     def save(self, *args, **kwargs):
#         # form_input = UploadFileForm()
#         # self.place = self.cleaned_data['file']
#         # file_csv = request.FILES['csv_file']
#         # datafile = open(file_csv, 'rb')
#         # records = csv.reader(datafile)
#         records = csv.reader(self.cleaned_data["csv_file"])
#         for line in records:
#             input_data = Upload()
#             #input_data.file = self.cleaned_data["file"]
#             input_data.save()
