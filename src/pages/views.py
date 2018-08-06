from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail


# Create your views here.
class Email(TemplateView):

    def get(self, request):
        subject = 'Testing'
        message = 'Hello, This mail is sent by your friend.'
        sender = 'pranjal0819@gmail.com'
        recever = ['pranjal0819@gmail.com']
        print("pending")
        send_mail('subject','message','pranjal0819@gmail.com',['pranjal0819@gmail.com'],fail_silently=False)
        print("success")
        return render(request, 'index.html', {})
