from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='frontend'),
    host(r'panel', 'fitness_club_app.url_backend', name='backend'),
    host(r'admin', 'fitness_club_app.url_admin', name='admin'),
)