from django.contrib import admin
from .models import *

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('full_name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('experience',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'id',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','id')
# @admin.site.register(Skill)
# @admin.site.register(About)
# @admin.site.register(Category)
# @admin.site.register(Post)
# @admin.site.register(Service)
# @admin.site.register(Portfolio)
# class MemberAdmin(admin.ModelAdmin):
#     ...


