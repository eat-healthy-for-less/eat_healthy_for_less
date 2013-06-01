from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
	"""Home Page"""
	return HttpResponseRedirect('/home/')

def home(request):
    """Presents the setup page for user input"""
    return render(request, 'setup.html')

def post_setup(request):
	"""TODO: save variables, perform lookup / algo
	to find the recipe results"""
	return results(request)

def results(request):
	"""Results Page"""
	return render(request, 'setup.html')
