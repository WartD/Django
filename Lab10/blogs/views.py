
from django.shortcuts import render, get_object_or_404, redirect
from blogs.models import Article, Comment, CommentForm


def home(request):
    article = Article.objects.all()
    context = {
        'articles' : article
    }
    return render(request, 'blog/home.html', context)

# Create your views here.
def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id) #Получаем статью или 404 ошибку

    if request.method == "POST":
        form = CommentForm(request.POST) #Получаем данные из формы

        if form.is_valid(): #Проверяем валидность формы
            if request.user.is_authenticated: #Проверяем авторизацию пользователя
                form.cleaned_data["article"] = article #Добавляем ключ и значение статьи
                try:
                    Comment.objects.create(**form.cleaned_data) #Создаем новую запись в таблицу
                    return redirect('article', article_id) #Обновляем страницу со статьей
                except Exception as Ex:
                    print(Ex)
                    form.add_error(None, 'Ошибка добавления коммента')
            else:
                return redirect("login")

    else:
        form = CommentForm()
    return render(request, 'blog/article.html', {'article': article, 'comment': article.comment_set.all, 'form': form})
