from rest_framework import routers, viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import College, Student
from .serializers import CollegeSerializer, StudentSerializer


class IsAdminOrUserReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method in SAFE_METHODS:
            return bool(user.is_authenticated)
        return bool(user.is_active and user.is_superuser)


# Create your views here.
class CollegeApiView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrUserReadOnly]
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class StudentApiView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrUserReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class NamedAPIRootView(routers.APIRootView):
    name = 'Student List'
