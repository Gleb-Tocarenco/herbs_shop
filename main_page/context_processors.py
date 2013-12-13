from django.conf import settings
from models  import Product

def default(request):

	return dict (
			categories = Product.objects.values_list('category_name', flat = True ).distinct()
		)