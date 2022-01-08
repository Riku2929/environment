#from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from .models import Article,Comment
from .forms import ArticleForm
#from .comment_form import CommentCreateForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django import forms
from django.shortcuts import render


#最初のページを映し出すためのIndexVIew
class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]

#記事を映し出すためのArticleView
class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'

#画面上で記事を投稿するためのview(formsのためのもの)
class FormView(generic.CreateView):
    form_class = ArticleForm
    template_name = 'form.html'
    success_url = '/'

class CommentCreate(generic.CreateView):
    """コメント投稿ページのビュー"""
    #template_name = 'secound_form.html'
    model = Comment
    #form_class = CommentCreateForm


    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Article, pk=post_pk)
        comment = form.save(commit=False)
        comment.article = post
        comment.save()
        return redirect('first_news:first_object', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Article, pk=self.kwargs['pk'])
        return context

def show_index(request):
    return render(request, 'index.html')

first_object = IndexView.as_view()
secound_object = ArticleView.as_view()
thrd_object = FormView.as_view()
force_object = CommentCreate.as_view()