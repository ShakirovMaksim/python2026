def prepare_request(**kwargs):
    if "endpoint" not in kwargs:
        raise ValueError("Не ведён аргумент!")

    timeout = kwargs.get('timeout', 5)
    retries = kwargs.get('retries', 3)

    payload = {
        key: value for key, value in kwargs.items()
        if key not in ('endpoint', 'timeout', 'retries')
    }

    return {
        'endpoint': kwargs['endpoint'],
        'control': {
            'timeout': timeout,
            'retries': retries
        },
        'payload': payload
    }


print(prepare_request(endpoint="/stats", data=[1, 2]))

print(prepare_request(endpoint="/sync", timeout=10, retries=0, mode="fast"))
