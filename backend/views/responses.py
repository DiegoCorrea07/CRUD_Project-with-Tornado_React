import json

def success_response(data):
    """Genera una respuesta exitosa en formato JSON."""
    return json.dumps({"status": "success", "data": data})

def error_response(message):
    """Genera una respuesta de error en formato JSON."""
    return json.dumps({"status": "error", "message": message})
