from .models import CustomUser, Category, News, Tour, Comment, Request ,UserProfile
from rest_framework import serializers
from django.contrib.auth import authenticate , get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'country', 'city', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            country=validated_data.get('country', ''),
            city=validated_data.get('city', ''),
            phone_number=validated_data.get('phone_number', '')
        )
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'country', 'city', 'phone_number')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")
 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'key', 'name']  

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'name', 'city', 'kind', 'time', 'price', 'discount', 'img_url', 'category', 'description']


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Используем кастомный сериализатор пользователя

    class Meta:
        model = Comment
        fields = ['id', 'message', 'rate', 'user']  # Подставьте нужные вам поля комментария


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
