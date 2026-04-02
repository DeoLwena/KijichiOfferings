from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        data['username'] = user.username
        data['email'] = user.email
        data['is_staff'] = user.is_staff

        data['groups'] = list(user.groups.values_list('name', flat=True))
        return data