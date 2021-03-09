from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from suphome.models import SignUpModel
import sqlite3



def home(request):
	return render(request, 'home.html', {})

def login(request):
	if request.method != 'POST':
		return render(request, 'login.html', {})
	else:
		
		login_name = request.POST.get("login_name")
		login_pass = request.POST.get("login_pass")
		con = sqlite3.connect("C:/Users/Kaiden Thrailkill/Desktop/Environment/supbot/db.sqlite3")

		cur = con.cursor()
		
		for row in cur.execute('SELECT * FROM suphome_signupmodel;'):
			if login_name and login_pass in row:
				return HttpResponseRedirect(reverse("home"))
		print("damn")	
		con.close()
		return render(request, 'login.html', {})


def SignUp(request):

	return render(request, 'signup.html', {})


def SignUp_save(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("signup"))
	else:
		tag=request.POST.get("tag")
		email=request.POST.get("email")
		password=request.POST.get("psw")


		setup1=SignUpModel(tag=tag, email=email, password=password)
		setup1.save()
		return HttpResponseRedirect(reverse('login'))