from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
# Reader -> AbstractUser -> AbsractBaseUser -> models.> Model
class Reader(AbstractUser):
    READER_TITLE = {
        #key = will be stored in the database
        #value = will be stored in display
        "Mr":"Mr",
        "Mrs":"Mrs",
        "Ms":"Ms",
        "Dr":"Dr"
    }
    # if no explicit primary is defined, Django will generatean id for us.
    # class attributes will represent fields in out table
    #by default,django fields are'not null' 
    username=models.CharField(max_length=50, primary_key=True)
    #null = true set the null fileld when used on the terminal
    #blank = true set the null fiels when used on the dashboard
    title=models.CharField(max_length=5,null=True,blank=True,choices=READER_TITLE)
    # If you want to remove the default ,just set it to NONE
    # email = None
    class Meta:
        #Define some meta data,    including constraints
         constraints = [
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr','Mrs','Ms','Dr']) 
            )
         ] 
    def __str__(self) -> str:   
        return  f'{self.title} {self.username}'