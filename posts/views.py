from django.shortcuts import render

from posts.forms import PostForm
from posts.models import Post


# Create your views here.
def post_list(request):
    post = Post.objects.first()
    testForm = PostForm()
    content = {'post': post, 'form': testForm}
    return render(request, 'posts/post_list.html', content)