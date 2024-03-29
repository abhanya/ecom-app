# Generated by Django 4.1.1 on 2023-03-10 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hcart', '0001_initial'),
        ('seller', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcart.customer')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_quantity', models.IntegerField(default='1')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcart.customer')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
