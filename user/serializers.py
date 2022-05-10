from user.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "phone",
            "country",
            "company",
            "role",
            "bio",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.get("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
