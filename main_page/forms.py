import django.forms

POST_TYPE_CHOICES = ("recipies", "news")
from django import forms
class ProductForm(forms.Form):
	product_name = forms.CharField()
	
	price = forms.IntegerField()
	avalability = forms.BooleanField()
	discount = forms.BooleanField()
	discount_amt = forms.IntegerField()
	

class ArticleForm(forms.Form):
	title = forms.CharField()
	post = forms.CharField(widget=forms.Textarea)
	article_type = forms.CharField(max_length=3,widget=forms.Select(choices=POST_TYPE_CHOICES ))

class OrderDetailsForm(forms.Form):
	client_name  = forms.CharField()
	client_phone = forms.CharField()
	client_email = forms.EmailField()
	subuscribed = forms.BooleanField(widget=forms.CheckboxInput)