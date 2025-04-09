import datetime

def parse_datetime_local(datetime_str):
    """
    Parsea una cadena de fecha y hora local (YYYY-MM-DDTHH:mm) y devuelve un objeto datetime
    asumiendo la zona horaria de Ecuador (UTC-5).
    """
    if datetime_str:
        try:
            # Parsear la cadena sin información de zona horaria
            dt_obj_naive = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")
            # Asignar la zona horaria de Ecuador (UTC-5)
            local_tz = datetime.timezone(datetime.timedelta(hours=-5))
            dt_obj_aware = dt_obj_naive.replace(tzinfo=local_tz)
            return dt_obj_aware
        except ValueError as e:
            print(f"Error al parsear la fecha y hora local: {e}, Input: {datetime_str}") #Para depuración
            return None
    return None