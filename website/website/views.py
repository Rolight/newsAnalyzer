from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from website.tools import conv_str
from website.gdata import get_data

import datetime
import os.path

def get_time_span(request, begin_time, end_time, top_n):
    try:
        top_n = int(top_n)
    except ValueError:
        raise Http404()
    gdata = get_data(begin_time, end_time, top_n)
    return render_to_response('time_span.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def demo_html(request):
    return render_to_response('demo.html');
