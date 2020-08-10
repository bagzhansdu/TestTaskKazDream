from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='base-home'),
    path(r'<lesson_pk>',views.more, name='lesson-more')
]