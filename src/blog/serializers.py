from rest_framework import serializers
from .models import Posts
import datetime


class PostsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Posts
        fields = ("id","title", "date", "description", "content")