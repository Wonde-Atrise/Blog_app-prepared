from django.contrib import admin

# Register your models here
from .models import Blogmodel,Message,Profile
class ProperAdmin(admin.ModelAdmin):
 list_display = ('title','description')
 list_editable = ('description',)
 list_per_page = 4
 search_fields = ('title', 'description',)
admin.site.site_header ="Blog App"
admin.site.site_title ="Blog section"
admin.site.index_title ="welcome to Bog page "

admin.site.register(Blogmodel, ProperAdmin)
admin.site.register(Message )
admin.site.register(Profile)