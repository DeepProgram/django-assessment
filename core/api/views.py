from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import RegisterUserSerializer, UserSerializer
from .utils import create_jwt_token, verify_jwt_token, TokenStatus

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = create_jwt_token(user.id)
            return Response({
                'user_id': user.id,
                "token": token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StatusView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return Response({'error': 'Authorization token required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            bearer_token = auth_header.split(" ")[1]
        except Exception:
            return Response({'error': 'Authorization token format is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token_data = verify_jwt_token(bearer_token)

        if token_data.get("status") == TokenStatus.EXPIRED:
            return Response({'error': 'Authorization token is expired'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if token_data.get("status") == TokenStatus.INVALID:
            return Response({'error': 'Authorization token is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_id = token_data.get("payload").get('user_id')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)