from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleModelForm, CommentModelForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def new_article(request):

    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save()
            redirect(article)
        
        else:
            form = ArticleModelForm(request.POST)
    
    else:
        form = ArticleModelForm()
    
    return render(request, 'board/new_article.html', {
        'form':form,
    })

@require_GET
def article_detail(request, article_id):

    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all().order_by('-id')
    comment_form = CommentModelForm()

    return render(request, 'board:article_detail', {
        'article':article,
        'comments':comment,
        'comment_form':comment_form,
    })

@require_http_methods(['GET', 'POST'])
def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST:
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)


    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'board/article_update.html', {
        'form':form,
    })


@require_POST
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect(article)

@require_POST
def create_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.id = article.id
        return 

