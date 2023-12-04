wsgi_app = "gavr.wsgi:application"
workers = 2
bind = "0.0.0.0:8000"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True
loglevel = "info"
