from rest_framework import serializers

from pets.models import Pet
from groups.models import Group
from traits.models import Trait
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

    traits_count = serializers.SerializerMethodField(
        method_name="traits_count_function")

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def traits_count_function(self, obj: Pet):
        return obj.traits.count()

    def create(self, validated_data: dict) -> Pet:

        group_dict = validated_data.pop("group")
        group_create = Group.objects.get_or_create(**group_dict)[0]

        trait_list = validated_data.pop("traits")

        pet = Pet.objects.create(
            **validated_data, group=group_create)

        for trait_dict in trait_list:
            trait_create = Trait.objects.get_or_create(**trait_dict)[0]
            pet.traits.add(trait_create)

        return pet

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            if key == "group":
                group_obj = Group.objects.get_or_create(
                    **validated_data["group"])[0]
                setattr(instance, key, group_obj)
                continue

            if key == "traits":
                trait_list = validated_data["traits"]
                new_trait = [Trait.objects.get_or_create(
                    **trait_dict)[0] for trait_dict in trait_list]
                instance.traits.set(new_trait)
                continue

            setattr(instance, key, value)

        instance.save()

        return instance
