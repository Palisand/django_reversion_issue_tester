from django.contrib import admin
from app.models import Foo, Bar
from reversion.admin import VersionAdmin


class FooAdmin(VersionAdmin):
    list_display = ("id", "thing", "stuff")
    list_editable = ("thing", "stuff")


class BarAdmin(admin.ModelAdmin):
    list_display = ("id", "thing", "stuff")
    list_editable = ("thing", "stuff")


admin.site.register(Foo, FooAdmin)
admin.site.register(Bar, BarAdmin)
