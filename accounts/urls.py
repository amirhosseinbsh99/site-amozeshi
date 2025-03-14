from django.urls import path 

from blog.views import review_articles,accept_article,reject_article
from django.contrib.auth.views import LogoutView
from .views import (
						login_view, 
						register_view,
						dashboard_view, 
						logout_view,
						kave_negar_token_send,
						addarticle_view,
                        courses_view,
                        edit_course_view,
                        
					)

app_name= 'accounts'
urlpatterns = [
	
	path('dashboard/addarticle/' , addarticle_view , name = 'addarticle'),  

	path('login/' , login_view , name = 'login_view'),

	path('dashboard/' , dashboard_view , name = 'dashboard_view'),
    
	path('dashboard/courses/' , courses_view , name = 'courses_view'),
    
    path('courses/<int:course_id>/', edit_course_view, name='edit_course_view'),

	path('register/' , register_view , name = 'register_view'),

	path('logout/', logout_view, name='logout_view'),

	path('kave_negar_token_send/',kave_negar_token_send,name = 'kave_negar_token_send'),
    
	path('reviewarticles',review_articles,name='review_articles'),
    path('reviewarticles/accept/<int:article_id>',accept_article,name='accept_article'),
    path('reviewarticles/reject/<int:article_id>',reject_article,name='reject_article'),



	


]