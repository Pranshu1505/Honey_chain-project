"""QR Code service"""
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import json


class QRCodeService:
    """Generate and manage QR codes for honey batches"""
    
    @staticmethod
    def generate_qr_code(batch_id: str, batch_data: dict) -> bytes:
        """Generate QR code for a honey batch"""
        qr_data = {
            'batch_id': batch_id,
            'verify_url': f'https://honeychain.example.com/verify/{batch_id}',
            'timestamp': str(json.dumps(batch_data))
        }
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(qr_data))
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to BytesIO object
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        
        return ContentFile(img_io.getvalue(), name=f'{batch_id}_qr.png')
