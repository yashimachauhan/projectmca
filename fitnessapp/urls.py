from django.conf.urls import url
from fitnessapp import views

app_name="fitnessapp"
urlpatterns=[
url(r'^fitnessindex',views.fitnessindex,name="fitnessindex"),
]