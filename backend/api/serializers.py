"""Serializers for the API."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Metadata for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
