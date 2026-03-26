from django.db import models
from django.contrib.auth.models import User
from news.resources import TYPES, CATEGORIES, article


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        com_rating = sum([com.comment_rating for com in Comment.objects.filter(com_author=self.author).all()])
        posts = self.post_set.all()
        post_rating = sum([post.post_rating for post in posts])
        com_rating2 = 0
        for post in posts:
            com_rating2 += sum([com2.comment_rating for com2 in Comment.objects.filter(com_post=post).all()])

        self.author_rating = post_rating*3 + com_rating + com_rating2
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=3, choices=CATEGORIES)

class Post(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    article_news = models.CharField(max_length=1, choices=TYPES, default=article)
    post_header = models.CharField(max_length=100)
    post_content = models.TextField()
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_categories = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return f'{self.post_content[124:]}...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

class PostCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
   com_post = models.ForeignKey(Post, on_delete=models.CASCADE)
   com_author = models.ForeignKey(User, on_delete=models.CASCADE)
   comment_date = models.DateTimeField(auto_now_add=True)
   comment_content = models.CharField(max_length = 100)
   comment_rating = models.IntegerField(default=0)

   def like(self):
       self.comment_rating += 1
       self.save()

   def dislike(self):
       self.comment_rating -= 1
       self.save()
