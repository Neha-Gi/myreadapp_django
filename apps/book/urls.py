from django.urls import path
from .import views 
app_name = 'book-urls'
urlpatterns = [
    path('book/<isbn>' , views.book_detail,name = 'book_detail'),
   # path('book/<tag>',views.book_tag,name = 'book_tag')
]