from .models import DashboardSetting

def dashboard_settings(request):
    """Makes dashboard settings available in all templates"""
    try:
        return {
            'dashboard_settings': DashboardSetting.load()
        }
    except Exception as e:
        # Fallback if settings don't exist yet
        from django.conf import settings
        if settings.DEBUG:
            print(f"Dashboard settings error: {e}")
        return {
            'dashboard_settings': None
        }