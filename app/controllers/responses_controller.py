# Шаблон ответа сервера на запрос
def generate_resp(status, message, data):
    return {
        'status': status,
        'message': message,
        'data': data
    }


# Ответы сервера
def resp_ok(data=None):
    if data is None:
        data = []
    return generate_resp('ok', 'SUCCESS', data), 200
