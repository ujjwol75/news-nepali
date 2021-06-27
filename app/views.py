from django.shortcuts import render
from .models import Category, News
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.views import View



# Create your views here.
def base(request):
    return render(request, 'app/base.html')

def home(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:4]
    three_categories = Category.objects.all()[0:3]
    return render(request, 'app/home.html', {'first_news':first_news, 'three_news':three_news, 'three_categories':three_categories})

def all_news(request):
    all_news = News.objects.all()
    return render(request, 'app/all-news.html', {'all_news':all_news})

def detail(request,id):
    news = News.objects.get(pk=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    return render(request, 'app/detail.html', {'news':news, 'related_news':rel_news})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations! Registered Successfully.")
            form.save()
            form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
