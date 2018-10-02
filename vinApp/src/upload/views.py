from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
import csv
from urllib.request import urlopen
import logging
from django.shortcuts import render_to_response
# from .forms import UploadForm
#from .forms import UploadFileForm
from django.contrib.admin.views.decorators import staff_member_required

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/success/url')
#         else:
#             form = UploadFileForm()
#         return render(request, 'upload.html', {'form': form})

# @staff_member_required
# def imports(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             success = True
#             context = {"form": form, "success": success}
#             return render_to_response("imported.html", context,
#             context_instance=RequestContext(request))
#     else:
#         form = UploadFileForm()
#         context = {"form": form}
#         return render_to_response("imported.html", context,
#         context_instance=RequestContext(request))