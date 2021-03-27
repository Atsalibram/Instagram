from django.conf.urls import url
from . import views

urlpatterns=[
  url('^$',views.homepage,name='homePage'),
  url(r'^post',views.post,name='post'),
  url(r'^profile$',views.profile,name='profile'),
  url(r'^user/(?P<username>\w+)',views.showprofile,name ='showprofile'),
  url(r'^ search/',views.search, name='search'),
  url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
  
]