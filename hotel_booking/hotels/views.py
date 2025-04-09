from rest_framework import viewsets, permissions
from hotels.models import Hotel, Review
from hotels.serializers import HotelSerializer, ReviewSerializer,HotelImageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(hotel_id=self.kwargs['hotel_pk'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, hotel_id=self.kwargs['hotel_pk'])


@api_view(['GET'])
def hotels_root(request):
    return Response({'message': 'Welcome to the Hotels API'})


class HotelReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

        # Prevent duplicate reviews
        if Review.objects.filter(user=request.user, hotel=hotel).exists():
            return Response({'error': 'You have already reviewed this hotel.'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['hotel'] = hotel.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, hotel=hotel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class HotelImageUploadView(generics.CreateAPIView):
    serializer_class = HotelImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['hotel'] = hotel.id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save(hotel=hotel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    