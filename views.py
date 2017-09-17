from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
from random import random
def index(request):
	
	data = {'attempt': '', 'randomword': ''}
	if request.method =="GET":
		attempt = 0
		data = {'attempt': attempt, 'randomword': ''}
	elif request.method == "POST":
		attempt = int(request.POST['attempt']) + 1
		randomword = get_random_string(length=15).upper
		data = {'attempt': attempt, 'randomword': randomword}
	return render(request, "randomword/index.html", data)
