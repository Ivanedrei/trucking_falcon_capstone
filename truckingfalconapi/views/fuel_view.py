"""View module for handling requests about game types"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from truckingfalconapi.models.employee import Employee
from truckingfalconapi.models.fuel import Fuel


class FuelView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single fuel object
        Returns:
            Response -- JSON serialized deliveries
        """
        try:
            fuel = Fuel.objects.get(pk=pk)
            serializer = FuelSerializer(fuel)
            return Response(serializer.data)
        except Fuel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all fuel list

        Returns:
            Response -- JSON serialized list of delivery by permission type
        """
        fuel = Fuel.objects.all()
        delivery_id = request.query_params.get('id', None)
        if delivery_id is not None:
            delivery = delivery.filter(delivery_id=delivery)

        serializer = FuelSerializer(fuel, many=True)
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
    #     serializer = FuelSerializer(game)
    #     return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized fuel instance
        """
        employee = Employee.objects.get(user=request.auth.user)
        serializer = CreateFuelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fuel = serializer.save(employee=employee)
        fuel_serializer = FuelSerializer(fuel)
        return Response(fuel_serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, pk):
    #     """Handle PUT requests for a game

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """

    #     game = Game.objects.get(pk=pk)
    #     game.title = request.data["title"]
    #     game.maker = request.data["maker"]
    #     game.number_of_players = request.data["number_of_players"]
    #     game.skill_level = request.data["skill_level"]

    #     game_type = GameType.objects.get(pk=request.data["game_type"])
    #     game.game_type = game_type
    #     game.save()

    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """Handle PUT requests for a fuel object

        Returns:
            Response -- Empty body with 204 status code
        """
        fuel = Fuel.objects.get(pk=pk)
        serializer = CreateFuelSerializer(fuel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE request for a fuel object

        Returns:
            Response -- empty body with 204 status code
        """
        fuel = Fuel.objects.get(pk=pk)
        fuel.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class FuelSerializer(serializers.ModelSerializer):
    """JSON serializer for delivery
    """
    class Meta:
        model = Fuel
        fields = ['id', 'delivery', 'fuel_price', 'gallons_fuel',
                  'fuel_date', 'total_fuel_cost']
        depth = 1


class CreateFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['id', 'fuel_price', 'gallons_fuel',
                  'fuel_date', 'total_fuel_cost']
