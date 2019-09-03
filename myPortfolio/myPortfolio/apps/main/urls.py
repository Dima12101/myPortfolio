from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:comment_id>/', views.detail_comment, name="detail_comment"),
    path('leave_comment/', views.leave_comment, name="leave_comment"),
]