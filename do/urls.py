from django.urls import path
from . views import index,update,delete

urlpatterns = [
    
    path('', index, name='index'),
    path('update/<str:pk>/', update, name='update'),
    path('delete/<str:pk>/', delete, name='delete'),

]
