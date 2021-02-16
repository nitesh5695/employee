from django.db.models import fields
from rest_framework import serializers
from .models import employers,employer_profile,companies,company_profile


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model=companies
        fields="__all__"

class employerSerializer(serializers.ModelSerializer):
    class Meta:
        model=employers
        fields="__all__"        