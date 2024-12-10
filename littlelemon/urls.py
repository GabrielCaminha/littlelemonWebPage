from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views


# Configuração do roteador para a ViewSet de Booking
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

# Atualizar urls.py
urlpatterns = [
    # Administração
    path('admin/', admin.site.urls),

    # Rotas do aplicativo "restaurant"
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    # Autenticação com Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # Endpoints do menu com o prefixo 'api/'
    path('api/menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    path('api/menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),

    # Mensagem protegida por autenticação
    path('message/', views.msg, name='message'),

    path('api-token-auth/', obtain_auth_token)
]
