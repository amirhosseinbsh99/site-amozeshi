from django.urls import path 

from blog.views import review_articles,accept_article,reject_article
from .views import (
						login_view, 
						register_view,
						dashboard_view, 
                        user_dashboard_edit,
						logout_view,
						kave_negar_token_send,
                        courses_view,
                        edit_course_view,
                        create_course_view,
                        
					)

app_name= 'accounts'
urlpatterns = [

	path('login/' , login_view , name = 'login_view'),

	path('dashboard/' , dashboard_view , name = 'dashboard_view'),
    
	path('dashboard/edit/', user_dashboard_edit, name='user_dashboard_edit'),
    
	path('dashboard/courses/' , courses_view , name = 'courses_view'),
    
    path('courses/<int:course_id>/', edit_course_view, name='edit_course_view'),
    
	path('courses/create/', create_course_view, name='create_course_view'),

	path('register/' , register_view , name = 'register_view'),

	path('logout/', logout_view, name='logout_view'),

	path('kave_negar_token_send/',kave_negar_token_send,name = 'kave_negar_token_send'),
    
]