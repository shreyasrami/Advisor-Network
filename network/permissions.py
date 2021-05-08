from rest_framework import permissions

class NotUser(permissions.BasePermission):
    message = "Users cannot add new advisors."
    def has_permission(self,request,view):
        
        if request.user.is_authenticated:
            return False
        else:
            return True
        