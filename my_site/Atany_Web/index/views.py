from django.shortcuts import render
from django.http import HttpResponse

def fun1(request):
    return HttpResponse("in fun1")

def fun2(request):
	return HttpResponse("in fun2")

def fun(request):
	return HttpResponse("in fun")

def funFrom(request):
	return HttpResponse("in funFrom")

