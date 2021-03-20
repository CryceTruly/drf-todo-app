from todos.models import Todo
from todos.serializers import TodoSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

class TodoList(ListCreateAPIView):
    """
    List all Todos, or create a new todos.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user,pk=self.lookup_url_kwarg)



class TodoDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todos instance.
    """
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field="id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
