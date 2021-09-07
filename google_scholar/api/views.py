from . import serializers
from . import models
from . import permissions

from django.contrib.auth.models import User
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class OrganisationViewSet(ModelViewSet):
    serializer_class = serializers.OrganisationSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]

    def get_queryset(self):
        return models.Organisation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScholarViewSet(ModelViewSet):
    queryset = models.Scholar.objects.all()
    serializer_class = serializers.ScholarSerializer


class PaperViewSet(ReadOnlyModelViewSet):
    queryset = models.Paper.objects.all()
    serializer_class = serializers.PaperSerializer

