# Generated by Django 4.2.3 on 2023-07-08 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employee_department_employeedepartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='manager_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee'),
        ),
    ]