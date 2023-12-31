# Generated by Django 4.2.3 on 2023-07-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_of_sales', models.DateTimeField()),
                ('name_of_customer', models.CharField(max_length=300)),
                ('jersey_ordered', models.CharField(max_length=500)),
                ('jersey_type', models.CharField(choices=[('1', 'Home Kit'), ('2', 'Away Kit'), ('3', 'Third Kit')], max_length=200)),
                ('jersey_size', models.CharField(choices=[('1', 'SMALL'), ('2', 'MEDIUM'), ('3', 'LARGE'), ('4', 'XL'), ('5', '2XL'), ('6', '3XL')], max_length=200)),
                ('customer_address', models.CharField(max_length=300)),
                ('customized', models.BooleanField(blank=True, default=False)),
                ('name_on_jersey', models.CharField(blank=True, help_text='Only fill this field if the customer ordered a cusromized jersey', max_length=300)),
                ('number_on_jersey', models.CharField(blank=True, help_text='Only fill this field if the customer ordered a customized jersey', max_length=200)),
                ('amount_paid', models.IntegerField()),
                ('payment_evidence', models.FileField(upload_to='Payment Evidences')),
            ],
            options={
                'verbose_name': 'Jersey Order',
                'verbose_name_plural': 'Jersey Orders',
            },
        ),
    ]
