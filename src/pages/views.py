from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def spreadingnumber(request):
    return render(request,"spreading_number.html",{})

def email(request):
	subject = 'Testing'
	message = 'Hello, This mail is sent by your friend.'
	sender  = 'pranjal0819@gmail.com'
	recever = ['pranjal0819@gmail.com','pranjal.16bcs1112@abes.ac.in','nikhilarora1812@gmail.com']
	send_mail(subject,message,sender,recever,fail_silently=False)
	return redirect("home")
