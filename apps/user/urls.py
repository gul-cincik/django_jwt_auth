from django.contrib import admin
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from .schema import schema

app_name = 'user'  # Optional namespace for the app

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('breweries/', views.breweries, name='breweries'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),

]