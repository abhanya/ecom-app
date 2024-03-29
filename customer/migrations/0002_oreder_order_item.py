# Generated by Django 4.1.1 on 2023-03-31 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
        ('hcart', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oreder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('state', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=6)),
                ('total_price', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('tracking_no', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcart.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('oreder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.oreder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcart.seller')),
            ],
        ),
    ]
