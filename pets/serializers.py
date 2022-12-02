from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class PetSerializer(serializers.Serializer):
    SEX_CHOICES = (("Male", "Male"), ("Female", "Female"))

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SEX_CHOICES, default="Not Informed")

    group = GroupSerializer(read_only=True)
    traits = TraitSerializer(many=True, read_only=True)
# aa
