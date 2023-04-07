from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

user_list = (UserViewSet.as_view({
    'get': 'list'
}))
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'users', UserViewSet,basename="user")

urlpatterns = [
  path('', include(router.urls)),
  path('register',RegisterUserAPIView.as_view()),
  path('login/', LoginAPIView.as_view()),
  path('logout', LogoutAPIView.as_view()),
  path('products', ProductsViewSet.as_view({'get': 'list'})),

]