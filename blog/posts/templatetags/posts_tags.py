from django import template
from posts.models import Category

register = template.Library()

@register.inclusion_tag('posts/includes/cats_menu.html')
def show_cats(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}