from django.urls import path

from . import views


urlpatterns = [
    path('', views.allalbums, name='allalbums'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]
