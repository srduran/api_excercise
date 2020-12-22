from django.contrib import admin
from .models import Monkey


class MonkeyAdmin(admin.ModelAdmin):
  list_display = ('name', 'fleas')


admin.site.register(Monkey, MonkeyAdmin)
