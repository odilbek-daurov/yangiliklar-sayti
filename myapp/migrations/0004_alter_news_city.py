# Generated by Django 4.0.1 on 2022-01-13 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_news_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.city'),
        ),
    ]
