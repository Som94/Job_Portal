from django.contrib import admin
from testapp.models import BBSR_JOBS,HYD_JOBS,BNG_JOBS

# Register your models here.
class bbsrjobadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnumber']

class hydjobadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnumber']

class bngjobadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnumber']

admin.site.register(BBSR_JOBS,bbsrjobadmin)
admin.site.register(HYD_JOBS,hydjobadmin)
admin.site.register(BNG_JOBS,bngjobadmin)
