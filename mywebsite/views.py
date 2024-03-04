from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
import os 
#dir_path = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
photo_path = os.path.join(dir_path, "mywebsite")
photo_path = os.path.join(photo_path, "static")
photo_path = os.path.join(photo_path, "images")
photo_path = os.path.join(photo_path, "photography")
print(dir_path)

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def powerlift(request):
    return render(request, 'powerlift.html', {})

def photography(request):
    image_list = []
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        files.sort()
        for file in files:
            image_list.append("/images/photography/" + str(file))
            #image_list.append("/images/photography/" + files)
        print(image_list)
    return render(request, 'photography.html', {'images': image_list})

def contact(request):
    return render(request, 'contact.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
