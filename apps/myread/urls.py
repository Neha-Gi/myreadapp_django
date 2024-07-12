#We need the path
from django.urls import path
from . import views

# Django recogniyes path urls when there  are 
# define in the variable 'urlpatterns'.

app_name ='myread-urls'

urlpatterns =[
    path('',views.home_page,name='home-page')
]
