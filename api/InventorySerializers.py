from rest_framework_mongoengine import serializers
from .models import QualityControl, Package, EmptySpaces, Level, Inventory

class QualityControlSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = QualityControl
        fields = '__all__'

class PackageSerializer(serializers.EmbeddedDocumentSerializer):
    quality_control = QualityControlSerializer()

    class Meta:
        model = Package
        fields = '__all__'

class EmptySpacesSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = EmptySpaces
        fields = '__all__'

class LevelSerializer(serializers.EmbeddedDocumentSerializer):
    packages = PackageSerializer(many=True)
    empty_spaces = EmptySpacesSerializer()

    class Meta:
        model = Level
        fields = '__all__'

class InventorySerializer(serializers.DocumentSerializer):
    levels = LevelSerializer(many=True)

    class Meta:
        model = Inventory
        fields = '__all__'