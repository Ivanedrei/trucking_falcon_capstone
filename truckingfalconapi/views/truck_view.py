"""View module for handling requests about game types"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from truckingfalconapi.models.employee import Employee
from truckingfalconapi.models.fuel import Fuel
from truckingfalconapi.models.truck import Truck


class FuelView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single fuel object
        Returns:
            Response -- JSON serialized deliveries
        """
        try:
            truck = Truck.objects.get(pk=pk)
            serializer = TruckSerializer(truck)
            return Response(serializer.data)
        except Truck.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all fuel list

        Returns:
            Response -- JSON serialized list of delivery by permission type
        """
        truck = Truck.objects.all()
        delivery_id = request.query_params.get('id', None)
        if delivery_id is not None:
            delivery = delivery.filter(delivery_id=delivery)

        serializer = TruckSerializer(truck, many=True)
        return Response(serializer.data)

#    This code works fine
    # def create(self, request):
    #     """Handle POST operations

    #     Returns
    #     Response -- JSON serialized game instance
    #     """

    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     game_type = GameType.objects.get(pk=request.data["game_type"])

    #     game = Game.objects.create(
    #         title=request.data["title"],
    #         maker=request.data["maker"],
    #         number_of_players=request.data["number_of_players"],
    #         skill_level=request.data["skill_level"],
    #         gamer=gamer,
    #         game_type=game_type
    #     )
    #     serializer = TruckSerializer(game)
    #     return Response(serializer.data)


class TruckSerializer(serializers.ModelSerializer):
    """JSON serializer for delivery
    """
    class Meta:
        model = Fuel
        fields = ['id', 'plate_number', 'color', 'make']
        depth = 1
