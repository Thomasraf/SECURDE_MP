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
from library import views as libraryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', libraryView.accountRegister, name="register"),
    path('registerManager/', libraryView.managerRegister, name="registerManager"),
    path('login/', libraryView.accountLogin, name="login"),
    path('profile/', libraryView.accountProfile, name="profile"),
    path('editPassword/', libraryView.accountChangePassword, name="editPassword"),
    path('returnBook/<int:ISBN>', libraryView.returnBook, name="returnBook"),
    path('bookInstance/<int:ISBN>', libraryView.bookInstance, name="bookInstance"),
    path('borrowBookInstanceForm/<int:imprint>/<int:ISBN>', libraryView.borrowBookInstanceForm, name="borrowBookInstanceForm"),
    path('bookInstanceManager/<int:ISBN>', libraryView.bookInstanceManager, name="bookInstanceManager"),
    path('addBookInstance/<int:ISBN>', libraryView.addBookInstance, name="addBookInstance"),
    path('deleteBookInstance/<int:ISBN>', libraryView.deleteBookInstance, name="deleteBookInstance"),
    path('deleteBookInstanceForm/<int:imprint>/<int:ISBN>', libraryView.deleteBookInstanceForm, name="deleteBookInstanceForm"),
    path('editBookInstance/<int:ISBN>', libraryView.editBookInstance, name="editBookInstance"),
    path('editBookInstanceForm/<int:imprint>/<int:ISBN>', libraryView.editBookInstanceForm, name="editBookInstanceForm"),
    path('logout/', libraryView.accountLogout, name="logout"),
    path('about/', libraryView.about, name="library-about"),
    path('catalog/', libraryView.home, name="library-home"),
    path('addBook/', libraryView.addBook, name="addBook"),
    path('deleteBook/<int:ISBN>', libraryView.deleteBook, name="deleteBook"),
    path('editBook/<int:ISBN>', libraryView.editBook, name="editBook"),
    path('s/', libraryView.search, name="search"),
    path('userWhoForgotPassword/', libraryView.accountForgotPassword, name="forgotPassword"),
    path('editForgottenPassword/<str:username>', libraryView.editForgottenPassword, name="editForgottenPassword"),
    path('books/<int:ISBN>', libraryView.viewBook, name="viewBook"),
    path('', libraryView.home, name="library-home"),
]

handler400 = 'library.views.error_400'
handler403 = 'library.views.error_403'
handler404 = 'library.views.error_404'
handler500 = 'library.views.error_500'
