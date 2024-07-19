from django.urls import path
from . import views
app_name = 'reader-urls' 

urlpatterns = [
     path('reader/login/',views.login_view, name='reader-login'),
     path('reader/profile',views.profile,name = 'reader-profile'),
     path('reader/logout/',views.logout_view,name='reader-logout')
]

