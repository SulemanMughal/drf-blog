# # posts/urls.py
# from django.urls import path
# # from .views import PostList, PostDetail
# from .views import UserList, UserDetail, PostList, PostDetail
# urlpatterns = [
#     path('users/', UserList.as_view()), # new
#     path('users/<int:pk>/', UserDetail.as_view()), #
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]



# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls