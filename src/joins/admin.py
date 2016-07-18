from django.contrib import admin

# Register your models here.
from .models import Join


class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'friend', 'timestamp', 'updated', 'ip_address', 'ref_id','count_added']
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)
