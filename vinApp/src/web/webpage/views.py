from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import request

# Create your views here.
def webnovel(self):
	return render(request, "cool.html", {})