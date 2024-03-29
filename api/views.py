from django.shortcuts import render
from app.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissons import *

# functions based profile api
@api_view(['GET', 'POST'])
def get_profile_data(request):
    if request.method == 'POST':
        print(request.data)
        print(type(request.data))

    profile = Profile.objects.first()
    data = {
        'image': str(profile.image),
        'full_name': profile.full_name,
        'bio': profile.bio
    }

    return Response(data=data)


@api_view(['GET'])
def get_skills_data(request):
    skills = Skill.objects.all()
    # serializer code

    serializer = SkillSerializer(instance=skills, many=True)

    return Response(data=serializer.data)

    # python code
    # a = []

    # for i in skills:
    #     b = {
    #         'title': i.title,
    #         'percentage': i.percentage,
    #         'order': i.order
    #     }
    #     a.append(b)
    # print(a)
    # return Response(data=a, status=200)

# class based profile api

class ProfileData(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        profile = Profile.objects.first()
        data = {
            'image': str(profile.image),
            'full_name': profile.full_name,
            'bio': profile.bio
        }

        return Response(data=data)
    
    def post(self, request, format=None):
        print(request.data)
        return Response(status=200)



# About ----------------------------------------------------------------
@api_view()
def get_about_data(request, format=None):
    about = About.objects.first()
    data = {
        'experience': about.experience,
        "total_projects": about.total_projects,
        'total_users': about.total_users,
        'salary': about.salary
    }

    return Response(data=data)


# Category ----------------------------------------------------------------
# class CategorySerializer(ModelSerializer):

#     class Meta:
#         model = Category
#         fields = ('name',)


# def get_category_data(request,  format=None):
#     category = Category.objects.all()

#     # serializer = CategorySerializer(instance=category, many=True)
#     a = []
#     for i in category:
#         data = {
#             'name' : i.name,
#         }
#         a.append(data)
#     print(a)
#     return Response(data=a)


# POST ----------------------------------------------------------------

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('author','image', 'description', 'title', 'count_views')


@api_view()
def get_post_data(request):
    post = Post.objects.all()

    serializer = PostSerializer(instance=post, many=True)

    return Response(data=serializer.data)

# Service ----------------------------------------------------------------
class ServiceSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = ('title','icon', 'description')


@api_view()
def get_service_data(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(instance=service, many=True)
    return Response(data=serializer.data)




# Portfolios ----------------------------------------------------------------
class PortfoliosSerializer(ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'image', 'link', 'used_tools', 'category', 'complated_at')


@api_view()
def get_portfolio_data(request):
    portfolio = Portfolio.objects.all()
    serializer = PortfoliosSerializer(instance=portfolio, many=True)
    return Response(data=serializer.data)

# ----------------------------------------------------------------


class SkillListAPIView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]


class AboutCreateAPIView(CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogAPIView(APIView):
    def post(self, request, format=None):
        serializer = BlogCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        
        return Response(status=201)
    


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('category','author')
    permission_classes = [IsAuthenticated]
    search_fields = ('title',)
    serializer_class = BlogListSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(author=self.request.user)


class ServiceListAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [ServicePermission, IsAuthenticated]


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [PostPermission, IsAuthenticated]






