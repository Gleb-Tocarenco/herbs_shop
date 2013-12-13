from django.contrib import admin
import models

admin.site.register(models.Article)
admin.site.register(models.Product)
admin.site.register(models.OrderDetails)
admin.site.register(models.Order)