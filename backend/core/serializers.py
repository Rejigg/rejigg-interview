from rest_framework import serializers

from core.models import Lead, Business, Person, Industry, Affiliation

class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ("title",)


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = (
            "id",
            "name",
        )

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            "id",
            "full_name",
            "about_me",
        )


class BusinessSerializer(serializers.ModelSerializer):
    person = PersonSerializer(source="owner", read_only=True)
    owner = PersonSerializer(read_only=True)
    affiliation = AffiliationSerializer(read_only=True)
    industry_id = serializers.IntegerField(read_only=True, source="safe_industry.id")
    safe_industry = IndustrySerializer(read_only=True)
    owner_full_name = serializers.CharField(
        source="owner.full_name",
        required=False,
        default="",
        allow_null=True,
        allow_blank=True,
        read_only=True,
    )
    about_the_owner = serializers.CharField(
        source="owner.about_me",
        required=False,
        default="",
        allow_null=True,
        allow_blank=True,
        read_only=True,
    )
    class Meta:
        model = Business
        fields = (
            "id",
            "name",
            "description",
            "person",
            "industry_id",
            "safe_industry",
            "owner_full_name",
            "about_the_owner",
            "affiliation",
            "owner",
        )


class LeadSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)

    img = serializers.CharField(source="business.owner.profile_img_url", read_only=True)

    class Meta:
        model = Lead
        fields = (
            "id",
            "business",
            "business_id",
            "is_favorite",
            "img"
        )
