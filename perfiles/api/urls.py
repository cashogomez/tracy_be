from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from perfiles.api.views import login_view, perfil_view, logout_view, session_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('login-app/', login_view, name='login-app'),
    path('registrar/', perfil_view, name='registrar'),
    path('logout/', logout_view, name='logout'),
    path('session/', session_view, name='session'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]