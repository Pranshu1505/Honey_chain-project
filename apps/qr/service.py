"""QR Code service"""
import qrcode
import base64
from io import BytesIO
import json


class QRCodeService:
    """Generate and manage QR codes for honey batches"""

    @staticmethod
    def generate_qr_code_base64(batch_id: str, batch_data: dict) -> str:
        """Generate QR code for a honey batch and return as base64 data URI"""
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

        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)

        encoded = base64.b64encode(img_io.getvalue()).decode('utf-8')
        return f'data:image/png;base64,{encoded}'