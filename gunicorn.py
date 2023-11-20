wsgi_app = "gavr.wsgi"
loglevel = "debug"
workers = 2
bind = "0.0.0.0:8000"
accesslog = errorlog = "/var/log/gunicorn/dev.log"
capture_output = True
daemon = True
