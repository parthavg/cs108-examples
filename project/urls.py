from django.urls import path
from .views import *

urlpatterns = [
    path('all/', PostersPageView.as_view(), name="show_all_posters"),#home page showing all posters
    path('<str:type>/', PostersCategoryPageView.as_view(), name="show_category_posters"),#filtering through different categories of posters
    path('poster/<int:pk>/', PosterPageView.as_view(), name="show_poster_page"),#displays individual poster page
    path('profile/<int:pk>/', ProfilePageView.as_view(), name="show_profile"),#displays user profile
    path('create_list', CreateListView.as_view(),name="create_list"),# allows one to create a new Poster listing
    path('create_profile', CreateProfileView.as_view(),name="create_profile"),# allows one to create a new profile
    path('poster/<int:pk>/update', UpdatePosterView.as_view(), name="update_poster"),# updates poster
    path('poster/<int:pk>/post_review',post_review_message, name="post_review"),# allows user to post review
    path('poster/<int:poster_pk>/delete_review/<int:review_pk>', DeleteReviewView.as_view(), name="delete_review"), #delete review uploaded by the respective profile
    path('search/', SearchView.as_view(), name="search"),#search through all posters
]

