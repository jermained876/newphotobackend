
from django.urls import path
from .views import AdminAccessOnlyAPIView, AuthenticatedAccessOnlyAPIView, GetAlbumFilesAuthAPIView, GetCurrentUserAPIView, ChangeFileToHidden, ChangeFileToOpen, AlbumToPublicAPIView, AlbumToPrivatAPIView, CreateCustomerUserCreateAPIView, CreateGuestUserCreateAPIView, ChangeToCustomerAPIView, ChangeToGuestAPIView, ChangeToAdminAPIView

urlpatterns = [
    path('/createCustomer', CreateCustomerUserCreateAPIView.as_view(), name='createCustomer'),
    path('/createGuest', CreateGuestUserCreateAPIView.as_view(), name='createGuest'),
    path('/currentuser', GetCurrentUserAPIView.as_view(), name='currentuse'),
    path('/changeUsertoCustomer/<str:username>', ChangeToCustomerAPIView.as_view(), name='UsertoCustomer'),
    path('/changeUsertoGuest/<str:username>', ChangeToGuestAPIView.as_view(), name='UsertoGuest'),
    path('/changeUsertoAdmin/<str:username>', ChangeToAdminAPIView.as_view(), name='UsertoAdmin'),
    path('/albumToPrivate/<str:slug>', AlbumToPrivatAPIView.as_view(), name='AlbumtoPrivate'),
    path('/albumToPublic/<str:slug>', AlbumToPublicAPIView.as_view(), name='AlbumtoPublic'),
    path('/changeFileToOpen/<str:slug>', ChangeFileToOpen.as_view(), name='FiletoOpen'),
    path('/changeFileToHidden/<str:slug>', ChangeFileToHidden.as_view(), name='FiletoHidden'),
    path('/getalbumfileAuth/<str:slug>', GetAlbumFilesAuthAPIView.as_view(), name='ablumfilesAUth'),
    path('/adminOnly', AdminAccessOnlyAPIView.as_view(), name='AdminOnly'),
    path('/authOnly', AuthenticatedAccessOnlyAPIView.as_view(), name='AuthOnly'),
]
