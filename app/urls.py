from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'app'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('courses', views.CourseViewSet, basename='courses')
router.register('lessons', views.LessonViewSet, basename='lessons')
router.register('videos', views.VideoViewSet, basename='videos')
router.register('reviews', views.ReviewViewSet, basename='reviews')


urlpatterns = [
    path('', include(router.urls)),
    path('send/message/email', views.SendEmailView.as_view()),
    path('lesson/<int:pk>/like/', views.LikeView.as_view()),
    path('lesson/like/create/', views.LikeLessonCreateView.as_view()),
]