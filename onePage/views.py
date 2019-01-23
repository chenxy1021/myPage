from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .tasks import *
import random

# Create your views here.


def index(req):
    mySkills = MySkill.objects.all().order_by('-id')[0:6]
    myProjects = MyProject.objects.all().order_by('-id')[0:3]
    myBlogs = Blog.objects.all().order_by('b_reads')[:3]
    return render(req,'index.html',locals())

def skills(req):
    mySkills = MySkill.objects.all().order_by('-id')

    return render(req, 'skills.html', locals())


def contact(req):
    if req.method == 'GET':
        return render(req,'contact.html')
    else:
        params = req.POST
        name = params.get('name')
        email = params.get('email')
        title = params.get('title')
        message = params.get('message')
        Contact.objects.create(
            m_name=name,
            m_email=email,
            m_title=title,
            m_message=message
        )
        send_user_email.delay(name=name,email=email)
        send_mine_email.delay(name=name,email=email,m_title=title,m_sessage=message)
        return render(req,'email.html')



def blogHome(req):
    if req.method == 'POST':
        params = req.POST
        search = params.get('search')
        articles = Blog.objects.filter(b_title__icontains=search).order_by('-b_created_time')
        page_num = req.GET.get("page")
        paginator = Paginator(articles, 6)

        try:
            page = paginator.page(page_num)
            # 把page对象里的数据 我们读取出来， 然后返回给前端，（前端也需要有个页面）
            result = page.object_list
        except:
            result = []
    else:
        articles = Blog.objects.all().order_by('-b_created_time')
        page_num = req.GET.get("page")
        paginator = Paginator(articles, 6)

        try:
            page = paginator.page(page_num)
            # 把page对象里的数据 我们读取出来， 然后返回给前端，（前端也需要有个页面）
            result = page.object_list
        except:
            result = []

    categorys = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')
    reads = Blog.objects.all().order_by('-b_reads')[0:5]

    return render(req,'blog/blogHome.html',locals())

def blogDetails(req,b_id):
    article = Blog.objects.get(id=b_id)
    article.b_reads += 1
    article.save()
    reads = Blog.objects.all().order_by('-b_reads')[0:5]
    categorys = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')
    if article.comments_set.all():
        comments = article.comments_set.all()
    else:
        pass
    return render(req,'blog/blogDetails.html',locals())


def projectHome(req):
    myProjects = MyProject.objects.all().order_by('-id')

    return render(req,'myProject/myProject.html',locals())


def projectDetails(req,p_id):
    project = MyProject.objects.get(id=p_id)
    projectImages = project.projectimage_set.all()

    return render(req,'myProject/projectDetails.html',locals())

def comment(req,b_id):
    params = req.GET
    c_context = params.get('c_context')
    c_name = params.get('c_name')
    c_email = params.get('c_email')
    Comments.objects.create(
        c_name = c_name,
        c_context = c_context,
        c_email = c_email,
        c_blog_id=b_id,
        c_img='author-image- (%d)'%random.randint(1,21) + '.png',
    )
    reponse = redirect('p:blogDetails',b_id)
    return reponse

def category(req,c_id):
    articles = Blog.objects.filter(b_category_id=c_id).order_by('-b_created_time')
    categorys = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')
    reads = Blog.objects.all().order_by('b_reads')[0:5]
    page_num = req.GET.get("page")
    paginator = Paginator(articles, 6)

    try:
        page = paginator.page(page_num)
        # 把page对象里的数据 我们读取出来， 然后返回给前端，（前端也需要有个页面）
        result = page.object_list
    except:
        result = []
    return render(req,'blog/blogHome.html',locals())

def tags(req,t_id):
    tag = Tag.objects.get(id=t_id)
    articles = tag.blog_set.all().order_by('-b_created_time')
    categorys = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')
    reads = Blog.objects.all().order_by('b_reads')[0:5]
    page_num = req.GET.get("page")
    paginator = Paginator(articles, 6)

    try:
        page = paginator.page(page_num)
        # 把page对象里的数据 我们读取出来， 然后返回给前端，（前端也需要有个页面）
        result = page.object_list
    except:
        result = []
    return render(req,'blog/blogHome.html',locals())





