from django.db import models

class Comment(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    author = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'comment'  # Set 

    def __str__(self):
        return f'{self.author} - {self.text[:50]}'
