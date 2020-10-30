# Generated by Django 3.1.2 on 2020-10-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201029_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='valid',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='final_determination',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_issued',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_received',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='social',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='total_award',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
