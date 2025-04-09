
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'accounts': request.build_absolute_uri('api/accounts/'),
        'hotels': request.build_absolute_uri('api/hotels/'),
        'bookings': request.build_absolute_uri('api/bookings/'),
        'dashboard': request.build_absolute_uri('api/dashboard/'),
    })

#python 