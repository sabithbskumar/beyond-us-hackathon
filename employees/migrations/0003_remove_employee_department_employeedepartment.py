# Generated by Django 4.2.3 on 2023-07-08 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.CreateModel(
            name='EmployeeDepartment',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employees.employee')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
            ],
        ),
    ]