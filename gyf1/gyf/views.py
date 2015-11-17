# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import *
from django.contrib.auth import forms
from django.template import RequestContext,Context
from django.contrib.auth.forms import UserCreationForm
from django.db import connection,transaction 
import MySQLdb
def main(request):
    cursor = connection.cursor()
    cursor.execute('select * from Books')
    books = cursor.fetchall()
    cursor.close()
    return render_to_response("main.html",{"books":books})
def searching_result(request):
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        cursor = connection.cursor()
        cursor.execute('select * from Books left join Authors on Books.AuthorID=Authors.AuthorID where Authors.Name = \''+name+'\'')
        hul = cursor.fetchall()
        transaction.commit_unless_managed()
        cursor.close()
        return render_to_response("searching_result.html",{"books":hul})
    else:
        return render_to_response("searching_result.html")
def delete(request):
    if 'name' in request.GET and request.GET['name']:
        isbn = request.GET['name']
        cursor = connection.cursor()
        cursor.execute('delete from Books where Books.ISBN=\''+isbn+'\'')
        transaction.commit_unless_managed()
        cursor.execute('select * from Books')
        books = cursor.fetchall()
        cursor.close()
        return render_to_response("delete.html",{"books":books})
    else:
        return render_to_response("delete.html")
def message(request):
    if 'name' in request.GET and request.GET['name'] and 'a' in request.GET and request.GET['a']:
        authorid = request.GET['name']
        title = request.GET['a']
        cursor = connection.cursor()
        cursor.execute('select * from Books where Books.Title=\''+title+'\'')
        books = cursor.fetchall()
        cursor.execute('select * from Authors where Authors.AuthorID=\''+authorid+'\'')
        hul = cursor.fetchall()
        cursor.close()
        dic = {"books":books,"authors":hul}
        return render_to_response("message.html",dic)
    else:
        return render_to_response("message.html")
def add_author(request):
    if 'name1' in request.GET and request.GET['name1'] and 'authorid' in request.GET and request.GET['authorid'] and 'age' in request.GET and request.GET['age'] and 'country' in request.GET and request.GET['country']:
        name = request.GET['name1']
        authorid = request.GET['authorid']
        age = request.GET['age']
        country = request.GET['country']
        cursor = connection.cursor()
        cursor.execute('select * from Books')
        key = 1
        huls = cursor.fetchall()
        for hul in huls:
            if authorid == hul[1]:
                key = 0
        if key == 1:
            cursor.execute('insert into Authors(Name,AuthorID,Age,Country) values (\''+name+'\',\''+authorid+'\',\''+age+'\',\''+country+'\')')
            transaction.commit_unless_managed()
            cursor.execute('select * from Authors')      
            authors = cursor.fetchall()
            cursor.close()
            return render_to_response("add_author.html",{"authors":authors})
        else:
            return render_to_response("error.html")
    else:
        cursor = connection.cursor()
        cursor.execute('select * from Authors')
        authors = cursor.fetchall()
        cursor.close()
        return render_to_response("add_author.html",{"authors":authors})
def add_book(request):
    if 'isbn' in request.GET and request.GET['isbn'] and 'title' in request.GET and request.GET['title'] and 'authorid' in request.GET and request.GET['authorid'] and 'publisher' in request.GET and request.GET['publisher'] and 'publishdate' in request.GET and request.GET['publishdate'] and 'price' in request.GET and request.GET['price']:
        isbn = request.GET['isbn']
        title = request.GET['title']
        authorid = request.GET['authorid']
        publisher = request.GET['publisher']
        publishdate = request.GET['publishdate']
        price = request.GET['price']
        key = 1
        cursor = connection.cursor()
        cursor.execute('select * from Books')      
        huls = cursor.fetchall()
        for hul in huls:
            if isbn == hul[0]:
                key = 0
        if key == 1:
            cursor.execute('insert into Books(ISBN,Title,AuthorID,Publisher,Publishdate,Price) values (\''+isbn+'\',\''+title+'\',\''+authorid+'\',\''+publisher+'\',\''+publishdate+'\',\''+price+'\')')
            transaction.commit_unless_managed()
            cursor.execute('select * from Books')      
            books = cursor.fetchall()
            cursor.close()
            return render_to_response("add_book.html",{"books":books})
        else:
            return render_to_response("error.html")
    else:
        cursor = connection.cursor()
        cursor.execute('select * from Books')
        books = cursor.fetchall()
        cursor.close()
        return render_to_response("add_book.html",{"books":books})
def edit_book(request):
    if 'isbn' in request.GET and request.GET['isbn'] and 'title' in request.GET and request.GET['title'] and 'authorid' in request.GET and request.GET['authorid'] and 'publisher' in request.GET and request.GET['publisher'] and 'publishdate' in request.GET and request.GET['publishdate'] and 'price' in request.GET and request.GET['price']:
        isbn = request.GET['isbn']
        title = request.GET['title']
        authorid = request.GET['authorid']
        publisher = request.GET['publisher']
        publishdate = request.GET['publishdate']
        price = request.GET['price']
        cursor = connection.cursor()
        cursor.execute('update Books set ISBN=\''+isbn+'\',Title=\''+title+'\',AuthorID=\''+authorid+'\',Publisher=\''+publisher+'\',PublishDate=\''+publishdate+'\',Price=\''+price+'\' where ISBN = \''+isbn+'\'')
        transaction.commit_unless_managed()
        cursor.execute('select * from Books')      
        books = cursor.fetchall()
        cursor.close()
        return render_to_response("add_book.html",{"books":books})
    else:
        cursor = connection.cursor()
        cursor.execute('select * from Books')
        books = cursor.fetchall()
        cursor.close()
        return render_to_response("add_book.html",{"books":books})