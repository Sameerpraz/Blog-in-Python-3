from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import FormPost, FormEdit
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    # to show newest post first 
    ordering=['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogs/article_view.html'
    


class AddPostView(CreateView):
    model = Post
    template_name = 'blogs/add_post.html'
    # if we want to take all field from the model(table ) =>  fields = '__all__'
    # if we want to use only selected fields then =>          fields=('title','body')
    form_class = FormPost



class PostUpdate(UpdateView):
    model = Post
    form_class = FormEdit
    # can also be done this way=>    fields = ['title','title_tag','body']
    template_name = 'blogs/updatepost.html'



class DeletePost(DeleteView):
    model = Post
    template_name = 'blogs/deletepost.html'
    # send 
    success_url = reverse_lazy('home')