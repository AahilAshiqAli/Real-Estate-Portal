from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from polls.models import Contact,EliteEstateRoyce
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from email_validator import validate_email,EmailNotValidError




def is_valid_email(email):
    try:
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
        return True
    except EmailNotValidError as e:
        # Email is not valid, exception message is human-readable
        return False








#..................................................................................................................

    
    
    
    
    
    
# Create your views here.
def index(request):
    query = EliteEstateRoyce.objects.raw('SELECT * FROM elite_estate_royce limit 9')
    q = {'data' : query}
    if request.user.is_anonymous:
        q['user'] = False
    else:
        q['user'] = True
        q['username'] = request.user.username
   
    return render(request,'index.html',q)







#..................................................................................................................






def loginUser(request):
    if request.method == 'GET':
        if 'login' in request.GET:
            return render(request,'login.html',{'q' : True})
        elif 'request' in request.GET:
            return render(request,'login.html',{'q' : False})
        else:
            return render(request,'login.html')
    
    elif request.method == 'POST':

        if 'confirm password' in request.POST:
            username = request.POST['username']
            email = request.POST['login']  # Assuming this is intended to be the email.
            password = request.POST['password']
            confirm_password = request.POST['confirm password']
            
            # Simple validation example
            if password == confirm_password and is_valid_email(email):
                # Create the user and log them in, etc.
                user = User.objects.create_user(username, email, password)
                user.save()
                
            else:
                # make error that user exists
                if is_valid_email(email):
                    return HttpResponse('Invalid email credentials')
                
                else:
                    return HttpResponse('Passwords dont match')
        else:
            # check if user is logged in    
            email = request.POST.get('email')
            password = request.POST.get('password')
            
        user = authenticate(email=email, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            print(user)
            return render(request,'login.html')





#..................................................................................................................








def logoutUser(request):
    logout(request)
    return redirect('/login')












#..................................................................................................................







def housing(request):
    q = {}
    if request.user.is_anonymous:
        q['user'] = False
    else:
        q['user'] = True
        q['username'] = request.user.username
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
        
    q['query'] = query 
    return render(request,'housing.html',q)







#..................................................................................................................






def details(request,house_id):
    q = {}
    if request.user.is_anonymous:
        redirect('/login')
    q['username'] = request.user.username
    query = EliteEstateRoyce.objects.raw('select * from elite_estate_royce where id = '+str(house_id) + ' limit 1')
    q['query'] = query
    return render(request,'details.html',q)
#.....................................................................................................................








def commercial(request):
    return render(request,'commercial.html')









#..................................................................................................................










def upload(request):
    q={}
    if request.user.is_anonymous:
        redirect("/login")
    else:
        q['user'] = True
        q['username'] = request.user.username
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
        
    return render(request,'upload.html',q)







#..................................................................................................................







def contact(request):
    # if post request aarahi hai tau database mei store kardo
    q = {}
    if request.user.is_anonymous:
        q['user'] = False
    else:
        q['user'] = True
        q['username'] = request.user.username
    return render(request,'contact.html',q)

