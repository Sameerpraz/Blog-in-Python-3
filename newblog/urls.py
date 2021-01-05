from django.urls import path
# from . import views
from .views import HomeView,ArticleDetailView,AddPostView,PostUpdate,DeletePost
# app_name="newblog"
urlpatterns=[
    # path('',views.index,name='index'),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>/',ArticleDetailView.as_view(),name='view_article'),
    path('add/',AddPostView.as_view(),name='addpost'),
    path('article/edit/<int:pk>/' , PostUpdate.as_view() , name='update'),
    path('article/<int:pk>/delete' , DeletePost.as_view() , name='delete'),

]