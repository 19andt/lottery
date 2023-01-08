from django.contrib import admin
from .models import User, Slot, Bid, Game

# Register your models here.


@admin.register(User)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.get_fields()]


@admin.register(Slot)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slot._meta.get_fields()]


@admin.register(Bid)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bid._meta.get_fields()]


@admin.register(Game)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Game._meta.get_fields()]
