# Generated by Django 5.0.4 on 2024-05-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dividens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('number_of_promotion', models.FloatField(blank=True, null=True)),
                ('price_of_promotion', models.FloatField(blank=True, null=True)),
                ('total_sum_of_promotions', models.FloatField(blank=True, null=True)),
                ('procent_of_dividends', models.FloatField(blank=True, default=3, null=True)),
                ('calculated_dividend', models.FloatField(blank=True, null=True)),
                ('holded_dividends', models.FloatField(blank=True, null=True)),
                ('payable_dividens', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
