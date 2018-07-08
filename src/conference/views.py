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
    if request.user.is_staff:
        record = paperRecord.objects.all().order_by('-timestamp') 
        if not record:
            messages.error(request,"No one submit any paper")
    else:
        record = list(paperRecord.objects.filter(author=request.user.id)).order_by('-timestamp')
        if not record:
            messages.error(request,"You have not submit any paper")
    return render(request,'view_paper.html',{'record':record})

@login_required(login_url='/login')
def view_detail(request, pk):
    detail = paperRecord.objects.get(pk=pk)
    return render(request,'detail.html',{'r':detail})

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

