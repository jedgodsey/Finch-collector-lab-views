# Generated by Django 3.1.2 on 2020-10-28 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('social', models.IntegerField()),
                ('final_determination', models.DateField()),
                ('payment_issued', models.DateField()),
                ('payment_received', models.DateField()),
                ('total_award', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_type', models.CharField(choices=[('BL', 'Blindness'), ('BS', 'Brain Stab'), ('ED', 'Ear Drum Piercing'), ('PT', 'Post Traumatic Stress Disorder')], default='BL', max_length=2)),
                ('valid', models.BooleanField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.client')),
            ],
        ),
    ]
