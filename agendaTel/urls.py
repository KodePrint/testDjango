"""agendaTel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# Importamos la vista de creacion de contacto
from contacto.views import Create, List, Update, Delete, actualizar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', Create.as_view(), name='createContact'),
    path('', List.as_view(), name='listContact'),
    path('update/<int:pk>', Update.as_view(), name='updateContact'),
    path('delete/<int:pk>', Delete.as_view(), name='deleteContact'),
    path('actualizar/', actualizar, name='update'),
]
