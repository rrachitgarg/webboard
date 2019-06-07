from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Board,Post,Topic,User
from .forms import AddBoardTopicForm,PostsReplyForm

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def add_board_topics(request,pk):
    board= get_object_or_404(Board,pk=pk)
    
    if request.method == 'POST':
        form=AddBoardTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board=board
            topic.starter=request.user
            topic.save()
            post=Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)    
    else:
        form = AddBoardTopicForm()
    return render(request,'add_topic.html',{'board':board,'form':form})

def topic_post(request,pk,topic_pk):
    topic=get_object_or_404(Topic,board__pk=pk,pk=topic_pk)
    return render(request,'topic_post.html',{'topic':topic})

@login_required
def posts_reply(request,pk,topic_pk):
    topic=get_object_or_404(Topic,board__pk=pk,pk=topic_pk)
    if request.method== 'POST':
        form=PostsReplyForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.topic=topic
            post.created_by=request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form=PostsReplyForm()
    return render(request,'reply_topic.html',{'topic':topic,'form':form})



