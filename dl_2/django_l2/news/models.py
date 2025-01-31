from django.db import models

# Create your models here.

class Journalist(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title