from pyramid_chinook import models
from .test_views import gen_employee


def test_my_view_success(testapp, dbsession):
    model = models.MyModel(name='one', value=55)
    dbsession.add(model)
    dbsession.flush()

    res = testapp.get('/', status=200)
    assert res.body


def test_country_employee_view_success(testapp, dbsession):
    gen_employee(dbsession)
    res = testapp.get('/Employee/Country/FakeCountry', status=200)
    assert res.body


def test_city_employee_view_success(testapp, dbsession):
    gen_employee(dbsession)
    res = testapp.get('/Employee/City/FakeCity', status=200)
    assert res.body


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
