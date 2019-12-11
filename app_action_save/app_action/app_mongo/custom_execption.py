from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data.clear()
        response.data['status_code'] = response.status_code
        if response.status_code == 400:
            response.data['message'] = 'Input error'
        elif response.status_code == 401:
            response.data['message'] = "Auth failed"
        elif response.status_code == 404:
            response.data['message'] = 'Not found'
        elif response.status_code >= 500:
            response.data['message'] = "Internal service errors"
        elif response.status_code == 403:
            response.data['message'] = "Access denied"
        elif response.status_code == 405:
            response.data['message'] = 'Request method error'
        else:
            response.data['message'] = 'Not found'
    return response
