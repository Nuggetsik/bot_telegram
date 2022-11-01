from django.contrib import admin
from .forms import ProfileForm
from .models import Profile
from django.utils.safestring import mark_safe


# Register your models here

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'get_image', 'admin_photo')
    list_display = ('name', 'description', 'price', 'admin_photo')
    form = ProfileForm

    readonly_fields = ["admin_photo"]

    def admin_photo(self, obj):
        if obj.get_image:
            return mark_safe(f'<img src="{obj.get_image.url}" width="220" height="150">')
        else:
            return f'(none)'
    admin_photo.short_description = 'Image'
    

    
    
