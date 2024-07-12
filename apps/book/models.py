from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.core.models import CreatedModifiedAbstract
from apps.core.constants import BOOK_CATEGORY

# Create your models here

class BookManager(models.Manager):
    #self = Book.objects
    def get_books_by_tags(self,*tag):
        return self.filter(tag__name__in = tag)
class Tag(models.Model):
    name = models.CharField(max_length=100, unique = True)

    def __str__(self) -> str : 
        return f"{self.name}"
    
class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural = 'Books and Authors'

class BookAuthor(models.Model):
    BOOK_AUTHOR_ROLE = {
        "co_author": "Co_Author",
        "editor": "Editor",
        "author": "Author",
    }
    book = models.ForeignKey("book.Book", on_delete=models.CASCADE)
    author = models.ForeignKey("book.Author", on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=BOOK_AUTHOR_ROLE, default="author")

    def __str__(self) -> str:
        return f"{self.author} {self.role} {self.book}"


class Book(CreatedModifiedAbstract):

    BOOK_FORMAT = {"eb": "ebook", "hc": "hardcover"}
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page_count = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=2, choices=BOOK_CATEGORY, default="pr")
    published_date = models.IntegerField()
    publisher = models.CharField(max_length=50)
    # authors = ArrayField(ArrayField(models.CharField(max_length=50)))
    tag = models.ManyToManyField("book.Tag")
    authors = models.ManyToManyField(
        "book.Author",
        related_name="book",
        through="book.BookAuthor",
    )
    language = models.CharField(max_length=50)
    edition = models.SmallIntegerField(null=True, blank=True)
    book_format = models.CharField(max_length=2, choices=BOOK_FORMAT, default="eb")
    objects = BookManager()
    #@classmethod
    #def get_books_by_tags(cls,*tag):
      #  return cls.objects.filter(tag__name__in=tag)
    @property
    def short_des(self):
        
        return f'{self.short_des[:30]}'

    def __str__(self) -> str:
        return f"{self.title} {self.isbn} "
    class Meta:
        ordering = ('-title',)
        default_related_name = '%(app_label)s_%(model_name)s'