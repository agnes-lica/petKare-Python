from django.db import models


class Pet(models.Model):
    SEX_CHOICES = (("Male", "Male"), ("Female", "Female"))

    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=SEX_CHOICES, default="Not Informed")
    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="pets")

    def __repr__(self):
        return f"<{[self.id]} {self.name}>"
