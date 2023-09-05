from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("post_detail", kwargs={"pk": self.pk})
