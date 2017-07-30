from django.contrib import admin

# Register your models here.

from .models import Bulletin
from .models import Project
from .models import Achievement,Publication,Journal,Database
from .models import People,People_Researcher,People_Administrator,People_Committee,People_Scholar


admin.site.register(Bulletin)
admin.site.register(Project)
admin.site.register(Achievement)
admin.site.register(Publication)
admin.site.register(Journal)
admin.site.register(Database)
admin.site.register(People)
admin.site.register(People_Researcher)
admin.site.register(People_Administrator)
admin.site.register(People_Committee)
admin.site.register(People_Scholar)

