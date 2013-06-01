from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
	"""Home Page"""
	return HttpResponseRedirect('/home/')

def home(request):
    """Presents the search page and displays session specific
    assets if a session is loaded."""
    return render(request, 'setup.html')