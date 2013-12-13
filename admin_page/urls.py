from django.conf.urls import patterns, url
from admin_page import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name='main_page'),
    


    url(r'^addproduct$', views.add_product, name = 'add_product'),
    url(r'^productlist$', views.product_list, name = 'product_list'),
    url(r'^product/(\d+)$', views.product_page, name = 'product_page'),

    url(r'^addrecipy', views.add_recipy, name = 'add_recipy'),
    url(r'^articlelist$', views.news_list, name = 'article_list'),
    url(r'^article/(\d+)$', views.recipy_news_page, name = 'article_page'),

    url(r'^recipylist/$', views.recipy_list, name = 'recipy_list'),
    url(r'^recipy/(\d+)/$', views.recipy_news_page, name = 'recipy_page'),


    
    url(r'^listallorders$', views.list_all_orders, name = 'list_all_orders'),
    url(r'^orderpage/(\d+)$', views.order_page, name = "order_page"),

    url(r'^messages$', views.messages, name = 'messages'),
    url(r'^message/(\d+)$', views.message, name = 'message'),

    url(r'^login', 'django.contrib.auth.views.login', name = 'login'),
    url(r'^logout$',views.logout_page , name='logout')
)
