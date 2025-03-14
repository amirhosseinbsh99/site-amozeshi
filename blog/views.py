from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Course	

from .models import Comment,Article

from accounts.models import MyUser

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# a view for home
def home_view(request):

    courses = Course.objects.filter(status=True)
    # posts = Post.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'blog/blogs.html', context)

def SearchView(request):

    query = request.GET.get('search','')
    results = Course.objects.filter(name__iconcontaints=query) if query else []

    return render(request, 'blog/search_resualts.html',{'resualts': results , 'query': query})


# a view for detail of blog
def blog_detail(request, id):
    course = Course.objects.get(pk=id, status=True)
    comments = course.comments.filter(active=True)
    
# Comment posted
    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')

        if not comment_content:
            messages.error(request, 'متن شما خالی است')
        else:
            try:
                comment = Comment.objects.get(
                    body=comment_content,
                    name=request.user.first_name,
                    email=request.user.email,
                    active=False,
                    course=course
                )

                messages.error(request, 'شما قبل این نظر را ارسال کردید')
            except Comment.DoesNotExist:
                comment = Comment.objects.create(
                    course=course,
                    name=request.user.first_name,
                    email=request.user.email,
                    body=comment_content,
                    active=False
                )
                messages.success(request, 'نظر شما ثبت شد')
                return redirect('.')

    return render(request, 'blog/blog-detail.html', {'course': course, 'comments': comments})




def AddarticleView(request):
    if request.method == 'POST':
		# article=Article(
		# 	user = request.POST['user'],
    	# 	category = request.POST['category'],
		# 	title = request.POST['title'],
		# 	abstract = request.POST['abstract'],
		# 	key_word_1=request.POST['key_word_1'],
		# 	key_word_2=request.POST['key_word_2'],
		# 	key_word_3=request.POST['key_word_3'],
		# 	body=request.POST['body'],
		# 	created_date_jalali=request.POST['created_date_jalali'],
		# )
            # 'user': request.POST.get('user'),
            # 'category': request.POST.get('category'),
            # 'title': request.POST.get('title'),
            # 'abstract': request.POST.get('abstract'),
            # 'key_word_1': request.POST.get('keywords1'),
            # 'key_word_2': request.POST.get('keywords2'),
            # 'key_word_3': request.POST.get('keywords3'),
            # 'body': request.POST.get('body'),
            # 'created_date_jalali': request.POST.get('date'),
        
        return render(request, 'registerations/addarticle.html')
    else:
        return render(request, 'registerations/addarticle.html')

@login_required
def review_articles(request):
    if request.user.is_superuser:
        articles= Article.objects.filter(status='draft')
        return render(request)
    else:
        return HttpResponse('what??bro you are normal user this page is for superuser')
        
@login_required
def    accept_article(request,article_id):
    article=Article.objects.get(id=article_id)
    if request.user.is_superuser:
        article.status='published'
        article.save()
        messages.SUCCESS(request,f'accepted article{article.title}.')
    else:
        return HttpResponse('what??bro you are normal user this page is for superuser')

    return redirect('../')

@login_required
def reject_article(request,article_id):
    article=Article.objects.get(id=article_id)
    if request.user.is_superuser:
        article.status='archived'
        article.save()
        messages.SUCCESS(request,f'accepted article{article.title}.')
    else:
        return HttpResponse('what??bro you are normal user this page is for superuser')

    return redirect('../')  


def about_us(request):
    return render(request, 'blog/about-us.html')

def contact_us(request):
    return render(request, 'blog/contact-us.html')