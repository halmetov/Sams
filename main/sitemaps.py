# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9  # немного выше для важных статических страниц

    def items(self):
        # имена именованных url-шаблонов
        return ['main:index', 'main:catalog', 'main:about', 'main:contact']

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()  # или .filter(is_published=True)

    # если есть поле updated_at:
    # def lastmod(self, obj): return obj.updated_at

    # если нет get_absolute_url — можно так:
    # def location(self, obj): return reverse('category_detail', kwargs={'slug': obj.slug})


class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj): return obj.updated_at
