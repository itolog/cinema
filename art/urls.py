from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:id>', views.page, name='page'),
    path('search', views.search, name='search'),
    path('video', views.video, name='video'),
]
