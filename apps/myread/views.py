from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

from . import models
from apps.reader.models import Reader
from apps.book.models import Book


# Create your views here.
def home_page(request):
    # View can return valid formats like
    # html , xml ,json ,etc
    book_per_cat_cnt = Book.objects.values('category').annotate(cnt=Count('*'))
    engaged_reader_count = models.MyRead.objects.distinct('reader_username').count()
    total_reader_cnt = Reader.objects.count()
    context = {
        'total_reader_cnt':total_reader_cnt,
        'engaged_reader_count':engaged_reader_count,
        'book_per_cat_cnt':book_per_cat_cnt
    }
  
     
    #Return the response
    return render(request, 'home_page.html',context)
class HomePage (TemplateView):
    #specify the template to display
    template_name = 'home_page.html'

    