from django.db import models

from django_jalali.db import models as jmodels

from django.contrib.auth import get_user_model

from accounts.models import MyUser


class Course(models.Model):

    category = models.ForeignKey("Category" , null = True ,  blank = True , on_delete = models.SET_NULL)

    title = models.CharField(max_length = 250)

    content = models.TextField()

    image = models.ImageField(upload_to = 'blog/' , null = True , blank = True)

    slug = models.SlugField(unique = True , max_length = 250)

    status = models.BooleanField(default = False)

    time_of_study = models.IntegerField(default = 0)

    created_date = models.DateTimeField(auto_now_add = True)

    updated_date = models.DateTimeField(auto_now = True)

    created_date_jalali = jmodels.jDateField(auto_now_add = True , blank = True , null = True)

    updated_date_jalali = jmodels.jDateField(auto_now = True , blank = True , null = True)

    teacher = models.CharField(max_length = 150)

    price = models.IntegerField(null = True)

    discount_price = models.IntegerField(null=True, blank=True)  # قیمت با تخفیف (اختیاری)
    
    def get_final_price(self):
        """محاسبه قیمت نهایی با تخفیف (در صورت وجود)"""
        return self.discount_price if self.discount_price else self.price
    
    # Methods
    def __str__(self):

        return str(self.title)

class Category(models.Model):

    '''
        
        THIS IS A MODEL FOR CATEGORY OBJECTS...

    '''

    title = models.CharField(max_length = 250)

    slug = models.SlugField(unique = True , max_length = 250)

    created_date = models.DateTimeField(auto_now_add = True)

    updated_date = models.DateTimeField(auto_now = True)

    created_date_jalali = jmodels.jDateField(auto_now_add = True , blank = True , null = True)

    updated_date_jalali = jmodels.jDateField(auto_now = True , blank = True , null = True)

    # Methods
    def __str__(self):

        return f'{self.id} , {self.title}'

class Comment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    

class Article(models.Model):
    author =models.ForeignKey(MyUser,on_delete=models.PROTECT)
    category =models.ForeignKey(Category,on_delete=models.PROTECT)
    title=models.CharField(max_length=800)
    abstract= models.TextField(default=None)
    key_word_1=models.CharField(max_length=100,default=None)
    key_word_2=models.CharField(max_length=100,default=None)
    key_word_3=models.CharField(max_length=100,default=None)    
    body= models.TextField(default=None)
    image = models.ImageField(upload_to = 'blog/' , null = True , blank = True)
    created_date_jalali = jmodels.jDateField(auto_now_add = True , blank = True , null = True)

    STATUS_CHOICES={
        ('draft','Draft'),
        ('published','Published'),
        ('archived','Archived'),
    }
    status=models.CharField( max_length=20, choices=STATUS_CHOICES,default=None,null=True)
    def __str__(self):  
        return '{}'.format(self.title)


class Basket(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="items")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.basket.user.username} - {self.course.title}"

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'در انتظار پرداخت'), ('paid', 'پرداخت شده')],
        default='pending'
    )
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.status}"