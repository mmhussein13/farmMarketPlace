from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'state', 'country')
    search_fields = ('user__username', 'user__email', 'phone')
    list_per_page = 20

admin.site.register(UserProfile, UserProfileAdmin)
