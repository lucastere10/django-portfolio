from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PageProfile
# Register your models here.

# Apply summernote to all TextField in model.
class ProfileAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(PageProfile, ProfileAdmin)