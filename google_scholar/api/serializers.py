from . import models

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    organisations = serializers.HyperlinkedRelatedField(view_name='organisation-detail', many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'organisations']


class OrganisationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    scholars = serializers.HyperlinkedRelatedField(view_name='scholar-detail', many=True, read_only=True)
    
    class Meta:
        model = models.Organisation
        fields = '__all__'


class ScholarSerializer(serializers.ModelSerializer):
    organisations = serializers.HyperlinkedRelatedField(view_name='organisation-detail', many=True, read_only=True)
    papers = serializers.HyperlinkedRelatedField(view_name='paper-detail', many=True, read_only=True)
    
    class Meta:
        model = models.Scholar
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    scholars = serializers.HyperlinkedRelatedField(view_name='scholar-detail', many=True, read_only=True)
    
    class Meta:
        model = models.Paper
        fields = '__all__'

