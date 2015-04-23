from django.contrib import admin
from .models import Join

@admin.register(Join)
class JoinAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'updated')

    class Meta:
        model = Join


