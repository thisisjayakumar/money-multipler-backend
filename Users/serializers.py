from rest_framework import serializers
from .models import User
import random

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 'name', 'level', 'occupation', 'age', 'withdraw_method',
            'withdraw_account_id', 'account_balance', 'bank_no', 'ufsc'
        ]
        read_only_fields = ['user_id'] 

    def validate(self, data):
        if data.get('withdraw_method') == 'BANK':
            if not data.get('bank_no'):
                raise serializers.ValidationError("Bank number is required when withdrawal method is 'BANK'.")
            if not data.get('ufsc'):
                raise serializers.ValidationError("UFSC code is required when withdrawal method is 'BANK'.")
        return data

    def create(self, validated_data):
        user_id = str(random.randint(100000, 999999))
        validated_data['user_id'] = user_id
        return super().create(validated_data)
