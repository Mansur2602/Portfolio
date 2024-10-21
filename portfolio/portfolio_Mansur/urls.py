from django.contrib import admin
from django.urls import path

from portfolio_Mansur.views import main, about_me, portfolio, skills
urlpatterns = [
path('', main),
path('about_me', about_me, name= 'about_me' ),
path('portfolio', portfolio, name = 'portfolio'),
path('skills', skills, name = 'skills' )
]
