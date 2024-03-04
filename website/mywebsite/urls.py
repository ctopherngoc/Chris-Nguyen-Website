from django.urls import path
from . import views
from . views import BlogView, ArticleDetailView
urlpatterns = [
    path('', views.home, name ='home' ),
    path('about', views.about, name ='about' ),
    path('powerlift', views.powerlift, name ='powerlift' ),
    path('photography', views.photography, name ='photography' ),
    path('contact', views.contact, name ='contact' ),
    path('blog', BlogView.as_view(), name ="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name ='article-detail'),
]
