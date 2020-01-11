from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
##Dummy data
posts = [
        {
            'author':'Mary',
            'title':'Blog post 1',
            'content':'First Blog post',
            'date_posted':'July 29 2018'
        },
        {
            
            'author':'David',
            'title':'Blog post 2',
            'content':'Second Blog post',
            'date_posted':'July 30 2018'

        }

    ]


def home(request):
    #return HttpResponse('<h1> Home Page </h1>')
    context = {'posts':Post.objects.all(),'title':'Django App'}
    return render(request,'blog/home.html',context)

def about(request):
    #return HttpResponse('<h1> About Page </h1>')
    return render(request,'blog/about.html')

    
