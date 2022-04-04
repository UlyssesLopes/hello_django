from django.shortcuts import render, HttpResponse

def hello(request, nome):
    return HttpResponse('Hello World! {}'.format(nome))