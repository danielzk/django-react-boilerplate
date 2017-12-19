from django.core.paginator import (
    Paginator as DjangoPaginator, EmptyPage, PageNotAnInteger
)

SIDE_PAGES_TOTAL = 3
PER_PAGE = 20
PAGE_PARAM = 'page'


class Paginator(DjangoPaginator):
    def __init__(self, *args, **kwargs):
        self.side_pages_total = kwargs.pop('side_pages_total', SIDE_PAGES_TOTAL)
        self.page_param = kwargs.pop('page_param', PAGE_PARAM)
        super().__init__(*args, **kwargs)


def paginate(request, objs, per_page=PER_PAGE, side_pages_total=SIDE_PAGES_TOTAL,
             page_param=PAGE_PARAM):
    paginator = Paginator(
        objs, per_page, page_param=page_param,
        side_pages_total=side_pages_total
    )

    try:
        page = request.GET.get(page_param)
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return objs
