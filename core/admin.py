from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
	list_display = ['title', 'date_of_sales', 'amount_paid', 'address', 'customized', 'order_completed']

admin.site.register(Order, OrderAdmin)



# Register your models here.
