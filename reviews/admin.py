from django.contrib import admin
from .models import Wine
from .models import Review
from .models import User


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user')
    list_filter = ['rating']
    search_fields = ['body']


class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('residual_sugar', 'alcohol', 'color')

admin.site.register(Wine, WineAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User)

# Register your models here.
