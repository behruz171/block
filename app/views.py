from django.shortcuts import render
from .models import Profile, Skill, About, Category, Post, Portfolio
from django.shortcuts import get_object_or_404

def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    about = About.objects.first()
    category = Category.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        "profile": profile,
        "skills": skills,
        "about": about,
        "category": category,
        "portfolios": portfolios
        }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about-us.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            posts = posts.filter(title__icontains=search)
    
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'single-blog.html', {'post': post})
