from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),  # 消さないとエラーなる
    path('', include('diary.urls')),
    path('accounts/',include('allauth.urls')),
]
