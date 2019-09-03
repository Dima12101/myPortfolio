from django.http import  Http404, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse
from .models import Comment
#from django.http import HttpResponse

def index(request):
    latest_comments_list = Comment.objects.order_by('-date')[:5]
    return render(request, 'main/index.html', {
        'latest_comments_list' : latest_comments_list})

def detail_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except:
        raise Http404("Комментария не существует:(")

    return render(request, 'main/detail_comment.html', {'comment' : comment})

def leave_comment(request):
    new_comment = Comment(
        author_name=request.POST['name'],
        comment_text=request.POST['text'],
        date=timezone.now()
    )
    new_comment.save()
    return HttpResponseRedirect(reverse('main:index'))
