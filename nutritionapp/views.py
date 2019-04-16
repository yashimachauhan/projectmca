from django.shortcuts import render,redirect
from userapp.models import UserInfo
import authorize as au

def nutritionindex(request):
    try:
        auth=au.authriseuser(request.session["authenticated"],request.session["roleid"],2)
    except:
        return redirect("/notlogin/")
    if(auth):
        return render(request,'nutritionindex.html')
    else:
        aut,message=auth
        if(message=="Wrong User"):
            return redirect("/wrong user/")
        elif(message=="Not Login"):
            return redirect("/notlogin/")



def nutritionlogin(request):
    if (request.method == "POST"):
        uemail = request.POST["email"]
        upassword = request.POST["password"]
        try:
            userdata = UserInfo.objects.get(user_email=uemail)
            dp = userdata.user_password
            if (dp == upassword):
                request.session['authenticated']=True
                request.session['roleid']=userdata.role_id_id
                request.session['useremail']=userdata.user_email
                if(request.session['roleid']==2):
                    return redirect("/product/productindex/")
                elif(request.session['roleid']==3):
                    return redirect("/fitness/fitnessindex/")
                elif(request.session['roleid']==4):
                    return redirect("/nutrition/nutritionindex/")
            else:
                return render(request,'nutritionlogin.html',{'inserted':True})
        except:
             return redirect("/" )
    return render(request,"nutritionlogin.html",)

def weightgain(request):
    return render(request,"weightgain.html")

def updateinfo(request):
    if request.method=="POST":
        getemail=request.session['useremail']
        data=UserInfo.objects.get(user_email=getemail)
        old=data.user_password
        getold=request.POST["old"]
        new=request.POST["new"]
        confirm=request.POST["confirm"]
        if getold==old:
            if new==confirm:

                update=UserInfo(user_email=getemail,user_password=confirm )
                update.save(update_fields=['user_password'])
                return redirect("/logout/")
    return render(request,"updateinfo.html")