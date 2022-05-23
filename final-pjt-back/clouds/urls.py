from django.urls import path
from . import views


# ....8000/drops/
urlpatterns = [
    path('list/', views.drop_list),
    path('new/', views.drop_create),
    path('<int:pk>/', views.drop_detail),
    path('<int:pk>/like/', views.like_drop),
    path('<int:pk>/comments/', views.create_comment),
    path('<int:pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
]
