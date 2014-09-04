from myportfolio import urls
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.conf import settings


def home(request):
	return render_to_response("index.html")

def function(request):
	return render_to_response("index1.html")