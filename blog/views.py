from django.shortcuts import render, redirect

import random

from .models import Post


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'all_posts': all_posts})


def guess_numbers(request):
    if request.method == 'POST':
        number = request.POST['number']
        if random.randint(1, 4) == int(number):
            return render(request, 'blog/number.html', {
                'result': 'Вы угадали'
            })
        else:
            return render(request, 'blog/number.html', {
                'result': 'Вы не угадали'
            })
    return render(request, 'blog/number.html')


def create(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'blog/create.html')


def post_like(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
    return redirect('post_list')