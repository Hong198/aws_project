from django.contrib.auth import get_user_model

from users.models import CustomUser

from rest_framework.serializers import ModelSerializer

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    class meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data.get("name")
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User(
            name=name,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
