from authenticate.models import UserProfile

def add_credit_to_context(request, user_credit = None):

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        user_credit = user_profile.credit

    context = {"credit": user_credit}
    return context