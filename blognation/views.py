from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Data
from django.utils import timezone
from .forms import Queryform

# Create your views here.
def homeview(request):

	return render(request,"blognation/soham.html")

def blog_list(request):
		posts=Data.objects.all()

		return render(request,"blognation/Blog_list.html",{"posts":posts})
def indexview(request):

	return render(request,"blognation/index.html")

def customersview(request):

	return render(request,"blognation/customers.html")
def queryview(request):
	if request.method == 'POST':
	       # create a form instance and populate it with data from the request:
	        form = Queryform(request.POST)
	        # check whether it's valid:
	        if form.is_valid():
	            # process the data in form.cleaned_data as required
	            # ...
	            # redirect to a new URL:
	            return HttpResponseRedirect('/Soham/')

    # if a GET (or any other method) we'll create a blank form 
	else:
		form = Queryform()

	return render(request, 'blognation/query.html', {'form': form})

def gtaview(request):

	return render(request,"blognation/gta.html")

	




