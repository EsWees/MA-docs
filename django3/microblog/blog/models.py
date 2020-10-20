from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"id={self.id}, title={self.title}, slug={self.slug}"

# from blog.models import Post
## p2 = Post.objects.create(title="asdasd", slug=2, body='Lalala! lalala?1')
# >>> pq = Post.objects.get(slug=2)
# >>> pq
# <Post: asdasd>
# >>>