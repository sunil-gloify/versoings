from rest_framework import viewsets
from myapp.models import *
from .serializers import *


class USerVS(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
