
from django.urls import path
from .views import AccesstypeListAPIView

urlpatterns = [
    path('/all', AccesstypeListAPIView.as_view(), name='all'),

]
