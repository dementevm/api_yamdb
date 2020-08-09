from rest_framework.permissions import SAFE_METHODS, IsAdminUser


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        # is_admin = super().has_permission(request, view)
        # return request.method in SAFE_METHODS or is_admin
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == 'admin'
