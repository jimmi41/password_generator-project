from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def aboutUs(request):
    return render(request,'generator/aboutUs.html')

def home(request):
    return render(request,'generator/home.html')

def password(request):
    # here we are sending a dictionary
    
    characters=list('abcdefghijklmnopqrstuvwxyz')
    
    length=int(request.GET.get('length'))#here we are getting length from url
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    
    if request.GET.get('special'):
        characters.extend('!@~#$%^&*()_+<>?:"|\[}]{')
        
    
    if request.GET.get('digits'):
        characters.extend('0123456789')
    thepassword=''
    
    for x in range(length):
        thepassword+=random.choice(characters)
    
    return render(request,'generator/password.html',{'password':thepassword})