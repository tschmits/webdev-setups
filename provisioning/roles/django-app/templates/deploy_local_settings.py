DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['{{wan_server_ip}}', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': '{{django_postgres_pass}}',
        'HOST': '{{db_server_ip}}',
        'PORT': '{{postgresql_port}}',
    }
}
