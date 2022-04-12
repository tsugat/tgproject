#from django.contrib import admin
from django.urls import path
from .views import TgList, TgDetail, TgCreate, TgDelete, TgUpdate

urlpatterns = [
    path('list/', TgList.as_view(), name='list'),
    path('detail/<int:pk>/', TgDetail.as_view(), name='detail'),
    path('create/', TgCreate.as_view(), name='create'),
    path('delete/<int:pk>/', TgDelete.as_view(), name='delete'),
    path('update/<int:pk>/', TgUpdate.as_view(), name='update'),

#    path('admin/', admin.site.urls),
]