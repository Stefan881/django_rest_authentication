from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,serializers
from django.contrib.auth.models import User


MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )



class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )


class Meta:
    model = User
    fields = "__all__"

