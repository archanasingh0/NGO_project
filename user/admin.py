from django.contrib import admin
from  .models import *

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message")

admin.site.register(contact,contactAdmin)

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('gname','gpic')
admin.site.register(igallery,igalleryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('shead','ssub','sdes','spic')
admin.site.register(slider,sliderAdmin)


class iblogAdmin(admin.ModelAdmin):
    list_display = ('bname','bdes','bpicture','bdate','id')
admin.site.register(iblog,iblogAdmin)

class imembershipAdmin(admin.ModelAdmin):
    list_display = ('mname','mpincode','mcity','memail','mbank','mcompany','maddress')
admin.site.register(imembership,imembershipAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ccity','cdate')
admin.site.register(city,cityAdmin)

class vgalleryAdmin(admin.ModelAdmin):
    list_display = ('vlink','vdes','vtitle','vdate','id')
admin.site.register(vgallery,vgalleryAdmin)

class idonateAdmin(admin.ModelAdmin):
    list_display = ('id','damount','dfname','dlname','demail','dphone','dcountry','dadd','dstate','dcode','doccu')
admin.site.register(idonate,idonateAdmin)

class icountryAdmin(admin.ModelAdmin):
    list_display = ('countryd','id')
admin.site.register(icountry,icountryAdmin)

class istateAdmin(admin.ModelAdmin):
    list_display = ('statei','id')
admin.site.register(istate,istateAdmin)