from django.shortcuts import get_object_or_404, render
from .models import Article, Category
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    categories = Category.objects.all()
    category_name = request.GET.get('category')  # Get the selected category from the URL
    if category_name:
        articles = Article.objects.filter(category__name=category_name)  # Filter articles by category
    else:
        articles = Article.objects.all()  # Show all articles if no category is selected
    return render(request, 'app_1/home.html', {
        'categories': categories,
        'articles': articles,
        'is_tutor': request.user.groups.filter(name='Teacher').exists(),
        })
@login_required
def search(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(name__icontains=query) | Article.objects.filter(about__icontains=query)
    return render(request, 'app_1/home.html', {'articles': articles})
@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Fetch the article or return 404 if not found
    return render(request, 'app_1/article_detail.html', {
        'article': article,
        'is_tutor': request.user.groups.filter(name='Teacher').exists(),
        })