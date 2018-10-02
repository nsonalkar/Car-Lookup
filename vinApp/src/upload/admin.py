from django.contrib import admin
from .models import Upload
#from .forms import UploadFileForm
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display = ['file']
    #form = UploadFileForm
admin.site.register(Upload,UploadAdmin)
