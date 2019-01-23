from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index$',index,name='index'),
    url(r'^skills$',skills,name='skills'),
    url(r'^contact$',contact,name='contact'),
    url(r'^blogHome$',blogHome,name='blogHome'),
    url(r'^projectHome$',projectHome,name='projectHome'),
    url(r'^projectDetails/(\d+)$',projectDetails,name='projectDetails'),
    url(r'^blogDetails/(\d+)$',blogDetails,name='blogDetails'),
    url(r'^comment/(\d+)$',comment,name='comment'),
    url(r'^category/(\d+)$',category,name='category'),
    url(r'^tags/(\d+)$',tags,name='tags'),
]