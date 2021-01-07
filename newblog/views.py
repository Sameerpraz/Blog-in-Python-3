from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Category, User
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

    def get_context_data(self,*args,**kwargs):
        cat_menus = Category.objects.all()
        context = super( HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menus"] = cat_menus
        return context


def CategoryView(request,pk):
    category_blogs = Post.objects.filter(blog_category_id=pk)
    category_name=Category.objects.filter(pk=pk)

    return render(request, 'blogs/category.html',{
        'cats': category_name,
        'category_blogs': category_blogs
        })






class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogs/article_view.html'

    def get_context_data(self,*args,**kwargs):
        cat_menus = Category.objects.all()
        context = super( ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menus"] = cat_menus
        return context
    


class AddPostView(CreateView):
    model = Post
    template_name = 'blogs/add_post.html'
    # if we want to take all field from the model(table ) =>  fields = '__all__'
    # if we want to use only selected fields then =>          fields=('title','body')
    form_class = FormPost

    def get_context_data(self,*args,**kwargs):
        cat_menus = Category.objects.all()
        context = super( AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menus"] = cat_menus
        return context



class PostUpdate(UpdateView):
    model = Post
    form_class = FormEdit
    # can also be done this way=>    fields = ['title','title_tag','body']
    template_name = 'blogs/updatepost.html'

    def get_context_data(self,*args,**kwargs):
        cat_menus = Category.objects.all()
        context = super(PostUpdate , self).get_context_data(*args, **kwargs)
        context["cat_menus"] = cat_menus
        return context



class DeletePost(DeleteView):
    model = Post
    template_name = 'blogs/deletepost.html'
    # send 
    success_url = reverse_lazy('home')

    def get_context_data(self,*args,**kwargs):
        cat_menus = Category.objects.all()
        context = super(DeletePost , self).get_context_data(*args, **kwargs)
        context["cat_menus"] = cat_menus
        return context