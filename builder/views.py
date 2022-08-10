from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Templates
from django.core.serializers import serialize
import json

def index(request):
    templates = Templates.objects.all()
    return render(request, 'templates.html', {"templates":templates})


def addTemplate(request):
    return render(request, 'index.html')


def saveTemplate(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        template = Templates.objects.create(name='untitled', html=html, css=css)
        template.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [template])))[0]})


def editTemplate(request, id):
    template = Templates.objects.get(pk=id)
    return render(request, 'index.html', {"template":template})


def editTemplateContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        template = Templates.objects.get(pk=id)
        template.html = html
        template.css = css
        template.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [template])))[0]})


def previewTemplate(request, id):
    template = Templates.objects.get(pk=id)
    return render(request, 'preview.html', {"template":template})