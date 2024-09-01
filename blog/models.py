from django.db import models
from django.contrib import admin
from django.utils.html import format_html

from tinymce import models as tinymce_models
# Create your models here.


from django.contrib.auth import get_user_model
User = get_user_model()


# Tag
class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    class Meta():
        ordering = ["title"]



# PostImage
class PostImage(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="uploads/images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
    @admin.display(description="Image preview")
    def get_image_tag(self):
        img_tag = f'<img src="{self.image.url}" alt="{self.title}" title="{self.title}" style="width: 80px; height: 80px; object-fit: cover;" />'
        return format_html(img_tag)
    
    @admin.display(description="Image preview link")
    def get_link_image_tag(self):
        a_tag = f'<a href="{self.image.url}" title="{self.title}">{self.get_image_tag()}</a>'
        return format_html(a_tag)
    
    @admin.display(description="Image URL")
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
    

    

# Post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = tinymce_models.HTMLField()
    excerpt = models.TextField(max_length=255, default="")
    image = models.ForeignKey(PostImage, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    @admin.display(description="Image preview")
    def get_image_tag(self):
        return self.image.get_image_tag()
    
    @admin.display(description="Image preview link")
    def get_link_image_tag(self):
        return self.image.get_link_image_tag()
    

    @admin.display(description="Image URL")
    def get_image_url(self):
        return self.image.get_image_url()
    
    

    @admin.display(description="Tags")
    def get_tags_str(self):
        tags = self.tags.all().order_by("title")
        tags_list = [tag.title for tag in tags]
        return ", ".join(tags_list)
