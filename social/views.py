from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.



def feed(request):
	#queryset = request.GET.get("buscar")
	#print(queryset)
	posts = Post.objects.all()
	context = {'posts': posts}
	#if queryset:
	#	perfil = User.objects.filter(
#			Q(username = queryset),
			#Q( = queryset)
#		).distinct()
	return render(request, 'social/feed.html', context)

def profile(request, username=None):
	queryset = request.GET.get("buscar")
	print(queryset)
	if queryset:
		perfil = User.objects.filter(Q(username = queryset)).distinct()
	current_user = request.user
	if username and username != current_user.username: #revisamos a que usuarios queremos ver
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'social/profile.html', {'user':user, 'posts':posts})

def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado correctamente')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form': form }

	return render(request, 'social/registro.html', context)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Posteado correctamente')
			return redirect('feed')
	else:
		form = PostForm()


	return render(request, 'social/post.html', {'form': form})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'dejaste de seguir a {username}')
	return redirect('feed')

