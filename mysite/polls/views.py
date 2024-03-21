from django.shortcuts import render
from datetime import datetime
from polls.models import Contact,EliteEstateRoyce
from django.contrib import messages


# Create your views here.
def index(request):
    query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce limit 9')
    return render(request,'index.html',{'data' : query})


def login(request):
    if request.method == 'GET':
        if 'login' in request.GET:
            return render(request,'login.html',{'q' : True})
        elif 'login' in request.GET:
            return render(request,'login.html',{'q' : False})
        
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')

def housing(request):
    if request.method == "POST":
        city = request.POST.get('city')
        bedroom = request.POST.get('bedroom')
        bath = request.POST.get('bath')
        
        if bedroom.isdigit() and bath.isdigit(): 
            query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce where bedrooms = ' + bedroom + ' and baths = ' + bath + ' and city = \''+city+'\' limit 12')
        elif bath.isdigit(): 
            query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce where baths = ' + bath + ' and city = \''+city+'\' limit 12')
        elif bedroom.isdigit(): 
            query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce where bedrooms = ' + bedroom + ' and city = \''+city+'\' limit 12')
        else:
            query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce where city = \''+city+'\' limit 12')
            
    else:
        query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce limit 12')
        
    return render(request,'housing.html',{'query' : query})

def commercial(request):
    return render(request,'commercial.html')

def upload(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        link = request.FILES.get('link')
        price = request.POST.get('price')
        bedroom = request.POST.get('bedroom')
        bath = request.POST.get('bath')
        size = request.POST.get('size')
        
        contact = Contact(email = email, password = password, phone = phone, address = address, city = city, state = state, zipcode = zipcode, profile_picture = link, date = datetime.today())
        elite = EliteEstateRoyce(city = city, location = address, price = price, bedrooms =  bedroom, baths = bath, size = size)
        
        contact.save()
        elite.save()
        messages.success(request,'Property details uploaded')
        #messages.error(request,"You should check in some of the fields below") 
        
    return render(request,'upload.html')

def contact(request):
    # if post request aarahi hai tau database mei store kardo
    return render(request,'contact.html')

