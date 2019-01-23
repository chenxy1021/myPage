from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(MySkill)
class MySkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        's_name',
        's_describe',
    )
    ordering = ('-id',)

@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'p_name',
        'p_person',
        'p_datetime',
        'p_skills',
        'p_describe',
        'p_icon'
    )
    ordering = ('-id',)

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'i_image',
        'i_describe',
        'myProject'
    )


@admin.register(Blog)
class BlogAdim(admin.ModelAdmin):
    list_display = (
        'id',
        'b_category',
        'b_title',
        'b_reads',
        'b_user',
        'b_created_time',
        'b_modified_time',
        'b_excerpt'
    )
    list_per_page = 20
    ordering = ('-b_created_time',)
    list_display_links = (
        'id',
        'b_title',
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'c_name',
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        't_name'
    )

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'c_name',
        'c_email',
        'c_context',
        'c_create_time',
        'c_blog'
    )
    list_per_page = 20
    ordering = ('-c_create_time',)

admin.site.site_header = '酷酷的后台'
admin.site.site_title = '酷酷'
admin.site.site_url = 'http://47.101.151.17:12345/p/index'
