# Generated by Django 3.2 on 2021-05-24 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='ClientID',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='StyleID',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='StyleID',
        ),
        migrations.RemoveField(
            model_name='style',
            name='TreinerID',
        ),
        migrations.AddField(
            model_name='payment',
            name='Client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client'),
        ),
        migrations.AddField(
            model_name='payment',
            name='Style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.style'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='Style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.style'),
        ),
        migrations.AddField(
            model_name='style',
            name='Treiner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.teacher'),
        ),
    ]
