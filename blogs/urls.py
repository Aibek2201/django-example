from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs import views


router = DefaultRouter()
router.register(r'', views.BlogViewSet)

urlpatterns = [
    # path('', views.create_blog),
    # path('<int:id>/', views.get_blog),
    path('', include(router.urls)),
    # path('v2/', views.BlogView.as_view({'get': 'list'})),
    # path('v2/<int:pk>/', views.BlogView.as_view({'get': 'retrieve'})),
]