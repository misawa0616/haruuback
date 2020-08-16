from .views import ConfirmEmailAPIView, ChangeEmailAPIView, TestAPIView

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
    url('rest_auth/', include('rest_auth.urls')),
]
