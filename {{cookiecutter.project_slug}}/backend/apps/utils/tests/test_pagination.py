from django.shortcuts import render

from bs4 import BeautifulSoup

from ..pagination import paginate


def _test_snapshot(request, page_obj, snapshot):
    response = render(request, 'includes/pagination.html', context={'page_obj': page_obj})
    output = BeautifulSoup(response.content, 'html.parser').prettify()
    snapshot.assert_match(output)


def test_pagination_should_not_be_shown_if_only_one_page(rf, snapshot):
    request = rf.get('/')
    page_obj = paginate(request, range(1), 1)
    _test_snapshot(request, page_obj, snapshot)


def test_pagination_should_display_some_page_numbers(rf, snapshot):
    request = rf.get('/?page=5')
    page_obj = paginate(request, range(9), 1, side_pages_total=1)
    _test_snapshot(request, page_obj, snapshot)


def test_pagination_should_display_all_page_numbers(rf, snapshot):
    request = rf.get('/?page=5')
    # first, 3 left, actual, 3 right, last
    page_obj = paginate(request, range(9), 1, side_pages_total=3)
    _test_snapshot(request, page_obj, snapshot)


def test_pagination_should_not_display_next_if_last_page(rf, snapshot):
    request = rf.get('/?page=2')
    page_obj = paginate(request, range(2), 1)
    _test_snapshot(request, page_obj, snapshot)


def test_pagination_display_custom_page_param_links_with_extra_params(rf, snapshot):
    request = rf.get('/?extra=value&extra2=value2&custom_page=5')
    page_obj = paginate(request, range(9), 1, page_param='custom_page')
    _test_snapshot(request, page_obj, snapshot)
