from django.contrib import admin

# Register your models here.
from .models import Category,Post,Comment,Profile
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ("__str__",'author','status')
    list_display_links = ('author',)
    list_editable = ('status',)
    list_filter = ('author','status','created_at','category')
    search_fields = ('title','author__username','content')
    readonly_fields = ('title','content','author','views_count')
    save_on_top = True
    fieldsets = (
        (
            'основное',{
                'fields': ('title','content','author','category')
            }
        ),
        (
            'дополнительно',{
                'fields': ('status','views_count'),
                'classes':('collapse',)
            }
        )
    )
    actions = ['make_published','make_draft']

    def make_published(self,request,queryset):
        queryset.update(status=Post.PUBLISHED)
    make_published.short_discription = 'опубликовать выбранные посты'

    def make_draft(self,request,queryset):
            queryset.update(status=Post.DRAFT)
    make_draft.short_discription = 'перенести в черновик выбранные посты'