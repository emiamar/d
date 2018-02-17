#!/usr/bin/env python


import xmlrpclib

from django.conf.settings import config

user = config.get('cloud_server_provider', 'webfaction_username')
password = config.get('cloud_server_provider', 'webfation_password')


class Webfaction(object):

    def __init__(self, project_name):
        self.server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
        self.session_id, self.account = self.server.login(user, password)
        self.project_name = project_name

    def create_application(
        self,
        application_type='django-1.9.13_mod_wsgi-4.5.15_python-2.7'
    ):
        self.server.create_app(
            self.session_id,
            self.project_name,
            application_type
        )

    def create_domain(self):
        domain_name = "greendesignlabs.in"
        response = self.server.create_domain(
            self.session_id, domain_name,
            self.project_name,
            'www.{0}'.format(self.project_name))
        setattr(self, 'create_domain_response', response)

    def create_website(self):
        subdomains = [subdomain + self.create_domain_response['domain'] for subdomain in self.create_domain_response['subdomains']]
        self.server.create_website(
            self.session_id,
            self.project_name,
            '119.81.68.118',
            False,
            subdomains,
            [self.project_name, '/']
        )


    # To Do:
    # Delete bin lib and myproject folders.
    # Create Project Source code