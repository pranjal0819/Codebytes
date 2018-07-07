from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import submitPaper
from .models import paperRecord

# Create your views here.
@login_required(login_url='/login')
def welcome(request):
    return render(request, 'welcome.html', {})

@login_required(login_url='/login')
def view_paper(request):
    if request.user.id in [1,6]:
        record = paperRecord.objects.all()
        if not record:
            messages.error(request,"No one submit any paper")
    else:
        record = paperRecord.objects.filter(author=request.user.id)
        if not record:
            messages.error(request,"You have not submit any paper")
    return render(request,'view_paper.html',{'record':record})

@login_required(login_url='/login')
def submit_paper(request):
    if request.method == 'POST':
        record = submitPaper(request.POST,request.FILES)
        if record.is_valid():
            temp=record.save(commit=False)
            temp.author = request.user
            temp.save()
            return HttpResponseRedirect('/welcome')
    else:
        record = submitPaper()
    return render(request, 'submit_paper.html',{'record':record})

