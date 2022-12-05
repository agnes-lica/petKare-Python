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

    # traits_count = serializers.SerializerMethodField(
    #    method_name="traits_count_function")

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    # def traits_count_function(self, obj: Pet):
    #    count = obj
    #    print("=" * 100)
    #    print(obj)
    #    print("=" * 100)
    #    return "count"

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
        group_dict = validated_data.pop("group", None)
        if group_dict:
            group_obj = Group.objects.get_or_create(pets=instance)[0]
            for key, value in group_dict.items():
                setattr(group_obj, key, value)
            group_obj.save()

        traits_list = validated_data.pop("traits", None)
        for trait in traits_list:
            if trait:
                trait_obj = Trait.objects.get_or_create(pets=instance)[0]
                for key, value in trait.items():
                    set(trait_obj, key, value)
                trait_obj.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
