from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'rollbartest'}


@view_config(route_name='error')
def error(request):
    foo()
