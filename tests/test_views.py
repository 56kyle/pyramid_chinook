from pyramid_chinook import models
from pyramid_chinook.views.default import my_view, filtered_employee_view
from pyramid_chinook.views.notfound import notfound_view


def test_my_view(app_request, dbsession):
    one = models.MyModel(name='one', value='TestValue')
    dbsession.add(one)
    dbsession.flush()
    info = my_view(app_request)

    assert app_request.response.status_int == 200
    assert info['one'].name == 'one'


def test_filtered_employee_view_failure(app_request):
    info = filtered_employee_view(app_request)
    assert info.status_int == 500


def test_filtered_employee_view_wrong_attr(app_request):
    app_request.matchdict = {'filter': 'NotAnAttribute', 'value': 'Value'}
    info = filtered_employee_view(app_request)
    assert info.status_int == 518


def test_filtered_employee_view_no_results(app_request):
    app_request.matchdict = {'filter': 'EmployeeId',  'value': '-1'}
    info = filtered_employee_view(app_request)
    assert len(info['employees']) == 0


def test_filtered_employee_view_success(app_request, dbsession, employee_dict):
    for attribute, value in employee_dict.items():
        app_request.matchdict = {'filter': attribute, 'value': value}
        info = filtered_employee_view(app_request)
        assert app_request.response.status_int == 200
        assert getattr(info['employees'][0], attribute) == value


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
