web: gunicorn mygpo.wsgi:application -c conf/gunicorn.conf.py --bind=0.0.0.0:$PORT
beat: celery -A mygpo beat --pidfile /tmp/celerybeat.pid -S django
celery: celery -A mygpo worker --concurrency=3 -l info -Ofair
