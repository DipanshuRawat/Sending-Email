from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    #send_mail('subjec',message,emailfrom,list of recepist)
    send_mail('Hello,prince this side','This is my first proiect using django',
    'lp979851@gmail.com',
    ['torolej727@dnitem.com'],fail_silently=False)
    return render( request,'firstproject/index.html')
