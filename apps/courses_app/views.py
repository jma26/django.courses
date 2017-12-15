# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context) 

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')

    Course.objects.create(name = request.POST['name'], desc= request.POST['description'])
    return redirect('/')

def confirm(request, id):
    context = {
        'course': Course.objects.get(id = id)
    }
    return render(request, 'courses_app/validation.html', context)

def remove(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')
