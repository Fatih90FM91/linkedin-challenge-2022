from django.shortcuts import render
from django.views.generic import ListView,DetailView ,CreateView ,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

# def HomeView(request):
#     return render(request , 'home.html' ,{})


class HomeView(ListView):
    model = Post
    template_name='home.html'
   

class ArticleDetail(DetailView):
    model = Post
    template_name='article_detail.html'


class CreateJobView(CreateView):
    model = Post
    template_name='member_job.html'
    fields ='__all__'
    success_url = reverse_lazy('home')

