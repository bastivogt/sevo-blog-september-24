from django.contrib import admin

# Register your models here.

from . import models


class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "get_link_image_tag"
    ]
    ordering = ["title"]
    readonly_fields = [
        "get_link_image_tag",
        "get_image_url"
    ]
    fields = [
        "title",
        "image",
        "get_link_image_tag",
        "get_image_url"

    ]


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "id",
        "created_at",
        "updated_at",
        "get_image_tag",
        "get_tags_str",
        "featured",
        "published"   
    ]

    list_filter = [
        "tags",
        "published"
    ]

    ordering = ["-updated_at"]
    readonly_fields = [
        "get_link_image_tag",
        "get_image_url",
    ]

    fields = [
        "title",
        "content",
        "excerpt",
        "image",
        "get_link_image_tag",
        "get_image_url",
        "tags",
        "featured",
        "published"

    ]


admin.site.register(models.Tag)
admin.site.register(models.PostImage, PostImageAdmin)
admin.site.register(models.Post, PostAdmin)
