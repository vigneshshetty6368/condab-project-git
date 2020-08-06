from django.contrib import admin
from .models import con,item, part
from . import forms
# Register your models here.
class itemAdmin(admin.ModelAdmin):
        list_display=['Conc_Number','Number','SNumber','Mpos','Nom']
        #form=forms.createitemform
        list_filter=['Conc_Number','Number','SNumber']
        search_fields=['Conc_Number','Number','SNumber','Mpos']

admin.site.register(con)
admin.site.register(item,itemAdmin)
admin.site.register(part)
