from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]
