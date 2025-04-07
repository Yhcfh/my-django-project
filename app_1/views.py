# Importing necessary functions and modules from Django
from django.shortcuts import get_object_or_404, render
from .models import Article, Category  # Importing models for Article and Category
from django.contrib.auth.decorators import login_required  # Importing decorator to require login for access

# View function for the homepage, decorated with login_required to ensure the user is logged in
@login_required
def home(request):
    categories = Category.objects.all()  # Retrieve all categories from the database
    category_name = request.GET.get('category')  # Get the selected category from the URL query parameters
    if category_name:
        # If a category is selected, filter articles by that category's name
        articles = Article.objects.filter(category__name=category_name)
    else:
        # If no category is selected, fetch all articles
        articles = Article.objects.all()
    
    # Render the homepage template with the categories, articles, and user group information (whether the user is a tutor)
    return render(request, 'app_1/home.html', {
        'categories': categories,  # Pass the categories to the template
        'articles': articles,  # Pass the articles to the template
        'is_tutor': request.user.groups.filter(name='Teacher').exists(),  # Check if the user belongs to the 'Teacher' group
    })

# View function for handling the search functionality, also decorated with login_required
@login_required
def search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    # Filter articles by checking if the query exists in the 'name' or 'about' fields of the Article model
    articles = Article.objects.filter(name__icontains=query) | Article.objects.filter(about__icontains=query)
    
    # Render the homepage template again, but only with the filtered articles based on the search query
    return render(request, 'app_1/home.html', {'articles': articles})  # Pass the filtered articles to the template

# View function for showing the details of a specific article
@login_required
def article_detail(request, article_id):
    # Fetch the article using the provided article_id or return a 404 if the article does not exist
    article = get_object_or_404(Article, id=article_id)
    
    # Render the article detail page, passing the article data and user group information (whether the user is a tutor)
    return render(request, 'app_1/article_detail.html', {
        'article': article,  # Pass the article object to the template
        'is_tutor': request.user.groups.filter(name='Teacher').exists(),  # Check if the user belongs to the 'Teacher' group
    })
