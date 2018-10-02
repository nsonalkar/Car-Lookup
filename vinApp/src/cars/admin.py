from django.contrib import admin
from django import forms
from .models import Cars
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User, Group
import csv
from django.http import HttpResponse


admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
# class CsvImportForm(forms.Form):
#     csv_file = forms.FileField()
# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):
#
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]
#
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)
#
#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])
#
#         return response
#     export_as_csv.short_description = "Export Selected"
# class CarsResource(resources.ModelResource):
#     class Meta:
#         model = Cars
#         #import_id_fields = ('Vin Number',)
#
#         fields = ('id', 'vin', 'make', 'model', 'modelYear', 'engineCylinders', 'transmissionStyle', 'trim')
#         #list_display = ['vin', 'make', 'model', 'modelYear', 'engineCylinders', 'transmissionStyle', 'trim']

# class CarsAdmin(admin.ModelAdmin, ExportCsvMixin): #ImportExportModelAdmin
#     #resource_class = CarsResource
#     list_display = ['vin', 'make', 'model', 'modelYear', 'engineCylinders', 'transmissionStyle', 'trim']
#     actions = ["export_as_csv"]
#     change_list_template = "cars/cars_changelist.html"
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('import-csv/', self.import_csv)
#         ]
class CarsAdmin(ImportExportModelAdmin):
    list_display = ['__str__','vin', 'make', 'model', 'modelYear', 'engineCylinders', 'transmissionStyle', 'trim']
admin.site.register(Cars,CarsAdmin)
