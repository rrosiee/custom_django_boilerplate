from django.db import models

from boilerplate.bases.models import Model


# Main Section
class Post(Model):
    title = models.CharField("제목", max_length=30)
    content = models.TextField("내용", null=True, blank=True)
    visit_count = models.IntegerField("조회수", default=0)

    class Meta:
        verbose_name = verbose_name_plural = "게시글"
