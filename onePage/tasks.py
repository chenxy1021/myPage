from celery import task
from django.conf import settings
from django.core.mail import send_mail

# 发送邮件
@task
def send_user_email(name,email):
	title = "我已收到您的邮件"
	msg = "%s,您好,我已收到您的邮件,在看到之后会第一时间回复您"%name
	receivers = [
    	email,
	]
	email_from = settings.DEFAULT_FROM_EMAIL
	send_mail(title, msg, email_from, receivers)

@task
def send_mine_email(name,email,m_title,m_sessage):
    title = '%s:'%name + m_title
    msg = "来自:%s\n内容为:%s" %(email,m_sessage)
    receivers = [
        '709101158@qq.com',
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title, msg, email_from, receivers)