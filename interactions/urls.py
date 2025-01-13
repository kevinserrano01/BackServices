from django.urls import path
from .views import PostsList, PostsDetail, RequestsList, RequestsDetail, StatusServicesList, StatusServicesDetail

urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts_list'),
    path('posts/<int:id>/', PostsDetail.as_view(), name='posts_detail'),
    path('requests/', RequestsList.as_view(), name='requests_list'),
    path('requests/<int:id>/', RequestsDetail.as_view(), name='requests_detail'),
    path('statusservices/', StatusServicesList.as_view(),
         name='statusservices_list'),
    path('statusservices/<int:id>/', StatusServicesDetail.as_view(),
         name='statusservices_detail'),
]
