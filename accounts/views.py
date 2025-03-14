from django.shortcuts import render , redirect ,get_object_or_404


from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import MyUser

from blog.models import Course

from django.contrib.auth.hashers import check_password

from django.contrib.auth import login

from django.contrib.auth import logout

from kavenegar import *

from blog.models import Article,Category

import random



from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):

	'''
		a function for login view
	'''

	if not request.user.is_authenticated:


		if request.method == 'POST':

			username = request.POST.get('username' , None)

			password = request.POST.get('password' , None)

			if username == '' or username == None :

				messages.error(request , 'نام کاربری خالی است')

				return redirect('accounts:login_view')

			if password == '' or password == None :

				messages.error(request , 'رمز خود را وارد کنید')

				return redirect('accounts:login_view')

			try:
				
				user = MyUser.objects.get(username = username)

				matchcheck = check_password(password , user.password)

				if matchcheck:

					login(request , user)

					return redirect('accounts:dashboard_view')



			except:

				messages.error(request , 'کاربری یافت نشد')

				return redirect('accounts:login_view')


		return render(request , 'registerations/login.html')

	else:

		return redirect('blog:blog_home')

@login_required
def dashboard_view(request):
	if request.user.is_admin == True:
		user_count = MyUser.objects.count()
		course_count = Course.objects.count()
		article_count = Article.objects.count()

	return render(request , 'User/dashboard.html' , {'user_count': user_count,'course_count': course_count,'article_count': article_count})

@login_required
def courses_view(request):
    if request.user.is_admin:
        query = request.GET.get('q', '')
        courses = Course.objects.all()

        if query:
            courses = courses.filter(name__icontains=query)  # Adjust 'name' to match your model

        return render(request, 'User/courses.html', {'courses': courses, 'query': query})
	

@login_required
def edit_course_view(request, course_id):
    try:
        # Fetch the course by its ID
        course = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        raise Http404("دوره یافت نشد")

    if request.method == 'POST':
        # Process form submission to update course details
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        teacher = request.POST.get('teacher')
        time_of_study = request.POST.get('time_of_study')

        # Update course fields
        course.title = title
        course.content = content
        course.teacher = teacher
        course.time_of_study = time_of_study

        # Save image if a new one was uploaded
        if image:
            course.image = image

        course.save()  # Save the course instance

        # Add a success message to notify the user
        messages.success(request, "دوره با موفقیت ویرایش شد!")

        # Redirect to the courses view or another relevant page
        return redirect('accounts:courses_view')

    return render(request, 'User/course_detail.html', {'course': course})




def register_view(request):
	if not request.user.is_authenticated:

		if request.method == 'POST':
			

			global first_name
			first_name = request.POST['first_name']
			global last_name 
			last_name= request.POST['last_name']
			global username 
			username= request.POST['username']
			global email 
			email= request.POST['email' ]
			global password 
			password= request.POST['password' ]
			global password2 
			password2= request.POST['password']
			global phone_number 
			phone_number= request.POST['phone_number']
			if username == '' or username == None :

				messages.error(request , 'نام کاربری خالی است')

				return redirect('accounts:register_view')
			if password == '' or password == None :

				messages.error(request , 'رمز خود را وارد کنید')

				return redirect('accounts:register_view')
			if email == '' or email == None :

				messages.error(request , 'ایمیل خود را وارد کنید ')

				return redirect('accounts:register_view')
			if first_name == '' or first_name == None :

				messages.error(request , 'نام خود را وارد کنید')

				return redirect('accounts:register_view')
			if last_name == '' or last_name == None :

				messages.error(request , 'نام خود را وارد کنید')

				return redirect('accounts:register_view')
			if phone_number == '' or phone_number == None :

				messages.error(request , 'شماره خود را وارد کنید')

				return redirect('accounts:register_view')
	
			if password == password2:
				if MyUser.objects.filter(email=email).exists():
					messages.info(request,'email is already used')
					return redirect('accounts:register_view')
				elif MyUser.objects.filter(username=username).exists():
					messages.info(request,'username is already used')
					return redirect('accounts:register_view')
				elif MyUser.objects.filter(phone_number=phone_number).exists():
					messages.info(request,'phone_number is already used')
					return redirect('accounts:register_view')
				else:
				#User = MyUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,phone_number=phone_number)
						
					try:
						token2 = 12345


						api = KavenegarAPI('7937386A425358714D3072664F59414B4D79416D6E444C534C55357A724E33395258437661466F34727A343D')
						phone=phone_number

						params = {
						'token': token2,
						'receptor':'',
						'template': 'amir',
						'type': 'sms'
						}
						response = api.verify_lookup(params)
						print(response)
					except APIException as e: 
						print(e)
					except HTTPException as e: 
						print(e)

					User = MyUser.objects.create_user(username=username,token_send=token2)
					return redirect('accounts:kave_negar_token_send')

					
								
			else:



				messages.info(request,'passwords are not same')
				return redirect('accounts:register_view')
		else:
			return render(request,'registerations/register.html')

	else:

		return redirect('blog:blog_home')





def logout_view(request):

	logout(request)
	return redirect('blog_home')

def kave_negar_token_send(request):


	if request.method == 'POST':
		sms_code = request.POST['sms_code']
	
		if sms_code == '' or sms_code == None :
			messages.error(request , 'کد خود را وارد کنید')
		elif MyUser.objects.filter(token_send=sms_code).exists():
			MyUser.objects.filter(token_send=sms_code).delete()
			User = MyUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,phone_number=phone_number)


			return redirect('accounts:dashboard_view')
		else:
			messages.error(request , 'کد خود به درستی را وارد کنید')

	return render(request,'registerations/phonenumber.html') 

@login_required
def addarticle_view(request):


    if request.method == 'POST':

        author = request.user
        category_id = Category.objects.get(id=request.POST['category'])

        article=Article(
            author = author,
            category = category_id,
            title = request.POST['title'],
            abstract = request.POST['abstract'],
            key_word_1=request.POST['key_word_1'],
            key_word_2=request.POST['key_word_2'],
            key_word_3=request.POST['key_word_3'],
            body=request.POST['body'],
            created_date_jalali=request.POST['created_date_jalali'],
        )
        article.save()
        return render(request, 'registerations/addarticle.html')
    else:
        categories = Category.objects.all()
        return render(request, 'registerations/addarticle.html',{'categories': categories })





	