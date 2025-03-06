
from django.urls import path,include

from .views import home_view , blog_detail,AddarticleView,SearchView


urlpatterns = [

    path('' , home_view , name = 'blog_home'),

    path('blogs/<id>/' , blog_detail , name = 'blog_detail'),

    path('addarticle/' , AddarticleView , name = 'addarticle'),  

    path('ratings/', include('star_ratings.urls', namespace='ratings')),

    path('search/' , SearchView , name = 'search'),

 







   # path('<id>/' , comment_create , name = 'comment_create')



]