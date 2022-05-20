from django.urls import path
from . import views


# ....8000/drops/
urlpatterns = [
    path('new/', views.drop_create),
    path('<int:pk>/', views.drop_detail),
    path('<int:pk>/edit', views.drop_edit_delete ),
]
