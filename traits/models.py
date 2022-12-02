from django.db import models


class Trait(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID",)
    name = models.CharField(max_length=20, unique=True)
    pets = models.ManyToManyField("pets.Pet", related_name="traits")
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<{[self.id]} {self.name}>"
