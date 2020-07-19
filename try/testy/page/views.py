from django.http import HttpResponse
from django.shortcuts import render,redirect
from page.forms import pageForm
from page.models import page
from django.http import *
def login_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		return render(request,"login.html",{})
def signup_view(request,*args, **kwargs):
		print(args, kwargs)
		print(request.user )
		return render(request,"signup.html",{})	


def viewdetail(request):
	if request.method == "POST":
		form = pageForm(request.POST,request.FILES)
		if form.is_valid():
			try:
				form.save()
				form = pageForm()
				#return redirect()
			except:
				pass
	else:
		form = pageForm()	
	return render(request,"page.html",{'form':form})
def show(request):
	obj = page.objects.all()
	context = {
			'object':obj
	}
	return render(request,"show.html",{'obj':obj})
