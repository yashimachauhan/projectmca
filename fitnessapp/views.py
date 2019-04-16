from django.shortcuts import render,redirect
from userapp.models import  UserInfo
import authorize as au
# Create your views here.
def fitnessindex(request):
    try:
        auth=au.authriseuser(request.session["authenticated"],request.session["roleid"],3)
    except:
        return redirect("/notlogin/")
    if(auth):
        return render(request,'fitnessindex.html')
    else:
        aut,message=auth
        if(message=="Wrong User"):
            return redirect("/wrong user/")
        elif(message=="Not Login"):
            return redirect("/notlogin/")
def fitgain(request):
    return render(request,"fitgain.html")

def fitloss(request):
    return render(request,"fitloss.html")
