from django.contrib import admin
from django.contrib.auth.models import Group, User
from.models import Profile, Meep
#unregister groups
admin.site.unregister(Group)


#mix Prof with user
class ProfileInLine(admin.StackedInline):
    model = Profile


#extend user models
class UserAdmin(admin.ModelAdmin):
    admin = User
    #just username
    fields = ["username"]
    inlines = [ProfileInLine]



admin.site.unregister(User)

#register User and Prof
admin.site.register(User,UserAdmin)
#admin.site.register(Profile)

admin.site.register(Meep)
