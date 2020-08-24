from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_type(request, type):
    print("here", type)
    posts = Post.objects.filter(tags__contains=type).order_by('published_date')
    print(posts)
    return render(request, 'post_type.html', {'posts':posts})
