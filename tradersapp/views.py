from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def home2(request):
    return render(request,'home2.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def stock(request):
    return render(request,'stock.html')
def stock2(request):
    return render(request,'stock2.html')
def exchange(request):
    return render(request,'exchange.html')
def blog(request):
    return render(request,'blog.html')
def blog2(request):
    return render(request,'blog2.html')