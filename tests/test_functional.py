from pyramid_chinook import models
import datetime
import inspect


def test_filtered_employee_view_success(testapp, dbsession, employee_dict):
    for attribute, value in employee_dict.items():
        res = testapp.get('/Employee/{}/{}'.format(attribute, value), status=200)
        assert res.body


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
