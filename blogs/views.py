from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from blogs import services, models, serializers


class BlogViewSet(ModelViewSet):
    blog_services = services.BlogServicesV1()
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.blog_services.create_blog(data=serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.blog_services.get_blogs()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)