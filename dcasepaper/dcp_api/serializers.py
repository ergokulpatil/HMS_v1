from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *
from rest_framework_bulk import (BulkListSerializer,BulkSerializerMixin)


class PatientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=PatientProfile
        fields='__all__'
