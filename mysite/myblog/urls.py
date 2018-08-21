from django.urls import path

from .views import detail_view, list_view
from django.conf.urls import url, include
from rest_framework import routers
from myblog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
