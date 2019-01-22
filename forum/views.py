from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm
from django.contrib import messages

# Create your views here.
def post(request, id=None):
    obj = Post.objects.get(id=id)
    context = {"object": obj}
    return render(request, "forum/post_detail.html", context)

def posts(request):
    queryset = Post.objects.all()
    context = {"objects": queryset}
    return render(request, 'forum/post_list.html', context)

def createpost(request):

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user = request.user.userprofile
            newpost.save()
            messages.success(request, ('You Have published new Post...'))
            return redirect('post_list')
    else:
        form = PostModelForm()

    context = {'form': form}
    return render(request, 'forum/new_post.html', context)