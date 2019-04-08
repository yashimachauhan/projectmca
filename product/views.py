from django.shortcuts import render,redirect
from userapp.models import UserInfo
import authorize as au

# Create your views here.
def productindex(request):
    try:
        auth=au.authriseuser(request.session["authenticated"],request.session["roleid"],4)
    except:
        return redirect("/notlogin/")
    if(auth):
        return render(request,'productindex.html')
    else:
        aut,message=auth
        if(message=="Wrong User"):
            return redirect("/wrong user/")
        elif(message=="Not Login"):
            return redirect("/notlogin/")


