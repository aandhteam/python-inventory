from django.shortcuts import render, get_object_or_404
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def inventory_api(request):
    name_query = request.GET.get('name', '')
    inventories = Inventory.objects.filter(name__icontains=name_query).select_related('supplier')
    serializer = InventorySerializer(inventories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def inventory_list(request):
    inventories = Inventory.objects.select_related('supplier').all()
    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})


def inventory_detail(request, id):
    item = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/inventory_detail.html', {'item': item})
