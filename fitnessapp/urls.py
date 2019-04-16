from django.conf.urls import url
from fitnessapp import views

app_name="fitnessapp"
urlpatterns=[
url(r'^fitnessindex',views.fitnessindex,name="fitnessindex"),
url(r'^fitgain',views.fitgain,name="fitgain"),
url(r'^fitloss',views.fitloss,name="fitloss"),

]