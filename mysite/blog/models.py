from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    # Input field
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)

    # text area
    content = models.TextField()

    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

    # subclass
    class Meta:
        ordering = ['-created']

