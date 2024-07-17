from .serializers import *
from .models import *
from .permissions import *
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication
from django.core.mail import send_mail
from django.conf import settings


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission] 

    def get_queryset(self):
        return Course.objects.all()


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [CustomPermission]


class SendEmailView(APIView):
    def post(self, request: Request):

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_users = []
        for user in users:
            email_users.append(user.email)
        email_users.append("saydullayevsaidanasxon@gmail.com")

        send_mail(
            serializer.validated_data.get("subject"),
            serializer.validated_data.get("message"),
            settings.EMAIL_HOST_USER,
            email_users,
            fail_silently=False,
        )
        return Response({"message": "Email sent successfully."})
    
class LikeView(APIView):
    def get(self, request, pk):
        likes = LikeLesson.objects.filter(like_or_dislike=True, dars_like_id=pk).count()
        dislikes = LikeLesson.objects.filter(like_or_dislike=False, dars_like_id=pk).count()
        
     
        return Response({
            "likes": likes,
            "dislikes": dislikes,
        
        })

class LikeLessonCreateView(APIView):
    def post(self, request):
        try:
            likes_or_dislikes = LikeLesson.objects.filter(author_id=request.data.get("user"))
            for l_or_d in likes_or_dislikes:
                l_or_d.delete()
        except:
            pass

        serializer = LikeLessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeLessonSerializer(like_or_dislike).data)