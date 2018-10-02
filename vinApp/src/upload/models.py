#from __future__ import unicode_literals
from django.db import models
import random
import os
from django.db import models
#from .admin import UploadAdmin
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
import pandas as pd

# def get_filename_ext(filepath):
# 	base_name = os.path.basename(filepath)
# 	name, ext = os.path.splitext(base_name)
# 	return name, ext
#
# def upload_file_path(instance, filename):
# 	new_filename = random.randint(1, 3910209312)
# 	name, ext = get_filename_ext(filename)
# 	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#
# 	return "upload/{new_filename}/ {final_filename}".format(new_filename=new_filename, final_filename=final_filename)

#
# class Upload(models.Model):
# 	#file = models.FileField(upload_to='upload_file_path', null=True, blank=True)
# 	file = models.FileField()
# 	print(file.name)
#
# 	def __str__(self):
# 		return os.path.basename(self.file.name)
#
# 	def save(self, *args, **kwargs):
# 		super(Upload, self).save(*args, **kwargs)
# 		filename = self.file.url
#
import csv
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
import io
#from .signals import csv_uploaded
#from .validators import csv_file_validator
import request
#from .forms import UploadFileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# def target_model(self):
#     file = open(self, "r")
#     next(file)
#     vin = file.read().splitlines()
#     print(vin)
# class UploadManager(models.Manager):
#     def order(self, file):
#         print()

# def upload_csv_file(instance, filename):
#     qs = instance.__class__.objects.filter(user=instance.user)
#     if qs.exists():
#         num_ = qs.last().id + 1
#     else:
#         num_ = 1
#     return f'csv/{num_}/{instance.user.username}/{filename}'
# def upload_csv(instance,filename):
#     qs = instance.__class__.objects
#
class Upload(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    file = models.FileField()
    #completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    # def target_model(self):
    #     files = open(self.file, "r")
    #     next(files)
    #     vin = files.read().splitlines()
    # def save(self, *args, **kwargs):
    #     #filename = self.file.url
    #     #print(filename)


# def convert_header(csvHeader):
#     header_ = csvHeader[0]
#     # cols = [x.replace(' ', '_').lower() for x in header_.split(",")]
#     return header_


def pre_save_upload(sender,instance, *args,**kwargs):
    print("hi")
    qs = instance.__class__.objects
    print(qs)
    #print(instance.file.save())

pre_save.connect(pre_save_upload, sender=Upload)
def post_save_upload(sender,instance, created, *args,**kwargs):
    print("Hello")
    # if not instance.completed:
    #     csv_file = instance.file
    #     decoded_file = csv_file.read().decode('utf-8')
    #     io_string = io.StringIO(decoded_file)
    #     reader = csv.reader(io_string, delimiter=';', quotechar='|')
    #     header_ = next(reader)
    #     header_cols = convert_header(header_)
    #     parsed_items = []
    #     for line in reader:
    #         parsed_row_data = {}
    #         i = 0
    #         row_item = line[0].split(',')
    #         for item in row_item:
    #             print(item)
    #             key = header_cols[i]
    #             parsed_row_data[key] = item
    #             i += 1
    #         parsed_items.append(parsed_row_data)
    #     csv_uploaded.send(sender=instance, user=instance.user, csv_file_list=parsed_items)
    #     instance.completed = True
    #     instance.save()
    #     print(instance)
post_save.connect(post_save_upload, sender=Upload)