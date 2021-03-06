# Generated by Django 3.1.2 on 2020-10-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='valid',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='final_determination',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_issued',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='payment_received',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='social',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='total_award',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
