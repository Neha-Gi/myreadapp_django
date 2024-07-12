from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

from . import models,utils
from apps.reader.models import Reader
from apps.book.models import Book


# Create your views here.
def home_page(request):
    # View can return valid formats like
    # html , xml ,json ,etc
    book_per_cat_cnt = Book.objects.values('category').annotate(cnt=Count('*'))
    engaged_reader_count = models.MyRead.objects.distinct('reader_username').count()
    total_reader_cnt = Reader.objects.count()
    response =f"""  <html>
        <h1 style="color:red;">Welcome to MyRead App</h1>
        <p>{total_reader_cnt} reader(s) and counting!</p>
        <p>{engaged_reader_count} engaged reader(s) and counting!</p>
        
        <h2>Book count per categories</h2>
        <ul>{utils.generate_book_cat_list(book_per_cat_cnt)}</ul>
        </html>
        """
     
    #Return the response
    return HttpResponse(response)
class HomePage (TemplateView):
    #specify the template to display
    template_name = 'home_page.html'

    