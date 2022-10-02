"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from .views import questionList,questionDetails, choiceList, choiceDetails,qChoice

app_names="main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',questionList.as_view(),name='main.qList'),
    path('<int:pk>',questionDetails.as_view(),name='main.qDetails'),
    path('choice/',choiceList.as_view(),name='main.chList'),
    path('choice/id',qChoice.as_view(),name='main.chDetails'),
    

]
