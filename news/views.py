from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, ArticleCategory, ArticleTag


def news_list(request):
    """Danh sách tất cả tin tức"""
    articles = Article.objects.filter(status='published').select_related('author', 'category')
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        articles = articles.filter(category__slug=category_slug)
    
    # Filter by tag
    tag_slug = request.GET.get('tag')
    if tag_slug:
        articles = articles.filter(tags__slug=tag_slug)
    
    # Search
    search_query = request.GET.get('q')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) |
            Q(excerpt__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(articles, 9)  # 9 bài viết mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Featured articles (top 5)
    featured_articles = Article.objects.filter(
        status='published', 
        is_featured=True
    ).select_related('author', 'category')[:5]
    
    # Categories for sidebar
    categories = ArticleCategory.objects.all()
    
    # Popular articles (most viewed)
    popular_articles = Article.objects.filter(
        status='published'
    ).order_by('-views_count')[:5]
    
    context = {
        'page_obj': page_obj,
        'featured_articles': featured_articles,
        'categories': categories,
        'popular_articles': popular_articles,
        'search_query': search_query,
        'current_category': category_slug,
        'current_tag': tag_slug,
    }
    
    return render(request, 'news/news_list.html', context)


def news_detail(request, slug):
    """Chi tiết bài viết"""
    article = get_object_or_404(
        Article.objects.select_related('author', 'category'),
        slug=slug,
        status='published'
    )
    
    # Tăng lượt xem
    article.views_count += 1
    article.save(update_fields=['views_count'])
    
    # Tags của bài viết
    tags = article.tags.all()
    
    # Bài viết liên quan (cùng category hoặc tag)
    related_articles = Article.objects.filter(
        status='published'
    ).exclude(id=article.id)
    
    if article.category:
        related_articles = related_articles.filter(category=article.category)
    
    related_articles = related_articles.select_related('author', 'category')[:3]
    
    # Popular articles for sidebar
    popular_articles = Article.objects.filter(
        status='published'
    ).exclude(id=article.id).order_by('-views_count')[:5]
    
    context = {
        'article': article,
        'tags': tags,
        'related_articles': related_articles,
        'popular_articles': popular_articles,
    }
    
    return render(request, 'news/news_detail.html', context)


def news_category(request, slug):
    """Danh sách tin theo danh mục"""
    category = get_object_or_404(ArticleCategory, slug=slug)
    articles = Article.objects.filter(
        status='published',
        category=category
    ).select_related('author', 'category')
    
    # Pagination
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Categories for sidebar
    categories = ArticleCategory.objects.all()
    
    # Popular articles
    popular_articles = Article.objects.filter(
        status='published'
    ).order_by('-views_count')[:5]
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'categories': categories,
        'popular_articles': popular_articles,
    }
    
    return render(request, 'news/news_category.html', context)


def news_tag(request, slug):
    """Danh sách tin theo tag"""
    tag = get_object_or_404(ArticleTag, slug=slug)
    articles = tag.articles.filter(status='published').select_related('author', 'category')
    
    # Pagination
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Categories for sidebar
    categories = ArticleCategory.objects.all()
    
    # Popular articles
    popular_articles = Article.objects.filter(
        status='published'
    ).order_by('-views_count')[:5]
    
    context = {
        'tag': tag,
        'page_obj': page_obj,
        'categories': categories,
        'popular_articles': popular_articles,
    }
    
    return render(request, 'news/news_tag.html', context)
