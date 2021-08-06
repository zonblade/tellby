from verification.models import active_user, Inactive_user

def ActiveUser(userid):
    is_active = active_user.objects.filter(user_id=userid).count()
    if is_active:
        active = True
        return active
    else:
        active = False
        return active

def XActiveUser(userid):
    is_not_active = Inactive_user.objects.filter(user_id=userid).count()
    if is_not_active:
        inactive = True
        return inactive
    else:
        inactive = False
        return inactive