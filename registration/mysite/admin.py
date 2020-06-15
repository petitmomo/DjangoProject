

from django.contrib import admin
from .models import Cour, CourImage

# Register your models here.

class CourImageAdmin(admin.StackedInline):
    model = CourImage

@admin.register(Cour)
class CourAdmin(admin.ModelAdmin):
    inlines = [CourImageAdmin]

    class Meta:
        model = Cour

@admin.register(CourImage)
class CourImageAdmin(admin.ModelAdmin):
    pass

         
