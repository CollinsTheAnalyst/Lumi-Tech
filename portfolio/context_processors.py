from .models import Profile

def profile_context(request):
    # Fetch the first profile found in the database
    # Since it's a single-user portfolio, we just take the first one.
    profile = Profile.objects.first()
    return {'profile': profile}