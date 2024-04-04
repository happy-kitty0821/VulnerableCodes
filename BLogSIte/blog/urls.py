from . import views
from django.urls import path
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('read_file/', views.read_file, name='read_file'),
    path('robots.txt', views.robots, name='robots'),
    path('loginusr/', views.userlogin, name='loginusr'),
    path('development/', views.development, name='development'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout, name='logout'),
    path('writeBlog/', views.writeBlogPost, name='writeBlog'),
    path('loginusr/signup/', views.signup, name='signup'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/logout', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    # path('profile/writeBlog/', views.writeBlogPost, name='writeBlog')   
] 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
