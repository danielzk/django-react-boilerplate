# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_pagination_should_not_be_shown_if_only_one_page 1'] = ''

snapshots['test_pagination_should_display_some_page_numbers 1'] = '''<ul class="pagination">
 <li>
  <a href="?page=4">
   Previous
  </a>
 </li>
 <li>
  <a href="?page=1">
   1
  </a>
 </li>
 <li>
  <span>
   ...
  </span>
 </li>
 <li>
  <a href="?page=4">
   4
  </a>
 </li>
 <li class="active">
  <a href="#">
   5
  </a>
 </li>
 <li>
  <a href="?page=6">
   6
  </a>
 </li>
 <li>
  <span>
   ...
  </span>
 </li>
 <li>
  <a href="?page=9">
   9
  </a>
 </li>
 <li>
  <a href="?page=6">
   Next
  </a>
 </li>
</ul>
'''

snapshots['test_pagination_should_display_all_page_numbers 1'] = '''<ul class="pagination">
 <li>
  <a href="?page=4">
   Previous
  </a>
 </li>
 <li>
  <a href="?page=1">
   1
  </a>
 </li>
 <li>
  <a href="?page=2">
   2
  </a>
 </li>
 <li>
  <a href="?page=3">
   3
  </a>
 </li>
 <li>
  <a href="?page=4">
   4
  </a>
 </li>
 <li class="active">
  <a href="#">
   5
  </a>
 </li>
 <li>
  <a href="?page=6">
   6
  </a>
 </li>
 <li>
  <a href="?page=7">
   7
  </a>
 </li>
 <li>
  <a href="?page=8">
   8
  </a>
 </li>
 <li>
  <a href="?page=9">
   9
  </a>
 </li>
 <li>
  <a href="?page=6">
   Next
  </a>
 </li>
</ul>
'''

snapshots['test_pagination_should_not_display_next_if_last_page 1'] = '''<ul class="pagination">
 <li>
  <a href="?page=1">
   Previous
  </a>
 </li>
 <li>
  <a href="?page=1">
   1
  </a>
 </li>
 <li class="active">
  <a href="#">
   2
  </a>
 </li>
</ul>
'''

snapshots['test_pagination_display_custom_page_param_links_with_extra_params 1'] = '''<ul class="pagination">
 <li>
  <a href="?custom_page=4&amp;extra=value&amp;extra2=value2">
   Previous
  </a>
 </li>
 <li>
  <a href="?custom_page=1&amp;extra=value&amp;extra2=value2">
   1
  </a>
 </li>
 <li>
  <a href="?custom_page=2&amp;extra=value&amp;extra2=value2">
   2
  </a>
 </li>
 <li>
  <a href="?custom_page=3&amp;extra=value&amp;extra2=value2">
   3
  </a>
 </li>
 <li>
  <a href="?custom_page=4&amp;extra=value&amp;extra2=value2">
   4
  </a>
 </li>
 <li class="active">
  <a href="#">
   5
  </a>
 </li>
 <li>
  <a href="?custom_page=6&amp;extra=value&amp;extra2=value2">
   6
  </a>
 </li>
 <li>
  <a href="?custom_page=7&amp;extra=value&amp;extra2=value2">
   7
  </a>
 </li>
 <li>
  <a href="?custom_page=8&amp;extra=value&amp;extra2=value2">
   8
  </a>
 </li>
 <li>
  <a href="?custom_page=9&amp;extra=value&amp;extra2=value2">
   9
  </a>
 </li>
 <li>
  <a href="?custom_page=6&amp;extra=value&amp;extra2=value2">
   Next
  </a>
 </li>
</ul>
'''
