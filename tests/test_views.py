from pyramid_chinook import models
from pyramid_chinook.views.default import my_view, country_employee_view, city_employee_view
from pyramid_chinook.views.notfound import notfound_view


def test_my_view(app_request, dbsession):
    one = models.MyModel(name='one', value='TestValue')
    dbsession.add(one)
    dbsession.flush()
    info = my_view(app_request)

    assert app_request.response.status_int == 200
    assert info['one'].name == 'one'


def test_country_employee_view_failure(app_request):
    info = country_employee_view(app_request)
    assert info.status_int == 500


def test_country_employee_view_success(app_request, dbsession, employee):
    app_request.matchdict = {'country': 'FakeCountry'}
    info = country_employee_view(app_request)
    assert app_request.response.status_int == 200
    assert info['employees'][0].Country == 'FakeCountry'
    assert len(info['employees']) == 1


def test_city_employee_view_failure(app_request):
    info = city_employee_view(app_request)
    assert info.status_int == 500


def test_city_employee_view_success(app_request, dbsession, employee):
    app_request.matchdict = {'city': 'FakeCity'}
    info = city_employee_view(app_request)
    assert app_request.response.status_int == 200
    assert info['employees'][0].City == 'FakeCity'
    assert len(info['employees']) == 1


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
