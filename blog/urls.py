from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/create/', views.createblog, name='createblog'),
    path('blog/edit/<int:id>/',views.update, name='update'),
    path('blog/edit/',views.update, name='update'),
]



