from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('/om', views.AboutView.as_view(), name="about"),
    path('/kontakt', views.ContactView.as_view(), name="contact"),
]