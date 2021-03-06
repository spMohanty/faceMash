# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(
    word.capitalize() for word in request.application.split('_'))
response.subtitle = T('now everyone has one')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'S.P. Mohanty <spmohanty91@gmail.com>'
response.meta.description = 'YourMash'
response.meta.keywords = ''
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################


def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    
_()
