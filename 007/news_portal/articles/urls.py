from django.contrib import admin  
from django.urls import path, include  
from articles.views import home_view, register_view, article_create_view, CustomLoginView

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('accounts/', include('django.contrib.auth.urls')),   
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),  
    path('article/create/', article_create_view, name='article_create'),  
    path('', home_view, name='home'),  
]  