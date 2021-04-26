from pyramid_chinook import models
import datetime


def test_country_employee_view_success(testapp, dbsession):
    res = testapp.get('/Employee/Country/FakeCountry', status=200)
    assert res.body


def test_city_employee_view_success(testapp, dbsession):
    employee = models.Employee(
        LastName='Smith',
        FirstName='John',
        Title='Manager',
        ReportsTo=1,
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
    res = testapp.get('/Employee/City/FakeCity', status=200)
    assert res.body


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
