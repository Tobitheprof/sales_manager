from django.db import models




SIZES = (
	
	("1","SMALL"),
	("2","MEDIUM"),
	("3","LARGE"),
	("4","XL"),
	("5","2XL"),
	("6","3XL"),

)



JERSEY_TYPE = (
	
		("1", "Home Kit"),
		("2", "Away Kit"),
		("3", "Third Kit"),


)




class Order(models.Model):


	title = models.CharField(max_length=100)
	date_of_sales = models.DateTimeField()
	name_of_customer = models.CharField(max_length=300)
	jersey_ordered = models.CharField(max_length=500)
	jersey_type = models.CharField(max_length=200, choices=JERSEY_TYPE)
	jersey_size = models.CharField(max_length=200, choices=SIZES)
	address = models.CharField(max_length=300, null=True)
	customized = models.BooleanField(default=False, blank=True)
	name_on_jersey = models.CharField(max_length=300, blank=True, help_text="Only fill this field if the customer ordered a cusromized jersey")
	number_on_jersey = models.CharField(max_length=200, blank=True, help_text="Only fill this field if the customer ordered a customized jersey")
	amount_paid = models.IntegerField()
	payment_evidence = models.FileField(upload_to="Payment Evidences")
	date_paid = models.DateField(null=True)
	order_completed = models.BooleanField(null=True)



	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Jersey Order"
		verbose_name_plural = "Jersey Orders"



# Create your models here.
