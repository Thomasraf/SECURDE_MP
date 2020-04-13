"""machine_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from users import views as usersView
from library import views as libraryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', usersView.userRegister, name="register"),
    path('login/', usersView.userLogin, name="login"),
    path('profile/', usersView.userProfile, name="profile"),
    path('editPassword/', usersView.userChangePassword, name="editPassword"),
    path('logout/', usersView.userLogout, name="logout"),
    path('home/', libraryView.home, name="library-home"),
    path('about/', libraryView.about, name="library-about"),
    path('', include('library.urls')),
]