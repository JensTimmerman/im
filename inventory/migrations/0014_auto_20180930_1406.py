# Generated by Django 2.1.1 on 2018-09-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_pantryitem_expiry_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('in_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Location')),
            ],
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='expiry_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pantryitem',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.Location'),
        ),
    ]
