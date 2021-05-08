from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post2
from .forms import BlogForm

# Create your views here.

def main2(request):
    posts2 = Post2.objects.all()
    return render(request, "main2.html", {'posts2':posts2})

def detail2(request, id):
    post2 = get_object_or_404(Post2, pk = id)
    return render(request, 'detail2.html', {'post2':post2})

def new2(request):
    form = BlogForm()
    return render(request, 'new2.html', {'form':form})

def create2(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.post2_date = timezone.now()
        new_blog.save()
        return redirect('detail2', new_blog.id)
    return redirect('home')

def edit2(request, id):
    edit_blog = Post2.objects.get(id = id)
    return render(request, 'edit2.html', {'blog':edit_blog})

def update2(request, id):
    update_blog = Post2.objects.get(id = id)
    update_blog.post2_title = request.POST['title']
    update_blog.post2_writer = request.POST['writer']
    update_blog.post2_body = request.POST['body']
    update_blog.post2_date = timezone.now()
    update_blog.save()
    return redirect('detail2', update_blog.id)

def delete2(request, id):
    delete_blog = Post2.objects.get(id = id)
    delete_blog.delete()
    return redirect('main2')