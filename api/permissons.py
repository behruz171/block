from rest_framework import permissions

class ServicePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.first_name == 'behruz' and request.method == 'GET':
            return True
        return False

class PostPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return True
        elif user.is_superuser:
            return True
        return False