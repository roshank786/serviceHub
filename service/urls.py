from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from service import views


urlpatterns = [

    path('token/',ObtainAuthToken.as_view()),

    path('customers/',views.CustomerListCreateView.as_view()),

]