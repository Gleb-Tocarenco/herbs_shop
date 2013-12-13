from django.db import models
from django.forms import ModelForm, HiddenInput, TextInput, Textarea

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length = 50)
	category_name = models.CharField(max_length = 50)
	price = models.FloatField(unique = False )
	description = models.TextField(null=True, blank=True)
	
	avalability = models.BooleanField()
	discount = models.BooleanField()
	discount_amt = models.FloatField()
	image = models.ImageField(upload_to="images/",blank = True)
	
	def __unicode__(self):
		return self.product_name

	def price_discount(self):
		if self.discount:
			return self.price - self.discount_amt
		else:
			return self.price


	

class Order(models.Model):
	product = models.ForeignKey('Product', unique = False)
	quantity = models.FloatField()
	order_details_id = models.ForeignKey('OrderDetails', unique = False)
	
	date_added = models.DateTimeField(auto_now_add = True)

	def total(self):
		return self.quantity * self.product.price

	def product_name(self):
		return self.product.product_name

	def price(self):
		return self.product.price

	def augument_quantity(self, quantity):
		self.quantity += int(quantity)
	



class OrderDetails(models.Model):
	client_name = models.CharField(max_length = 100)
	client_phone = models.CharField(max_length = 100)
	client_email = models.EmailField(max_length = 150)
	served = models.BooleanField(default = False)
	order_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.client_name


		
		
class Article(models.Model):
	article_types = (('recipies','recipies'),('news', 'news'))
	title = models.CharField(max_length = 100)
	post = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	article_type = models.CharField(choices = article_types,max_length=10)

	def __unicode__(self):
		return self.title

class Contacts(models.Model):
	name = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	title = models.CharField(max_length = 100)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.name
		
		

class ProductForm(ModelForm):
	class Meta:
		model = Product

class ArticleForm(ModelForm):
	class Meta:
		model = Article

class OrderForm(ModelForm):

	class Meta:
		model = Order
		fields = ['quantity']
		widgets = { 'quantity' : TextInput(attrs = {'size' : 2 	})	}

class OrderdetailsForm(ModelForm):
	class Meta:
		model = OrderDetails
		fields = ['client_name', 'client_phone', 'client_email']
			

class ContactsForm(ModelForm):
	class Meta:
		model = Contacts
		exclude = ['date']
		widgets = {'message' : Textarea(attrs = {'cols' : 50, 'rows' : 20})}
			
		