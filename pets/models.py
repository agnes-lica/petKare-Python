from django.db import models


class sex_choices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    NOT_INFORMED = "Not_Informed"


class Pet(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=sex_choices.choices, default=sex_choices.NOT_INFORMED)
    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="pets")

    def __repr__(self):
        return f"<{[self.id]} {self.name}>"
