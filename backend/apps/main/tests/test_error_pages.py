from project import urls

from ..views import bad_request, page_not_found, permission_denied, server_error


def test_bad_request_error(rf):
    assert urls.handler400 == 'main.views.bad_request'
    response = bad_request(rf.get('/'))
    assert response.status_code == 400
    assert 'Bad request' in response.content.decode('utf-8')


def test_permission_denied_error(rf):
    assert urls.handler403 == 'main.views.permission_denied'
    response = permission_denied(rf.get('/'))
    assert response.status_code == 403
    assert 'Permission denied' in response.content.decode('utf-8')


def test_page_not_found_error(rf):
    assert urls.handler404 == 'main.views.page_not_found'
    response = page_not_found(rf.get('/'))
    assert response.status_code == 404
    assert 'Page not found' in response.content.decode('utf-8')


def test_server_error(rf):
    assert urls.handler500 == 'main.views.server_error'
    response = server_error(rf.get('/'))
    assert response.status_code == 500
    assert 'Server error' in response.content.decode('utf-8')
