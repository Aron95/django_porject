from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appointments import views

urlpatterns = [
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view()),
    path('car/', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]   


urlpatterns = format_suffix_patterns(urlpatterns)