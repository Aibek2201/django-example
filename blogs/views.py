from django.http import JsonResponse
from . import models


def index(request, *args, **kwargs):
    blogs = models.Blog.objects.all()
    blog_titles = [{'title': b.title} for b in blogs]

    return JsonResponse(blog_titles, safe=False)
