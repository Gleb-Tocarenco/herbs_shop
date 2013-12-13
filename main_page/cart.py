from models import Order, OrderDetails
def get_cart_items(request):
	return request.session.get('cart', [])

def add_to_cart(request):
	postdata = request.POST.copy()
	product = postdata.get('product','')
	quantity = postdata.get('quantity','1')
	price = postdata.get('price','').split(".")[0]
	items_in_cart = False
	cart_items = get_cart_items(request)

	for cart_item in cart_items:
		if product == cart_item['product']:
			cart_item['quantity'] += int(quantity)
			cart_item['total'] = int(price) * int(quantity)
			items_in_cart = True


	
	request.session['cart'] = cart_items
	
	if not items_in_cart:
		cart = get_cart_items(request)
		cart.append({'product': product, 'quantity': int(quantity), 'total' : int(price)*int(quantity), 'price' : price}, )
		request.session['cart'] = cart
def cart_total(request):
	cart = get_cart_items(request)
	total = 0
	for item in cart:
		total += int(item['total'])

	return total

def update_cart(request):
	cart_items = get_cart_items(request)
	postdata = request.POST.copy()

	product = postdata.get('product', '')
	quantity = postdata.get('quantity','')

	for cart_item in cart_items:
		if product == cart_item['product']:
			cart_item['quantity'] = int(quantity)
			cart_item['total'] = int(quantity) * int(cart_item['price'])	
	request.session['cart'] = cart_items

def remove_from_cart(request):
	cart_items = get_cart_items(request)
	postdata = request.POST.copy()

	product = postdata.get('product', '')
	for cart_item in cart_items[:]:
		if cart_item['product'] == product:
			cart_items.remove(cart_item)

	request.session['cart'] = cart_items

def save_order_to_db(request, instance):
	
 	cart_items = get_cart_items(request)
 	for cart_item in cart_items:

 		order = Order(product = cart_item['product'], quantity = cart_item['quantity'], order_details_id = instance)
 		order.save()
 	request.session.clear()