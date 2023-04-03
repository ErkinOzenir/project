from django.urls import path
from .views import *
urlpatterns = [
  path("get-details/<id>",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login/', LoginAPIView.as_view()),
  path('logout', LogoutAPIView.as_view()),
  path('products', ProductsViewSet.as_view({'get': 'list'})),

]