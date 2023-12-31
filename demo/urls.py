"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/index', views.index, name='department-index'),
    path('department/add', views.add, name='department-add'),
    path('department/destroy/<int:id>', views.destroy, name='department-destroy'),
    path('department/update/<int:id>', views.update, name='department-update'),

    path('userinfo/index', views.userinfo_index, name='userinfo-index'),
    path('userinfo/add', views.userinfo_add, name='userinfo-add'),
    path('userinfo/destroy/<int:id>', views.userinfo_destroy, name='userinfo-destroy'),
    path('userinfo/update/<int:id>', views.userinfo_update, name='userinfo-update')

]
