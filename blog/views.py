from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title':  'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '2019-08-27'
    },
    {
        'author': 'JaneDoe',
        'title':  'Blog Post 2',
        'content': '2nd Post Content',
        'date_posted': '2019-28-27'
    }
    
]

def home(request):
    context = {
        'posts': posts
        }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})    
