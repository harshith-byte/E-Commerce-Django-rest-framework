

# Register your models here.
from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(category)
admin.site.register(products)
admin.site.register(Cart)