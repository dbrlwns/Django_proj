import logging
from operator import is_none

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from posts.forms import PostForm
from posts.models import Post, PostImage, Comment


logger = logging.getLogger("post")

# Create your views here.
@require_POST
def add_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()

        for file in request.FILES.getlist('images'):
            PostImage.objects.create(post=post,image=file)
        logger.info(f"Post-{post.id} added by {request.user}.")
        return redirect('/')
    else:
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html',
                      {'posts': posts, 'form': form, 'update': False})

@require_POST
def del_post(request, id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user==post.author:
        logger.info(f"Post-{post.id} removed.")
        post.delete()
    return redirect('/')


def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('/')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            # add images
            for file in request.FILES.getlist('images'):
                PostImage.objects.create(post=post,image=file)
            # del images user chosen
            del_image = request.POST.getlist('delete_images')
            PostImage.objects.filter(id__in=del_image).delete()
            logger.info(f"Post-{post.id} updated by {request.user}.")
            return redirect('/')

    images = post.images.all()
    posts = Post.objects.all()
    form = PostForm(instance=post)
    return render(request, 'posts/post_list.html',
                  {'form': form, 'images': images, 'posts': posts, 'update': True, 'post': post})



def post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request,
        'posts/post_list.html',
        {'posts': posts, 'form': form}
    )

@require_POST
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    comment = Comment.objects.create(author=request.user, post=post,
                           content=request.POST['comment_content'])
    logger.info(f"Comment-{comment.id} added by {request.user}.")
    return redirect(f'/detail/{comment.post.id}/')

@require_POST
def del_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.user == comment.author:
        logger.info(f"Comment-{comment.id} removed by {request.user}.")
        comment.delete()
    return redirect('/')


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})


















