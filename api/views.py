from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Inventory
from .InventorySerializers import InventorySerializer

@api_view(['GET'])
def inventory_list(request):
    inventories = Inventory.objects.all()
    serializer = InventorySerializer(inventories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def inventory_detail(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = InventorySerializer(inventory)
    return Response(serializer.data)

@api_view(['POST'])
def inventory_create(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def inventory_update(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = InventorySerializer(inventory, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def inventory_delete(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    inventory.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
