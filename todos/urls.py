from django.urls import path
from .views import TodoList, TodoDetail


urlpatterns = [
    path('', TodoList.as_view(),name="todos"),
    path('<int:id>', TodoDetail.as_view(), name="todo"),
]
