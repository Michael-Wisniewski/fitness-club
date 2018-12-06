from django.shortcuts import render

def posts_list(request):

    return render(request, 'blog/posts_list.html')
