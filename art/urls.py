from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('serials', views.serials, name='serials'),
    path('page/<int:id>', views.page, name='page'),
    path('page-serials/<int:id>', views.page_serials, name='page-serials'),
    path('search/<int:page>', views.search, name='search'),
    path('video', views.video, name='video'),
]
