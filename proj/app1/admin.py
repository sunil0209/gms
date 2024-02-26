from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Use Django's ORM to fetch all objects from the Complaint model
        queryset = super().get_queryset(request)

        # You can apply additional filters or ordering if needed
        # queryset = queryset.filter(your_filtering_conditions).order_by(your_ordering_conditions)

        return queryset

admin.site.register(Complaint, ComplaintAdmin)
