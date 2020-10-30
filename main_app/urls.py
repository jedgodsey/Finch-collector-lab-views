from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # client routes
    path('clients/', views.client_index, name='clients'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients/add', views.add_client, name='add_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/edit/', views.edit_client, name='edit_client'),
    # claim routes
    path('claims/', views.claim_index, name='claims'),
    path('claims/<int:claim_id>/', views.claim_detail, name='claim_detail'),
    path('claims/add', views.add_claim, name='add_claim'),
    path('claims/<int:claim_id>/delete', views.delete_claim, name='delete_claim'),
    path('claims/<int:claim_id>/edit', views.edit_claim, name='edit_claim'),
]
