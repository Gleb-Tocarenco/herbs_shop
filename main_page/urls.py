from django.conf.urls import patterns, url
from main_page import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name='main_page'),
    url(r'^news$', views.news_list, name='news'),
    url(r'^productlist/(\w+)$', views.product_list_by_category, name = 'product_list_by_category'),
    url(r'^productlist/$', views.product_list_front, name = 'product_list_front'),
    url(r'^product/(\w+)$', views.product_page, name = 'product_page_front'),
    url(r'^specialoffers$', views.special_offers, name = "special_offers"),
    url(r'^news$', views.news_list, name = 'news_list'),
    url(r'^recipies$', views.recipies_list, name = 'recipies'),
    url(r'^recipiy/(\d+)$', views.recipy_page, name = 'front_recipy_page'),
    url(r'^news/(\d+)$', views.news_page, name = 'news_page'),

    url(r'^cart$', views.show_cart_page, name = 'show_cart_page'),
    url(r'^checkout$' , views.checkout, name = 'checkout'),
    url(r'^thankyou$', views.thanks, name = 'thanks'),	
    url(r'^contacts$', views.contact_page, name = 'contacts')

)
