from django.urls import path
from .views import UsersList, UsersDetail, RatingsList, RatingsDetail, ProfileView

urlpatterns = [
    path('users/', UsersList.as_view(), name='users_list'),
    path('users/<int:id>/', UsersDetail.as_view(), name='users_detail'),
    path('ratings/', RatingsList.as_view(), name='ratings_list'),
    path('ratings/<int:id>/', RatingsDetail.as_view(), name='ratings_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
