from rest_framework import permissions, status
from rest_framework.response import Response


class FollowIsExists(permissions.BasePermission):
    def has_permissions(self, request, view):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GroupReadOnly(permissions.BasePermission):
    def has_permissions(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
