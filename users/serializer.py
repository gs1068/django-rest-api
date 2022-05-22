# APIモードでのデータ入出力を扱う。モデルでの橋渡しを行う
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        # Jsonでは返さない
        extra_kwargs = {
            'password': {'write_only': True}
        }
