from django.db import models

class Biblioteka(models.Model):
    book_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.book_name}"

