"""
メモ：
プロジェクトのurls.py（自動でできたファイル）
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tgpost.urls')),
]
