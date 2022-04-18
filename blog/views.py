from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Post
from .forms import PostForm



def blog_home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'blog/home.html', context)


def post_details(request, pk):
	post = Post.objects.get(id=pk)
	tags = post.tag.all()
	context = {'post': post, 'tags': tags}
	return render(request, 'blog/post_details.html', context)

@login_required(login_url='blog-home')
def create_post(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('blog-home')	
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)

@login_required(login_url='blog-home')
def update_post(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('blog-home')		
	context = {'form': form}
	return render(request, 'blog/post_form.html', context)

@login_required(login_url='blog-home')
def delete_post(request, pk):
	post = Post.objects.get(id=pk)
	if request.method =="POST":
		post.delete()
		return redirect('blog-home')
	context = {'post': post}
	return render(request, 'blog/delete_form.html', context)