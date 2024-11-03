import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
from enum import Enum

class TokenStatus(Enum):
    VALID = "valid"
    EXPIRED = "expired"
    INVALID = "invalid"

def create_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
        'iat': datetime.now(timezone.utc)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return {
            "status": TokenStatus.VALID,
            "payload": payload
        }
    except jwt.ExpiredSignatureError:
        return {
            "status": TokenStatus.EXPIRED,
            "payload": None
        }
    except jwt.InvalidTokenError:
        return {
            "status": TokenStatus.INVALID,
            "payload": None
        }