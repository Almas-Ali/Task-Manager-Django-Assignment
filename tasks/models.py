from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """The base model class"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gallery(BaseModel):
    """The gallery model class"""

    title = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=500, default="")
    photo = models.ImageField(upload_to="gallery/")

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ["-created_at"]


class Task(BaseModel):
    """The task model class"""

    title = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000, default="")

    photos = models.ManyToManyField(Gallery, blank=True)

    due_date = models.DateField()
    priority = models.IntegerField(
        choices=[(1, "Low"), (2, "Medium"), (3, "High")],
        default=1,
    )
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-priority"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/tasks/{self.pk}/"

    def add_photos(self, photos):
        """Add photos to the task"""
        for photo in photos:
            self.photos.add(photo)
        self.save()
