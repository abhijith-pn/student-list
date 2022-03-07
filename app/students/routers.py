from rest_framework.routers import DefaultRouter

from . import views


class NamedDefaultRouter(DefaultRouter):
    include_root_view = False
    APIRootView = views.NamedAPIRootView


router = NamedDefaultRouter()
router.register('colleges', views.CollegeApiView)
router.register('students', views.StudentApiView)
