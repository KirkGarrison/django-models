from django.urls import path
from .views import SnackListView
from .views import AboutPageView
from .views import SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]