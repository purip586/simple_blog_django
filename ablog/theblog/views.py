from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theblog.models import post
from .forms import PostForm


class home(ListView):
    model = post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
