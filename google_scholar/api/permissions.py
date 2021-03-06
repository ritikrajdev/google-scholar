from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, organisation):
        if request.method in SAFE_METHODS:
            return True

        return organisation.user == request.user

