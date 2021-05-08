from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def main(request):
    posts = Post.objects.all()
    return render(request, "main.html", {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Post()
    new_blog.post_title = request.POST['title']
    new_blog.post_writer = request.POST['writer']
    new_blog.post_body = request.POST['body']
    new_blog.post_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Post.objects.get(id = id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Post.objects.get(id = id)
    update_blog.post_title = request.POST['title']
    update_blog.post_writer = request.POST['writer']
    update_blog.post_body = request.POST['body']
    update_blog.post_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Post.objects.get(id = id)
    delete_blog.delete()
    return redirect('main')