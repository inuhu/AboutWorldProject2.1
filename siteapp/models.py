from django.db import models
from django.urls import reverse


class Countries(models.Model):
    title = models.CharField(max_length=255, verbose_name='Countrie')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Photo Content",
    )
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Countries"
        verbose_name = "Countrie"
        ordering = ['title', 'time_create']