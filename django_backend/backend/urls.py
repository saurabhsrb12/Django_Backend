from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WorkList, WorkDetail , RegisterAPI
urlpatterns = [
    path('works/', WorkList.as_view(), name='work-list'),
    path('works/<int:pk>/', WorkDetail.as_view(), name='work-detail'),
    path('register/', RegisterAPI.as_view(), name='register'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
