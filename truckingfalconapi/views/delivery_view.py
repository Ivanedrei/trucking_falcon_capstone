"""View module for handling requests about game types"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from truckingfalconapi.models import Delivery
from truckingfalconapi.models.employee import Employee


class DeliveryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized deliveries
        """
        try:
            deliveries = Delivery.objects.get(pk=pk)
            serializer = DeliverySerializer(deliveries)
            return Response(serializer.data)
        except Delivery.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of delivery by permission type
        """
        delivery = Delivery.objects.all()
        permission_type = request.query_params.get('type', None)
        if permission_type is not None:
            delivery = delivery.filter(permission_type_id=permission_type)

        serializer = DeliverySerializer(delivery, many=True)
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
    #     serializer = DeliverySerializer(game)
    #     return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized delivery instance
        """
        employee = Employee.objects.get(user=request.auth.user)
        serializer = CreateDeliverySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delivery = serializer.save(employee=employee)
        ids = DeliverySerializer(delivery)
        return Response(ids.data, status=status.HTTP_201_CREATED)

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
        """Handle PUT requests for a delivery

        Returns:
            Response -- Empty body with 204 status code
        """
        delivery = Delivery.objects.get(pk=pk)
        serializer = CreateDeliverySerializer(delivery, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE request for a delivery

        Returns:
            Response -- empty body with 204 status code
        """
        delivery = Delivery.objects.get(pk=pk)
        delivery.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class DeliverySerializer(serializers.ModelSerializer):
    """JSON serializer for delivery
    """
    class Meta:
        model = Delivery
        fields = ['id', 'employee', 'from_address', 'destination',
                  'start_date', 'loaded', 'total_miles', 'truck',
                  'finish_date']
        depth = 1


class CreateDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'from_address', 'destination',
                  'start_date', 'loaded', 'total_miles', 'truck',
                  'finish_date']
