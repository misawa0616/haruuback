from .views import ConfirmEmailAPIView, ChangeEmailAPIView, TestAPIView, FavoriteRegisterAPIView, \
    FavoriteEditorAPIView, UserRegisterAPIView, ConfirmUserAPIView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^confirm_change_email/(?P<key>[-:\w]+)/$',
        ConfirmEmailAPIView.as_view(),
        name='confirm_change_email'),
    url(r'^change_email/',
        ChangeEmailAPIView.as_view(),
        name='change_email'),
    url('test/',
        TestAPIView.as_view(),
        name='test'),
    url('favorite_register/',
        FavoriteRegisterAPIView.as_view(),
        name='favorite_register'),
    url('favorite_editor/',
        FavoriteEditorAPIView.as_view(),
        name='favorite_editor'),
    url('user_register/',
        UserRegisterAPIView.as_view(),
        name='user_register'),
    url(r'confirm_user/(?P<key>[-:\w]+)/$',
        ConfirmUserAPIView.as_view(),
        name='confirm_user'),
    url('rest_auth/', include('rest_auth.urls')),
]
