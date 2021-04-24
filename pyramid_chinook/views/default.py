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


@view_config(route_name='Employee', renderer='pyramid_chinook:templates/employee.mako')
def my_view(request):
    try:
        query = request.dbsession.query(models.Employee)
        one = query.filter(models.Employee.EmployeeId == request.matchdict['id']).one()
    except SQLAlchemyError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {
        'employee_id': one.EmployeeId,
        'last_name': one.LastName,
        'first_name': one.FirstName,
        'title': one.Title,
        'reports_to': one.ReportsTo,
        'birth_date': one.BirthDate,
        'hire_date': one.HireDate,
        'address': one.Address,
        'city': one.City,
        'state': one.State,
        'country': one.Country,
        'postal_code': one.PostalCode,
        'phone': one.Phone,
        'fax': one.Fax,
        'email': one.Email
    }


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
