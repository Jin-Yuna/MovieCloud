from django.urls import path
from . import views


# ....8000/drops/
urlpatterns = [
    path('list/', views.drop_list),
    path('new/', views.drop_create),
    path('<int:pk>/', views.drop_detail),
    path('comment_create/', views.comment_create),
]
