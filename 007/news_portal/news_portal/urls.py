from django.contrib import admin  
from django.urls import path, include  
from articles.views import home_view, register_view, article_create_view, CustomLoginView, NewsListView

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),   
    path('news/', NewsListView.as_view(), name='news'),
    path('article/create/', article_create_view, name='article_create'),   
    path('', home_view, name='home'),  # Добавляем маршрут для корневого URL  
]  