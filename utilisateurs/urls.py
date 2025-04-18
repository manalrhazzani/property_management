from django.urls import path
from .views import (
    index_view, signup_view, logout_view,
    client_dashboard, agent_dashboard, admin_dashboard,
    access_denied, CustomLoginView
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('client/', client_dashboard, name='client_dashboard'),
    path('agent/', agent_dashboard, name='agent_dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),

    path('access-denied/', access_denied, name='access_denied'),
]