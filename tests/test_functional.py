from pyramid_chinook import models
import datetime


def test_filtered_employee_view_success(testapp, dbsession):
    res = testapp.get('/Employee/City/FakeCity', status=200)
    assert res.body


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
