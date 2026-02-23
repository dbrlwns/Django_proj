from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.title}'

class PostImage(models.Model):
    # Post.images 로 접근가능
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='postImages/',
                              validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'webp', 'gif'])])
    # 이미지 확장자 검증 추가

class Comment(models.Model):
    # Post.comments 로 접근가능
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f'{self.id}:{self.author} - {self.content}'


