from django.urls import path
from .views import *


urlpatterns = [
    path("profile/", ProfileData.as_view()),
    path("skills/", SkillListAPIView.as_view()),
    path("about/", AboutCreateAPIView.as_view()),
    # path("category/", get_category_data),
    # path("posts/", get_post_data),
    # path("service/", get_service_data),
    path("post/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view()),
    path("portfolio/", get_portfolio_data),
    path('blog/', BlogCreateAPIView.as_view()),
    path('blog/<int:pk>/', BlogUpdateAPIView.as_view()),
    path('blogs/', BlogListAPIView.as_view()),
    path('service/', ServiceListAPIView.as_view())
]