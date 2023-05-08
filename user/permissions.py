from rest_framework.permissions import BasePermission


class WorkerPermission(BasePermission):
    """This checks if user has worker role"""
    def has_permission(self, request, view):
        return True if request.user.is_authenticated and request.user.role == 'WORKER' else False
