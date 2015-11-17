
from address.models import Address
from django.shortcuts import render_to_response   

def address(request):
    
    if request.method == 'POST':           
        address_list = Address.objects.all()  
        return render_to_response("address_list.html",{"address_list":address_list})

def delete(request):
    
    if request.method == 'GET':
        get = request.GET        
        Address.objects.filter(id = get['id']).delete()
        address_list = Address.objects.all()
        return render_to_response("all_people.html",{"address_list":address_list})
            
def edit(request):        
    
    if request.method == 'GET': 
        get = request.GET         
        name1 = Address.objects.get(id = get['id'])
        Address.objects.get(id = get['id']).delete()
        return render_to_response('people.html',{                              
                              'name':name1.name,
                              'number':name1.number,
                              'telephone':name1.telephone,
                              'Email':name1.Email,
                              'QQ':name1.QQ,
                              'address':name1.address,    
                              'birthday':name1.birthday,
    })

def search(request):
    
    errors = []    
    address_list = Address.objects.all()
    
    if request.method == 'GET' and "name" in request.GET:
        
        get = request.GET        
        if not get.get('name',''):
            print "not exsit"                       
        else:
            try :
                Address.objects.get(name = get.get('name'))               
                address_list = Address.objects.filter(name = request.GET.get('name'))            
                                
            except:                
                print "not exsit"
                            
    return render_to_response('address_list.html',{"address_list":address_list,
                             'errors':errors,                             
    })