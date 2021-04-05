from django.urls import path
from .views import * #ShowAllProfilesView, ShowProfilePageView, RandomShowProfilePageView #our view class definition


urlpatterns = [
    path('', RandomShowProfilePageView.as_view(), name="random"),
    path('all', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('show_profile_page/<int:pk>', ShowProfilePageView.as_view(), name="profile"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="post_status"),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status")#delete
] 