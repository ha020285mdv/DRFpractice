from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myAPI.API.resources import WriterViewSet, BookViewSet


router = routers.SimpleRouter()
router.register('writers', WriterViewSet)
router.register('books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
