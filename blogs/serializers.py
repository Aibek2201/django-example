from rest_framework import serializers
from blogs import models

# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     blog = serializers.CharField()

class BlogModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)

    class Meta():
        model = models.Blog
        fields = '__all__'      # ('id', 'title')