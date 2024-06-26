import django_filters.rest_framework

from . models import Student
from . serializers import StudentSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import CustomPermission

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['firstName', 'secondName', 'year', 'phone']
