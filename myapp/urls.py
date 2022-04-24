from .views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('test/', test, name='test'),
    path('', cache_page(60)(BoshNews.as_view()), name='home'),
    # path('', index, name='home'),
    path('', BoshNews.as_view(), name='home'),
    path('category/<slug:slug>', get_category, name='category'),
    # path('category/<slug:slug>', NewsByCategory.as_view(), name='category'),
    # path('news/<slug:slug>', view_news, name='view_news'),
    path('news/<slug:slug>', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    # path('news/add_news/', add_news, name='add_news'),
]