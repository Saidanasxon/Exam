from rest_framework import serializers
from .models import * 
from .validators import validate_video_file

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        custom_user = CustomUser(user=user)
        custom_user.save()

        return user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(validators=[validate_video_file])

    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file']

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message  = serializers.CharField()  

class LikeLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeLesson
        fields = '__all__'