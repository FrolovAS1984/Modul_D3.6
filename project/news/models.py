from django.db import models


class Post(models.Model):
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
