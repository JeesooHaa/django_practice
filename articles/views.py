from django.shortcuts import render, redirect, get_object_or_404
#
from django.views.decorators.http import require_POST, require_GET
#
from django.contrib.auth.decorators import login_required 
# 
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_GET
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':
        articleform = ArticleForm(request.POST)
        if articleform.is_valid():
            article = articleform.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index') 
    else: 
        articleform = ArticleForm()
    context = {'articleform': articleform}
    return render(request, 'articles/create.html', context)


@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    commentform = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'commentform': commentform,
    }
    return render(request, 'articles/detail.html', context)


@login_required
# create 와 같은 html 로 가도 상관없음 
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 이걸 먼저?
    if article.user == request.user:
        if request.method == 'POST':
            #
            article = ArticleForm(request.POST, instance=article)
            if article.is_valid():
                article.save()
                return redirect('articles:index') 
        else: 
            #
            articleform = ArticleForm(instance=article)
    # 다른 사람 처리 
    else:
        return redirect('articles:detail', article_pk)
    context = {'articleform': articleform}
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    #
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.user == request.user:
            article.delete()
        else: 
            return redirect('articles:detail', article_pk)
    #
    return redirect('articles:index')


@require_POST
def commentcreate(request, article_pk):
    #
    if request.user.is_authenticated:
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            # .save
            comment = commentform.save(commit=False)
            comment.article_id = article_pk
            #
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article_pk) 


@require_POST
def commentdelete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
        return redirect('articles:detail', article_pk) 
    #
    return HttpResponse('Error', status=401)


# login_required!!!
@login_required
def liked(request, article_pk):
    # request.user
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    if user in article.liked_users.all():
        # remove!!
        user.liked_articles.remove(article)
    else:
        user.liked_articles.add(article)
    return redirect('articles:detail', article_pk) 
