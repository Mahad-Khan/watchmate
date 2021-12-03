# from rest_framework.permissions import IsAdmin

# # Custom permissions

# class AdminOrReadOnly(permissions):
#     def has_permission(self, request, view):
#         admin_permissions = (request.user == "GET" and request.user.is_staff)
#         return admin_permissions or request.method == "GET"

# class ReviewUserOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, object):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             object.review_user == request.user
