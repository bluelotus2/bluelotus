# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from gyf.models import Books,Authors,User
from django.contrib.auth import forms
from django.template import RequestContext,Context
from django.contrib.auth.forms import UserCreationForm

#def hello(request):
#    #html="main.html"
#    return render_to_response("main.html")
#
#def Delete(request):
##    delete_id = request.GET["id"]
##    Books.objects.filter(id = delete_id).delete()
#    return render_to_response("delete.html")
#
#def Search(request):
##    delete_id = request.GET["id"]
##    Books.objects.filter(id = delete_id).delete()
#    return render_to_response("search.html")
def main(request):

    return render_to_response("main.html")
def book_list(request):  
    if request.GET['a'] and 'a' in request.GET:
        a = request.GET['a']
    if request.GET['b'] and 'b' in request.GET:
        b = request.GET['b']
    if request.GET['c'] and 'c' in request.GET:
        c = request.GET['c']
    if request.GET['d'] and 'd' in request.GET:
        d = request.GET['d']
    if request.GET['e'] and 'e' in request.GET:
        e = request.GET['e']
    if request.GET['f'] and 'f' in request.GET:
        f = request.GET['f']
    book = Books(ISBN=a,Title=b,AuthorID=c,Publisher=d,PublishDate=e,Price=f) 
    book.save()     
    return render_to_response("book_showing.html")