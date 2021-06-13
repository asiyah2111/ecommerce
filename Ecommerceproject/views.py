from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
def signup(request):
	if request.method=='POST':
		fn=request.POST['fname']
		ln=request.POST['lname']
		un=request.POST['uname']
		pwd=request.POST['pwd']
		em=request.POST['email']
		mob=request.POST['mob']
		addr=request.POST['address']
		type=request.POST['type']
		uobj=User(first_name=fn,last_name=ln,username=un,password=make_password(pwd),email=em)
		uobj.save()
		userpobj=UserProfile(user=uobj,usertype=type,mobile=mob,address=addr)
		userpobj.save()
	return render(request,"signup.html")
def login_call(request):
	if request.method=='POST':
		un=request.POST['uname']
		pwd=request.POST['pwd']
		user=authenticate(username=un,password=pwd)
		if user:
			login(request,user)
			profileObj=UserProfile.objects.get(user__username=request.user)
			if profileObj.usertype=='seller':
				return redirect('/seller/home/')
			elif profileObj.usertype=='buyer':
				return redirect('/buyer/home/')
			else:
				return HttpResponse("<h3>invalid user<h3>")

	return render(request,"login.html")
def logout_call(request):
	logout(request)
	return redirect('/login/')