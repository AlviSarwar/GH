from music.models import PremiumSubscription


def premium_status(request):
    """
    Inject premium status into every template context.
    is_premium  → bool: user has an active subscription
    user_subscription → PremiumSubscription object or None
    """
    if not request.user.is_authenticated:
        return {'is_premium': False, 'user_subscription': None}
    try:
        sub = request.user.subscription
        is_premium = sub.is_active()
        return {'is_premium': is_premium, 'user_subscription': sub}
    except PremiumSubscription.DoesNotExist:
        return {'is_premium': False, 'user_subscription': None}
