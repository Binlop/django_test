import time
from datetime import datetime
import pytz
import json

class RequestTimeMiddleware:
    def __init__(self, get_response):
       self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if self.check_url_path:
            timestamp = time.monotonic()

            data = {
                'date': self.get_current_date_UTC_7(),
                'path': request.path,
                'request_total': round(time.monotonic() - timestamp, 3),
                'user': str(request.user),
            }
            self.write_data_to_json_logs(data)
        return response
    
    @property
    def check_url_path(self, request):
        if request.path.startswith('/sampletypes/'):
            return True


    def get_current_date_UTC_7(self):
        current_datetime = datetime.now()
        timezone_utc_7 = pytz.timezone('Asia/Krasnoyarsk')  # Выберите нужную зону времени из базы данных часовых поясов
        current_datetime_utc_7 = current_datetime.astimezone(timezone_utc_7)
        return current_datetime_utc_7.strftime("%Y-%m-%d %H:%M:%S")
    
    def write_data_to_json_logs(self, data):
        with open('request.log', 'a') as f:
           f.write(json.dumps(data) + '\n')