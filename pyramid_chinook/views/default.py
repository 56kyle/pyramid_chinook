from datetime import datetime
import inspect
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='home', renderer='pyramid_chinook:templates/mytemplate.mako')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'pyramid_chinook'}


@view_config(route_name='FilteredEmployee', renderer='pyramid_chinook:templates/employee.mako')
def filtered_employee_view(request):
    try:
        query = request.dbsession.query(models.Employee)
        if not query:
            return {'employees': []}

        if isinstance(getattr(models.Employee, request.matchdict['filter']), datetime):
            filtered_query = query.filter(
                str(getattr(models.Employee, request.matchdict['filter'])) == request.matchdict['value']
            )
        else:
            filtered_query = query.filter(
                getattr(models.Employee, request.matchdict['filter']) == request.matchdict['value']
            )
        if not filtered_query:
            return {'employees': []}
        filtered_query.order_by(models.Employee.EmployeeId)
        employees = filtered_query.all()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    except TypeError:
        return Response('Query has failed.', content_type='text/plain', status=500)
    except AttributeError:
        return Response('Filter is incorrectly spelled or not existent', content_type='text/plain', status=518)
    return {
        'employees': employees
    }


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.md for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""