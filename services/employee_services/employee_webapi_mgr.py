import requests

from commons.app_constants import BASE_URL


def get_employee(id: int = 1) -> dict:
    try:
        response = requests.get(f'{BASE_URL}/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    
    except Exception as ex:
        return f'ERROR: Dogodila se greska {ex}'
