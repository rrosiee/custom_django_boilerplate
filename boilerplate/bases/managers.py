from django.db.models import Manager


# Main Section
class AvailableManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
