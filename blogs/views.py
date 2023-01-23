from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from blogs import models, serializers


@api_view(['POST'])
def create_blog(request):
    serializer = serializers.BlogModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    blog = models.Blog.objects.create(**serializer.validated_data)

    return Response(serializers.BlogModelSerializer(blog).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_blog(request, *args, **kwargs):
    blog = get_object_or_404(models.Blog.objects.all(), **kwargs)
    # blog = models.Blog.objects.get(**kwargs)
    serializer = serializers.BlogModelSerializer(blog)

    return Response(serializer.data)


class BlogView(ViewSet):

    def list(self, request, *args, **kwargs):
        blogs = models.Blog.objects.all()
        serializer = serializers.BlogModelSerializer(blogs, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        blog = get_object_or_404(models.Blog.objects.all(), pk=pk)
        serializer = serializers.BlogModelSerializer(blog)

        return Response(serializer.data)


class BlogViewSet(ModelViewSet):

    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogModelSerializer