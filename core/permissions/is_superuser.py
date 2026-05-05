from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSuperUserPermission(BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_superuser and request.user.is_staff and request.user.is_active
