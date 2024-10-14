
from django.urls import path,include

from .views import home_view , blog_detail,addarticle_view


app_name = 'blog'
urlpatterns = [

    path('' , home_view , name = 'blog_home'),

    path('<id>/' , blog_detail , name = 'blog_detail'),

    path('addarticle/' , addarticle_view , name = 'addarticle'),  

    path('ratings/', include('star_ratings.urls', namespace='ratings')),







   # path('<id>/' , comment_create , name = 'comment_create')



]