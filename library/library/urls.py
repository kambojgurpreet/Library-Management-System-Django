from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('author', views.AuthorReadOnlyModelViewSet, basename='author')
router.register('book', views.BookModelViewSet, basename='book')
router.register('customer', views.CustomerReadOnlyModelViewSet, basename='customer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
