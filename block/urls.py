from django.contrib import admin
from django.urls import path, include
from app.views import index, about, portfolio, blog, blog_detail
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path("about/", about),
    path('portfolio/', portfolio),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('login/', views.obtain_auth_token),
    path("api/v1/", include("api.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
