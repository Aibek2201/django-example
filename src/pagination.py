from rest_framework.pagination import PageNumberPagination, CursorPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'


class CustomCursorPagination(CursorPagination):
    page_size_query_param = 'page_size'
    ordering = '-created_at'