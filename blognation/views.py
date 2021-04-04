from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Data, Feedback
from django.utils import timezone
from .forms import Queryform, Feedbackform

# Create your views here.
def homeview(request):

	return render(request,"blognation/soham.html")

def samplesview(request):

	return render(request,"blognation/samples.html")

def blog_list(request):
		posts=Data.objects.all()

		return render(request,"blognation/Blog_list.html",{"posts":posts})
def indexview(request):

	return render(request,"blognation/index.html")

def customersview(request):
	if request.method == 'POST':
	       # create a form instance and populate it with data from the request:
	        form2 = Feedbackform(request.POST)
	        # check whether it's valid:
	        if form2.is_valid():
	        	form2.save()
	        	return HttpResponseRedirect('Soham')

    # if a GET (or any other method) we'll create a blank form 
	else:
		form2 = Feedbackform()
	return render(request,"blognation/customers.html",{'form2':form2})
def queryview(request):
	if request.method == 'POST':
	       # create a form instance and populate it with data from the request:
	        form = Queryform(request.POST)
	        # check whether it's valid:
	        if form.is_valid():
	        	form.save()
	        	return HttpResponseRedirect('Soham')

    # if a GET (or any other method) we'll create a blank form 
	else:
		form = Queryform()

	return render(request, 'blognation/query.html', {'form': form})

def Gameview(request):
	if request.method == 'POST':
	       # create a form instance and populate it with data from the request:
	        form = Queryform(request.POST)
	        # check whether it's valid:
	        if form.is_valid():
	        	form.save()
	        	return HttpResponseRedirect('Soham')

    # if a GET (or any other method) we'll create a blank form 
	else:
		form2 = Feedbackform()

	return render(request,"blognation/Game.html",{'form2': form2})

	




