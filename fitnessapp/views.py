from django.shortcuts import render,redirect
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




