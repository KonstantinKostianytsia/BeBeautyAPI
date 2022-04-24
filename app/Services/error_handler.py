from rest_framework.response import Response

def handle_error(message: str,translation_code: str, status: int) -> Response: 
    return Response({
        "error": message,
        "translation_code":  translation_code
    }, status=status)

def unhandled_error():

    return Response({
        "error": "Unhandled error",
        "translation_code": "UNHANDLED_ERROR"
    }, status=500)