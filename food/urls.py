from django.conf.urls import url
from . import views

urlpatterns = [
    # main URL
    url(r'^$', views.foodpost_list, name='foodpost_list'),

    # Filter url
    url(r'^(?P<pk>\d+)/$', views.foodpost_detail, name='foodpost_detail'),

    # Add Comment
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),

    # url(r'^post/new/$', views.new_food_entry, name='new_food_entry'),
]
