import datetime
from pyramid_chinook import models
from pyramid_chinook.views.default import my_view, country_employee_view, city_employee_view
from pyramid_chinook.views.notfound import notfound_view


def test_my_view_failure(app_request):
    info = my_view(app_request)
    assert info.status_int == 500


def test_my_view_success(app_request, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    info = my_view(app_request)
    assert app_request.response.status_int == 200
    assert info['one'].name == 'one'
    assert info['project'] == 'pyramid_chinook'


def test_country_employee_view_failure(app_request):
    info = country_employee_view(app_request)
    assert info.status_int == 500


def test_country_employee_view_success(app_request, dbsession):
    gen_employee(dbsession)

    info = country_employee_view(app_request)
    assert app_request.response.status_int == 200
    assert info['employees'][0].Country == 'FakeCountry'
    assert len(info['employees']) == 1


def test_city_employee_view_failure(app_request):
    info = city_employee_view(app_request)
    assert info.status_int == 500


def test_city_employee_view_success(app_request, dbsession):
    gen_employee(dbsession)

    info = city_employee_view(app_request)
    assert app_request.response.status_int == 200
    assert info['employees'][0].City == 'FakeCity'
    assert len(info['employees']) == 1


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}


def gen_employee(dbsession):
    employee = models.Employee(
        LastName='Smith',
        FirstName='John',
        Title='Manager',
        # ReportsTo=None,
        BirthDate=datetime.datetime(1990, 1, 1, 1, 1, 1, 1),
        HireDate=datetime.datetime(2020, 1, 1, 1, 1, 1, 1),
        Address='0000 NotARealPlace Ln.',
        City='FakeCity',
        State='FakeState',
        Country='FakeCountry',
        PostalCode='99999',
        Phone='(999)999-9999',
        Fax='(999)999-9998',
        Email='JohnSmithTheManager@notasite.com'
    )
    dbsession.add(employee)
    dbsession.flush()
