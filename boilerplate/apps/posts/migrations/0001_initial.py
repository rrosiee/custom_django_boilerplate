# Generated by Django 5.1.4 on 2024-12-05 14:20

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="삭제 여부"
                    ),
                ),
                (
                    "deleted",
                    models.DateTimeField(blank=True, null=True, verbose_name="삭제 시간"),
                ),
                ("title", models.CharField(max_length=30, verbose_name="제목")),
                ("content", models.TextField(blank=True, null=True, verbose_name="내용")),
            ],
            options={
                "verbose_name": "게시글",
                "verbose_name_plural": "게시글",
            },
        ),
    ]
