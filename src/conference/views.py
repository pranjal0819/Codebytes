from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages, auth
from .forms import authorRecordForm, paperRecordForm, reviewPaperForm
from .models import paperRecord, authorRecord, reviewPaper

# Create your views here.
class welcome(TemplateView):
    template_name = 'welcome.html'

    def get(self, request):
        return render(request, self.template_name, {})

class view_all_paper(TemplateView):
	template_name = 'view_all_paper.html'

	def get(self, request):
		if request.user.is_staff:
			list = paperRecord.objects.all().order_by('id')
			if not list:
				messages.error(request,"Paper is not submited yet")
		else:
			list = paperRecord.objects.filter(user=request.user)
			if not list:
				messages.error(request,"You have not submited any paper")
		return render(request, self.template_name, {'paperlist':list})

class select_user(TemplateView):
	template_name = 'userlist.html'

	def get(self, request, pk):
		try:
			if request.user.is_staff:
				paper    = paperRecord.objects.get(pk=pk)
				userlist = auth.models.User.objects.exclude(username=paper.author).filter(is_superuser=False)
				list1 = []
				list2 = []
				for user in userlist:
					try:
						reviewPaper.objects.get(user=user, paper=paper)
						list1.append(user)
					except:
						list2.append(user)
				return render(request, self.template_name, {'userlist':userlist,'paper':paper, 'list1':list1,'list2':list2})
			else:
				messages.error(request,"Lot of Error")
				redirect("conference:welcome")
		except:
			messages.error(request,"Lot of error")
			redirect("conference:view_all_paper")

class selected_user(TemplateView):

	def get(self, request, paper_pk, user_pk):
		if request.user.is_staff:
			try:
				user = auth.models.User.objects.get(pk=user_pk)
				paper = paperRecord.objects.get(pk=paper_pk)
				print(user_pk, paper_pk)
				try:
					reviewPaper.objects.get(user=user ,paper=paper)
					messages.error(request,"Already Assign this user")
				except:
					instance = reviewPaper.objects.create(user=user, paper=paper, overallEvaluation='', remark='', point=0)
					instance.save()
					messages.success(request,"successfuly record save")
			except:
				messages.error(request,"Please Try again")
			return redirect("conference:view_all_paper")
		else:
			messages.error(request,"You are not a Chair Person")
			return redirect("conference:welcome")

class view_detail(TemplateView):
	template_name = 'detail.html'

	def get(self, request, pk):
		try:
			if request.user.is_staff:
				obj = paperRecord.objects.get(pk=pk)
			else:
				obj = paperRecord.objects.get(user=request.user, pk=pk)
			list = obj.author.all()
		except:
			obj = None
			list = None
			messages.error(request,"Lot of Error")
			return redirect("conference:welcome")
		return render(request, self.template_name, {'record':obj, 'authorlist':list})

class submit_paper(TemplateView):
	template_name = 'submit_paper.html'

	def get(self, request):
		authorform  = authorRecordForm()
		paperform   = paperRecordForm()
		attr = {'authorform':authorform,
				'paperform':paperform}
		return render(request, self.template_name, attr)

	def post(self, request):
		paperform  = paperRecordForm(request.POST,request.FILES)
		if paperform.is_valid():
			temp = paperform.save(commit=False)
			temp.status = False
			temp.user = request.user
			temp.save()
			try:
				for i in range(1,10,1):
					j=str(i)
					nam = request.POST['name'+j]
					eml = request.POST['email'+j]
					mob = request.POST['mobile'+j]
					cou = request.POST['country'+j]
					org = request.POST['org'+j]
					url = request.POST['url'+j]
					if nam is not "":
						obj = authorRecord.objects.create(name=nam,email=eml,mobileNumber=mob,country=cou,organization=org,webpage=url)
						temp.author.add(obj.id)
			except:
				pass
			messages.success(request,"Paper submited successfuly")
			return redirect("conference:submit_paper")
		else:
			messages.error(request,"Lot of Error")
			return redirect("conference:welcome")
		return render(request, self.template_name, {'paperform':None})

class delete_paper(TemplateView):

	def get(self, request, pk):
		try:
			if request.user.is_staff:
				obj = paperRecord.objects.get(pk=pk)
			else:
				obj = paperRecord.objects.get(user=request.user, pk=pk)
			list = obj.author.all()
			for l in list:
				l.delete()
			obj.delete()
			messages.success(request,"Paper deleted")
		except:
			messages.error(request,"Lot of error")
			return redirect("conference:welcome")
		return redirect("conference:view_all_paper")