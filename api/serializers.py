from rest_framework.serializers import ModelSerializer, Serializer
from app.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
class SkillSerializer(ModelSerializer):
    
    class Meta:
        model = Skill
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at",)



class AboutSerializer(Serializer):
    experience = serializers.CharField()
    total_projects = serializers.IntegerField()
    total_users = serializers.IntegerField()
    salary = serializers.IntegerField()

    def validate(self, attrs):
        print(attrs)
        if attrs['salary'] < 1000:
            raise serializers.ValidationError(detail={
                'salary': '1000 sumdan kop bolishi kerak'
            }, code=400)
        if attrs['total_users'] < attrs['total_projects']:
            raise serializers.ValidationError(detail={
                'total_users':'total_user total_projects dan kam'
            }, code=400)
        
        return super().validate(attrs)

    def create(self, validated_data):
        about = About.objects.create(
            **validated_data
        )
        return about



class SkillSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    percentage = serializers.IntegerField()
    order = serializers.IntegerField()

    def create(self, validated_data):
        title = validated_data.get('title')
        percentage = validated_data.get('percentage')
        order = validated_data.get('order')
        instance = Skill.objects.create(
            title=title,
            percentage=percentage,
            order=order
        )
        return instance


class ProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    bio = serializers.CharField(max_length=200)




class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')

class BlogListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    author = AuthorSerializer()
    class Meta:
        model = Blog
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"