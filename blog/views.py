from django.shortcuts import render,get_object_or_404
from .models import Blog,Comment
from django.core.paginator import (Paginator,EmptyPage, PageNotAnInteger)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from blog.forms import UserForm


@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:allblogs'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
    return render(request,'blog/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:allblogs'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'blog/login.html', {})

def allblogs(request):
    #blogs = Blog.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    blogs_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs_list, 2)
    
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try : 
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/allblogs.html', {'blogs':blogs})
 
def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)

    comments = blogdetail.comments.filter(active = True)

    new_comment = None

    if request.method == "POST":
    	comment_form = CommentForm(data=request.POST)
    	if comment_form.is_valid():
    		new_comment = comment_form.save(commit = False)
    		new_comment.blog = blogdetail 
    		new_comment.save()
    else:
    	comment_form = CommentForm()

    return render(request, 'blog/detail.html', {'blog':blogdetail, 'comments':comments, "new_comment":new_comment,'comment_form':comment_form})

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	return render(request, 'blog/contact.html')

def dark(request):
    return render(request, 'blog/dark.html')

