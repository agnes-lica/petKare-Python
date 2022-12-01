from django.db import models


class Group(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID",)
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<{[self.id]} {self.scientific_name}>"
