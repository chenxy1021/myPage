
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
# Create your models here.

class MySkill(models.Model):
    s_name = models.CharField(
        verbose_name='技能名称',
        max_length=20,
    )
    s_describe = models.CharField(
        verbose_name='技能描述',
        max_length=150,
    )
    class Meta:
        db_table = '技能'
        verbose_name = '技能'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.s_name


class MyProject(models.Model):
    p_person = models.CharField(
        verbose_name='项目人员',
        max_length=100,
    )
    p_datetime = models.DateField(
        verbose_name='项目时间'
    )
    p_skills = models.CharField(
        max_length=150,
        verbose_name='项目使用技能'
    )
    p_name = models.CharField(
        verbose_name='项目名称',
        max_length=20,
    )
    p_describe = models.CharField(
        verbose_name='项目描述',
        max_length=240,
    )
    p_icon = models.ImageField(
        verbose_name='项目图片',
        upload_to=r'img/portfolio/%Y/%m/%d'
    )
    class Meta:
        db_table = '项目'
        verbose_name = '项目'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.p_name


class ProjectImage(models.Model):
    i_image = models.ImageField(
        verbose_name='图片',
        upload_to=r'img/portfolio/%Y/%m/%d'
    )
    i_describe = models.CharField(
        verbose_name='图片描述',
        max_length=50,
        null=True
    )
    myProject = models.ForeignKey(
        MyProject,
        verbose_name='项目'
    )
    class Meta:
        db_table = '项目图片'
        verbose_name = '项目图片'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.i_describe

class Contact(models.Model):
    m_name = models.CharField(
        verbose_name='姓名',
        max_length=30,
    )
    m_email = models.EmailField(
        verbose_name='邮箱',
        max_length=100,
    )
    m_title = models.CharField(
        verbose_name='标题',
        max_length=120,
    )
    m_message = models.TextField(
        verbose_name='正文',
        max_length=255,
    )
    class Meta:
        db_table = '联系人'
        verbose_name = '联系人',
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.m_email

# -------------------blog---------------------------------------

class Category(models.Model):
    c_name = models.CharField(
        verbose_name='文章分类',
        max_length=20,
    )
    class Meta:
        db_table = '文章分类'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.c_name

class Tag(models.Model):
    t_name = models.CharField(
        verbose_name='文章标签',
        max_length=20,
    )
    class Meta:
        db_table = '文章标签'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.t_name

class Blog(models.Model):
    b_title = models.CharField(
        max_length=50,
        verbose_name='文章标题'
    )
    b_excerpt = models.TextField(
        verbose_name='文章摘要',
        max_length=200,
    )
    b_category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='分类',
        null=True,
        blank=True,
    )
    b_tag = models.ManyToManyField(
        Tag,
        verbose_name='标签',
    )
    b_img = models.ImageField(
        verbose_name='文章图片',
        upload_to=r'img/blog/%Y/%m/%d',
        null=True,
    )
    b_context = UEditorField(
        verbose_name='内容',
        width=800, height=500,
        toolbars="full",
        imagePath="upimg/",
        filePath="upfile/",
        upload_settings={
            "imageMaxSize": 1204000
        },
        settings={},
        command=None,
        blank=True
    )
    b_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='作者'
    )
    b_reads = models.PositiveIntegerField(
        default=0,
        verbose_name='阅读量'
    )
    b_created_time= models.DateTimeField(
        auto_now_add=True,
        verbose_name='发表时间'
    )
    b_modified_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间',
    )
    class Meta:
        db_table = '文章'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.b_title

class Comments(models.Model):
    c_name = models.CharField(
        verbose_name='评论人',
        max_length=10,
    )
    c_img = models.CharField(
        verbose_name='评论头像',
        max_length=50,
    )
    c_email = models.EmailField(
        max_length=100,
        verbose_name='评论人邮箱'
    )
    c_context = models.TextField(
        max_length=240,
        verbose_name='评论内容'
    )
    c_create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='评论时间'
    )
    c_blog = models.ForeignKey(
        Blog,
        verbose_name='文章'
    )
    class Meta:
        db_table = '文章评论'
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.c_name