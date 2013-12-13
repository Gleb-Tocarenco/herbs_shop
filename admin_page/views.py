# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from main_page.models import ArticleForm, ProductForm, OrderDetails, Article, Product, Order, Contacts
from django.utils import timezone
from django.template import RequestContext, loader
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required
def main_page(request):
	pass

@login_required
def list_all_orders(request):
	orders = OrderDetails.objects.all().order_by('-order_date')
	return render(request, 'backend/orderlist.html', {"orders" : orders})

@login_required	
def order_page(request, order_id):
	if request.method == "POST":
		order_details = OrderDetails.objects.get(id = order_id)
		order_details.served = True 
		order_details.save()
		return redirect('list_all_orders')

	order_details = OrderDetails.objects.get(id = order_id)
	order = Order.objects.filter(order_details_id = order_details)
	return render(request, 'backend/orderpage.html', {"order_details": order_details, "order": order})




@login_required
def add_recipy(request):
	if request.method == 'POST':
		r_id = request.session.get('r_id', '')

		if r_id:
			recipy = Article.objects.get(id = r_id)
			form = ArticleForm(request.POST, instance = recipy)
			del request.session['r_id']
		else:
			form = ArticleForm(request.POST)


		
		if form.is_valid():
			
			recipy_instance = form.save()


			if recipy_instance.article_type == 'news':
				return redirect('article_list')
			else:
				return redirect('recipy_list')
	else:
		r_id = request.session.get('r_id', '')
		if r_id:
			recipy = Article.objects.get(id = r_id)
			form = ArticleForm(instance = recipy)
			
			
		else:
			form = ArticleForm()
	return render_to_response('backend/newrecipy.html', {'form': form},context_instance=RequestContext(request))

@login_required
def recipy_list(request):
	recipies = Article.objects.filter(article_type = 'recipies')
	return render(request, 'backend/recipylist.html', {"recipies": recipies})

@login_required
def recipy_news_page(request, r_id):
	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata['submit'] == 'edit':
			request.session['r_id'] = r_id
			return redirect('add_recipy')
		elif postdata['submit'] == 'delete':
			recipy = Article.objects.get(id = r_id)
			recipy.delete()
			return redirect('recipy_list')

			
	else:
		recipy = Article.objects.get(id = r_id)
	return render(request, 'backend/recipypage.html', {"recipy": recipy})


@login_required
def news_list(request):
	news = Article.objects.filter(article_type = 'news')
	return render(request, 'backend/newslist.html', {"news": news})



@login_required
def product_list(request):
	products = Product.objects.all()
	return render(request, 'backend/productlist.html', {"products": products})

@login_required
def add_product(request):
	if request.method == "POST":
		p_id = request.session.get('p_id', '')
		if p_id:

			instance = get_object_or_404(Product, id=p_id )
			form  = ProductForm(request.POST, request.FILES, instance = instance)
			del request.session['p_id']
		else:
			form = ProductForm(request.POST, request.FILES)
		if form.is_valid():

			form.save()
			
			return redirect('product_list')
	else:

		p_id = request.session.get('p_id', '')

		if p_id:
			product = Product.objects.get(id = p_id)
			form = ProductForm(instance = product)
			
			
			
		else:
		
			form = ProductForm()
	return render(request, 'backend/newproduct.html', {"form": form})

@login_required		
def product_page(request, p_id):
	product = Product.objects.get(id = p_id)
	if request.method == "POST":	
		postdata = request.POST.copy()
			
		if postdata['submit'] == 'edit':
				
			request.session['p_id'] = p_id
			return redirect('add_product')

		if postdata['submit'] == 'delete':
			product.delete()
			return redirect('product_list')
	else:
		return render(request, "backend/product_page.html", {"product" : product})		
	
@login_required
def messages(request):
	messages = Contacts.objects.all().order_by('date')
	return render(request, "backend/messages.html", locals() )


@login_required
def message(request, m_id):
	message = Contacts.objects.get(id = m_id)
	return render(request, "backend/message.html", locals())


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return redirect("list_all_orders")
    else:
        # Show an error page
        return redirect("")

def logout_page(request):
	auth.logout(request)
	return redirect('login')