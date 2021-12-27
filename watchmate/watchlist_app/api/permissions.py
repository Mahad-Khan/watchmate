from rest_framework import permissions

# # Custom permissions
class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permissions = bool(request.user and request.user.is_staff)
        return admin_permissions or request.method == "GET"


class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.review_user

class HIsReviewUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        has_permissions = bool(request.user and request.user.is_staff)
        return has_permissions
    
    
# class ReviewUserOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, object):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             object.review_user == request.user
