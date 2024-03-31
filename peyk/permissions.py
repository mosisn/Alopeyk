from rest_framework.permissions import BasePermission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.all().role == 'customer')