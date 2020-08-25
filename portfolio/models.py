from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class Technology(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100, default="")
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    description = models.TextField(verbose_name="Description", default="")
    technologies = models.ManyToManyField(Technology, verbose_name="Tecnologies", blank=True, default='')
    image = models.ImageField(verbose_name="Image", upload_to="images", default="", blank=True)
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(350, 200)],
        format='JPEG',
        options={'quality': 60},
    )
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created"]

    def __str__(self):
        return self.title


