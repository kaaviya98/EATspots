from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Restaurant(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_owner"
    )
    location = models.CharField(max_length=200, db_index=True)
    address = models.TextField(max_length=50)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "restaurant_detail",
            args=[
                self.slug,
            ],
        )
