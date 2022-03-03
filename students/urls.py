from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('colleges', views.CollegeApiView)
router.register('students', views.StudentApiView)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
