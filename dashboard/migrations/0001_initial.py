# Generated by Django 4.1.3 on 2022-11-21 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('transfer_type', models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('recipient_or_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_or_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
