from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages, auth
from .forms import submitPaperForm, reviewPaperForm
from .models import paperRecord, commentOnPaper

# Create your views here.
class welcome(TemplateView):
    template_name = 'welcome.html'

    def get(self, request):
        record = commentOnPaper.objects.filter(user=request.user)
        recordList=[]
        for r in record:
            list = paperRecord.objects.filter(pk=int('0'+r.paper))
            if list:
                recordList.append(list[0])
        return render(request, self.template_name, {'record':recordList})

class review_paper(TemplateView):
    template_name = 'review_paper.html'

    def get(self, request, pk):
        try:
            view = commentOnPaper.objects.get(user=request.user, paper=pk)
            paper = paperRecord.objects.get(pk=pk)
            review = reviewPaperForm()
        except:
            messages.error(request,"There is no paper")
            paper = None
            review = None
            view = None
        return render(request, self.template_name, {'paper':paper, 'viewComment':view, 'c':review})

    def post(self, request, pk):
        review = reviewPaperForm(request.POST)
        if review.is_valid():
            view = commentOnPaper.objects.get(user=request.user, paper=pk)
            view.comment = review.cleaned_data['comment']
            view.save(update_fields=['comment'])
            return redirect("conference:welcome")
        else:
            messages.error(request, "Refresh the page")
            paper = None
            review = None
            view = None
        return render(request, self.template_name, {'paper':paper, 'viewComment':view, 'c':review})

class view_paper(TemplateView):
    template_name = 'view_paper.html'

    def get(self, request):
        if request.user.is_staff:
            record = paperRecord.objects.all().order_by('-timestamp') 
            if not record:
                messages.error(request,"No one submit any paper")
        else:
            record = paperRecord.objects.filter(author=request.user.id).order_by('-timestamp')
            if not record:
                messages.error(request,"You have not submit any paper")
        return render(request, self.template_name, {'record':record})

class view_detail(TemplateView):
    template_name = 'detail.html'

    def get(self, request, pk):
        try:
            if request.user.is_staff:
                detail = paperRecord.objects.get(pk=pk)
                userrecord = auth.models.User.objects.exclude(username=detail.author).filter(is_staff=False)
            else:
                detail = paperRecord.objects.get(author=request.user.id,pk=pk)
                userrecord = None
            commentrecord = commentOnPaper.objects.filter(paper=pk)
        except:
            messages.error(request,"There is no paper")
            detail = None
            userrecord = None
            commentrecord = None
        return render(request, self.template_name, {'record':detail, 'userrecord':userrecord, 'commentrecord':commentrecord})

class select_user(TemplateView):

    def get(self, request, paper_pk, user_pk):
        if request.user.is_staff:
            try:
                user = auth.models.User.objects.get(id=user_pk)
                try:
                    commentOnPaper.objects.get(user=user ,paper=str(paper_pk))
                    messages.error(request,"Already Assign this user")
                except:
                    instance = commentOnPaper.objects.create(user=user, paper=str(paper_pk),comment="No Comment")
                    instance.save()
                    messages.success(request,"successfuly record save")
            except:
                messages.success(request,"Lot of error")
        return redirect("conference:view_detail",paper_pk)

class delete_paper(TemplateView):

    def get(self, request, pk):
        try:
            if request.user.is_staff:
                intance = paperRecord.objects.get(pk=pk)
            else:
                intance = paperRecord.objects.get(author=request.user.id, pk=pk)
            intance.delete()
        except:
            pass
        return redirect("conference:view_paper")

class submit_paper(TemplateView):
    template_name = 'submit_paper.html'

    def get(self, request):
        record = submitPaperForm()
        return render(request, self.template_name, {'record':record})

    def post(self, request):
        record = submitPaperForm(request.POST,request.FILES)
        if record.is_valid():
            temp=record.save(commit=False)
            temp.author = request.user
            temp.save()
            messages.success(request,"Paper submited successfuly")
            return redirect("conference:submit_paper")
        else:
            messages.error(request,"Try again")
        return render(request, self.template_name, {'record':record})