# Generated by Django 4.1.5 on 2023-01-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="createdAt",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="isOffering",
            new_name="is_offering",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="isPremium",
            new_name="is_premium",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="updatedAt",
            new_name="updated_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="isActive",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
