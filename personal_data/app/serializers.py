from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from .models import *

class RequesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequesterData
        fields = '__all__'

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CandidateData
        fields = '__all__'

class IndividualBusinessmanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndividualBusinessman
        fields = '__all__'


