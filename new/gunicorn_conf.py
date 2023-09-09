import multiprocessing

bind = '0.0.0.0:80'
workers = 5

backlog = 8192
worker_class = "gevent"
worker_connections = 1000
daemon = False
debug = True
proc_name = 'gunicorn_demo'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
pidfile = './logs/gunicorn.pid'
errorlog = './logs/error.log'
accesslog = "./logs/access.log"
