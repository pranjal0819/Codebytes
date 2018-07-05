from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import submitPaper
from .models import paperRecord

# Create your views here.
@login_required(login_url='/login')
def welcome(request):
    return render(request, 'welcome.html', {})

@login_required(login_url='/login')
def view_paper(request):
    record = paperRecord.objects.get(author=request.user.id)
    return render(request,'view_paper.html',{'record':record})

@login_required(login_url='/login')
def submit_paper(request):
    if request.method == 'POST':
        record = submitPaper(request.POST,request.FILES)
        if record.is_valid():
            temp=record.save(commit=False)
            temp.author = request.user
            temp.save()
            return HttpResponseRedirect('/')
    else:
        record = submitPaper()
    return render(request, 'submit_paper.html',{'record':record})

