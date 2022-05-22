from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
# Create your views here.

# ViewSetはCRUDを実装を肩代わりしてくれる
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
