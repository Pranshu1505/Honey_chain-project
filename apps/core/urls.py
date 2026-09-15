from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('features/', views.FeaturesPageView.as_view(), name='features'),
    path('dashboard/', views.DashboardPageView.as_view(), name='dashboard'),
    path('contact/', views.contact_page_view, name='contact'),
    path('faq/', views.FaqPageView.as_view(), name='faq'),
    path('terms/', views.TermsPageView.as_view(), name='terms'),
    path('privacy/', views.PrivacyPageView.as_view(), name='privacy'),
    path('api/status/', views.api_status, name='api_status'),
]
