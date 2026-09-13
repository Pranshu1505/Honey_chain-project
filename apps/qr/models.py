"""QR Code models"""
from django.db import models
from apps.batch.models import HoneyBatch


class QRCode(models.Model):
    batch = models.OneToOneField(HoneyBatch, on_delete=models.CASCADE, related_name='qr_code')
    code_data = models.CharField(max_length=500)
    qr_image = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
    scans = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'qr_codes'
    
    def __str__(self):
        return f"QR for batch {self.batch.batch_id}"
