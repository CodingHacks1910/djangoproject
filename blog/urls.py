from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'


urlpatterns = [
    path('', views.allblogs , name='allblogs'),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('about/', views.about, name ="about"),
    path('dark/', views.dark, name ="dark"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name ='register'),
    path('user_login', views.user_login, name ='user_login'),
]

#if not settings.DEBUG: urlpatterns += [ url(r'^uploads/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT})]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
