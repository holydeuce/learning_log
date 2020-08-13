from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index),
    path('topics', views.topics),
    path('topics/<int:topic_id>', views.topic),
    path('new_topic', views.new_topic),
    path('new_entry/<int:topic_id>', views.new_entry),
]