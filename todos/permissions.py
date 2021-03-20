from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message="Not allowed to do anything on this one"
    def has_object_permission(self, request, view, obj):
        return request.user==obj.owner