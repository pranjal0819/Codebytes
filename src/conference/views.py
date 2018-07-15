from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import submitPaperForm, reviewPaperForm
from .models import paperRecord, commentOnPaper

# Create your views here.
@login_required(login_url="account:login")
def welcome(request):
    record = commentOnPaper.objects.filter(commentuser=request.user)
    recordList=[]
    if not record:
        messages.error(request,"No paper to review")
    for r in record:
        list=paperRecord.objects.filter(pk=int('0'+r.paper))
        recordList.append(list[0])
    return render(request, 'welcome.html', {'record':recordList})

@login_required(login_url="account:login")
def review_paper(request,pk):
    try:
        view = commentOnPaper.objects.get(commentuser=request.user, pk=pk)
        paper = paperRecord.objects.get(pk=pk)
        if request.method == 'POST':
            review = reviewPaperForm(request.POST)
            if review.is_valid():
                view.comment = review.cleaned_data['comment']
                view.save(update_fields=['comment'])
                return redirect("conference:welcome")
        else:
            review = reviewPaperForm()
    except:
        messages.error(request,"There is no paper")
        paper = None
        review = None
        view =None
    return render(request,'review_paper.html',{'paper':paper, 'viewComment':viewComment, 'c':review})

@login_required(login_url="account:login")
def view_paper(request):
    if request.user.is_staff:
        record = paperRecord.objects.all().order_by('-timestamp') 
        if not record:
            messages.error(request,"No one submit any paper")
    else:
        record = paperRecord.objects.filter(author=request.user.id).order_by('-timestamp')
        if not record:
            messages.error(request,"You have not submit any paper")
    return render(request,'view_paper.html',{'record':record})

@login_required(login_url="account:login")
def view_detail(request, pk):
    try:
        if request.user.is_staff:
            detail = paperRecord.objects.get(pk=pk)
        else:
            detail = paperRecord.objects.get(author=request.user.id,pk=pk)
    except:
        messages.error(request,"There is no paper")
        detail = None
    return render(request,'detail.html',{'r':detail})

@login_required(login_url="account:login")
def delete_paper(request, pk):
    intance = paperRecord.objects.get(author=request.user.id,pk=pk)
    intance.delete()
    return redirect("conference:view_paper")

@login_required(login_url="account:login")
def submit_paper(request):
    if request.method == 'POST':
        record = submitPaperForm(request.POST,request.FILES)
        if record.is_valid():
            temp=record.save(commit=False)
            temp.author = request.user
            temp.save()
            messages.success(request,"Paper submited successfuly")
            return redirect("conference:submit_paper")
    else:
        record = submitPaperForm()
    return render(request, 'submit_paper.html',{'record':record})

