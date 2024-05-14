from django.http import JsonResponse
from .utils import number_to_words
import json

def num_to_english(request):
    # Initialize `number` to None
    number = None

    if request.method == 'GET':
        # Handle GET request; expect `number` as a query parameter
        number = request.GET.get('number')
    elif request.method == 'POST':
        # Handle POST request; expect `number` in the JSON body
        try:
            data = json.loads(request.body)
            number = data.get('number')
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    # Process `number` if it's available
    if number is not None:
        try:
            number = int(number)  # Convert to integer
            return JsonResponse({"status": "ok", "num_in_english": number_to_words(number)})
        except ValueError:
            return JsonResponse({"status": "error", "message": "Invalid input"}, status=400)
    
    # Default response if method is not supported or `number` is not provided
    return JsonResponse({"status": "error", "message": "Method not allowed or number parameter missing"}, status=405)


