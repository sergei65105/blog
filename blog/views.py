from django.shortcuts import render

import random

from .models import Post


def posts_list(request):
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