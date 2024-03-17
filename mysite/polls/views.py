from django.shortcuts import render
from datetime import datetime
from polls.models import Contact,EliteEstateRoyce
from django.contrib import messages

# Create your views here.
def index(request):
    query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce limit 9')
    return render(request,'index.html',{'data' : query})

def housing(request):
    if request.method == "POST":
        city = request.POST.get('city')
        bedroom = request.POST.get('bedroom')
        bath = request.POST.get('bath')

         
    query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce where bedrooms = 2 and baths = 2 and city = \'Lahore\'')
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

