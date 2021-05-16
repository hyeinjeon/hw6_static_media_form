from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post2
from .forms import BlogForm

# Create your views here.

def main2(request):
    posts2 = Post2.objects.all()
    return render(request, 'main2.html', {'posts2':posts2})

def detail2(request, id):
    post2 = get_object_or_404(Post2, pk = id)
    return render(request, 'detail2.html', {'post2':post2})

def new2(request):
    if request.method == 'POST': #글을 작성한 후 저장 버튼을 눌렀을 때
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.post2_date = timezone.now()
            post.save()
            return redirect('main2')
    else:   #글을 쓰려고 들어갔을 때
        post_form = BlogForm()   #글을 입력받기 위한 빈 form을 불러옴
        return render(request, 'new2.html', {'post_form':post_form})

# def create2(request):
#     form = BlogForm(request.POST, request.FILES)
#     if form.is_valid():
#         new_blog = form.save(commit=False)
#         new_blog.post2_date = timezone.now()
#         new_blog.save()
#         return redirect('detail2', new_blog.id)
#     return redirect('home')

def edit2(request, id):
    post = get_object_or_404(Post2, pk = id)
    if request.method == 'GET': #수정하려고 들어갔을 때
        post_form = BlogForm(instance = post)
        #현재 post가 포함된 form을 불러옴
        return render(request, 'edit2.html', {'edit_post':post_form})
    else:
        post_form = BlogForm(request.POST, request.FILES, instance = post)
        #현재 post에 가져온 정보를 form에 담음
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.post2_date = timezone.now()
            post.save()
        return redirect('/app2/detail2/'+str(id))


# def update2(request, id):
#     update_blog = Post2.objects.get(id = id)
#     update_blog.post2_title = request.POST['title']
#     update_blog.post2_writer = request.POST['writer']
#     update_blog.post2_body = request.POST['body']
#     update_blog.image = request.POST['image']
#     update_blog.post2_date = timezone.now()
#     update_blog.save()
#     return redirect('detail2', update_blog.id)

def delete2(request, id):
    delete_blog = Post2.objects.get(id = id)
    delete_blog.delete()
    return redirect('main2')