# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from models import Product, Article, OrderForm, OrderdetailsForm, OrderDetails, Order, ContactsForm

from cart import add_to_cart, remove_from_cart, update_cart, save_order_to_db, get_cart_items, cart_total

import forms
import models
import datetime
def main_page(request):
	pass

def news_list(request):
	news = Article.objects.filter(article_type="news")
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request,"frontend/news_list.html",locals())

def news_page(request, news_id):
	news = Article.objects.get(id = news_id)
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, 'frontend/news_page.html', locals())


def special_offers(request):
	special_offers = Product.objects.filter(discount = True)
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, 'frontend/special_offers.html', locals())


def contact_page(request):
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	
	if request.method == "POST" :
		postdata = request.POST.copy()
		form = ContactsForm(postdata)
		if form.is_valid():
			form.save()
			form = ContactsForm()
			return render(request, "frontend/contact.html", {"form" : form, "message" : "Thank you"})
	else:
		form = ContactsForm()
	
		

	return render(request, "frontend/contact.html", {"categories":categories, "form" : form})


def recipy_page(request,r_id):
	recipy = Article.objects.get(id = r_id)
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, "frontend/recipy_page.html", locals())

def recipies_list(request):
	recipies = Article.objects.filter(article_type = "recipies")
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, "frontend/recipies.html", locals())

def product_list_front(request):
	products = Product.objects.all()
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, "frontend/products.html", {"products" : products, "categories" : categories })

def product_list_by_category(request, category):
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	products = Product.objects.filter(category_name = category)
	if request.method == "POST":
		postdata = request.POST.copy()
		form = OrderForm(postdata)
		if form.is_valid():
			add_to_cart(request)
			return render(request, "frontend/products_by_category.html", locals())
			
	else:
		
		return render(request, "frontend/products_by_category.html", locals())

def product_page(request, product_name):
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	if request.method == "POST":
		postdata = request.POST.copy()
		form = OrderForm(postdata)
		if form.is_valid():
			add_to_cart(request)
			return redirect('show_cart_page')
	else:
		product = Product.objects.get(product_name = product_name)
		form = OrderForm()
	return render(request, "frontend/productpage.html", locals() )

def show_cart_page(request):
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Update':
			update_cart(request)
			orders = request.session.get('cart', '')
			cart_sum = cart_total(request)
			return render(request, "frontend/shoppingcart.html", locals())
		if postdata['submit'] == 'Delete':
			remove_from_cart(request)

	orders = request.session.get('cart', '')
	cart_sum = cart_total(request)
	return render(request, "frontend/shoppingcart.html", locals())

def checkout(request):
	if request.method == "POST":
		postdata = request.POST.copy()
		form = OrderdetailsForm(postdata)
		if form.is_valid():
			instance = form.save()
			cart_items = get_cart_items(request)
			for cart_item in cart_items:
				product = Product.objects.get(product_name = cart_item['product'])
 				order = Order(product = product, quantity = cart_item['quantity'], order_details_id = instance)
 				order.save()
 				request.session.clear()
			return redirect('thanks')
		
	else:
		form = OrderdetailsForm()
	categories = Product.objects.values_list('category_name', flat = True ).distinct()
	return render(request, 'frontend/checkout.html', {'categories' : categories, 'form' : form} )

def thanks(request):
	return render(request, 'frontend/thankyou.html')

