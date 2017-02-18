from django.shortcuts import render
from django.http import HttpResponse

import json
from main.models import User,UserTransaction,UserTask,DailyLog,Device


# Create your views here.



def dashboard(request):
	LoginId = request.GET.get('LoginId')
	return render(request,'main/examples/dashboard.html')

def table(request):
	return render(request,'main/examples/table.html')

def notifications(request):
	return render(request,'main/examples/notifications.html')

def typography(request):
	return render(request,'main/examples/typography.html')

def start(request):
	return render(request,'main/upload.html')

