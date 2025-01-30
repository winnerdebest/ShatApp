web: gunicorn a_core.wsgi
websocket: daphne a_core.asgi:application -b 0.0.0.0 -p $PORT