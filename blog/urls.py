
from django.urls import path,include

from .views import home_view , blog_detail,AddarticleView,SearchView,about_us,contact_us


urlpatterns = [

    path('' , home_view , name = 'blog_home'),

    path('blogs/<id>/' , blog_detail , name = 'blog_detail'),

    path('search/' , SearchView , name = 'search'),

    path('addarticle/' , AddarticleView , name = 'addarticle'),  

    path('ratings/', include('star_ratings.urls', namespace='ratings')),

    path('about/', about_us, name='about'),

    path('contact/', contact_us, name='contact'),

 







   # path('<id>/' , comment_create , name = 'comment_create')



]