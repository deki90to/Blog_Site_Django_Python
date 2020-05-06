from django.urls import path
# from . import views
from . views import HomeView, articleDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
	# path('',views.home, name='home')
	path('', HomeView.as_view(), name="home"),
	path('article/<int:pk>', articleDetailView.as_view(), name='article_details'),
	path('add_post/', AddPostView.as_view(), name='add_post'),
	path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
	path('article/remove/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]