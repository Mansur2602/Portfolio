from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'base.html')

def about_me(request):
    return render(request, 'about_me.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def skills(request):
    return render(request, 'skills.html')