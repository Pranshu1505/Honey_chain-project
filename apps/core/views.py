from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from apps.beekeeper.models import BeekeeperProfile
from apps.hive.models import Hive
from apps.batch.models import HoneyBatch
from apps.sensor.models import SensorData


class ContextMixin:
    """Mixin to add common context data"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_beekeepers'] = BeekeeperProfile.objects.count()
        context['total_hives'] = Hive.objects.count()
        context['total_batches'] = HoneyBatch.objects.count()
        context['total_sensors'] = SensorData.objects.count()
        context['recent_beekeepers'] = BeekeeperProfile.objects.all()[:5]
        context['recent_hives'] = Hive.objects.all()[:5]
        context['recent_batches'] = HoneyBatch.objects.all()[:5]
        return context


class HomePageView(ContextMixin, TemplateView):
    """Home page view"""
    template_name = 'home.html'


class AboutPageView(ContextMixin, TemplateView):
    """About page view"""
    template_name = 'about.html'


class FeaturesPageView(ContextMixin, TemplateView):
    """Features page view"""
    template_name = 'features.html'


class DashboardPageView(ContextMixin, TemplateView):
    """Dashboard page view"""
    template_name = 'dashboard.html'


class FaqPageView(ContextMixin, TemplateView):
    """FAQ page view"""
    template_name = 'faq.html'


class TermsPageView(ContextMixin, TemplateView):
    """Terms of service page view"""
    template_name = 'terms.html'


class PrivacyPageView(ContextMixin, TemplateView):
    """Privacy policy page view"""
    template_name = 'privacy.html'


def contact_page_view(request):
    """Contact page with form handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        # Send email
        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"From: {name} ({email})\n\n{message_text}",
                from_email='noreply@honeychain.com',
                recipient_list=['contact@honeychain.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'Failed to send message. Please try again.')
    
    context = {
        'total_beekeepers': BeekeeperProfile.objects.count(),
        'total_hives': Hive.objects.count(),
        'total_batches': HoneyBatch.objects.count(),
        'total_sensors': SensorData.objects.count(),
    }
    return render(request, 'contact.html', context)


def api_status(request):
    """API status endpoint - returns system status"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Honey Chain is running',
        'version': '1.0.0',
        'timestamp': str(timezone.now()),
    })
