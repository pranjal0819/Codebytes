from django.shortcuts import render

# Create your views here.
def spreadingnumber(request):
    return render(request,"spreading_number.html",{})
