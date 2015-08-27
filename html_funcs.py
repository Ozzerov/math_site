__author__ = 'alex'

import markup
import numpy as np


def create_page(header):
    page = markup.page()
    page.init(css=['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css',
                   'https://raw.githubusercontent.com/dbtek/bootstrap-vertical-tabs/master/bootstrap.vertical-tabs.min.css'],
              script=['http://code.jquery.com/jquery-latest.js',
                      'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full',
                      'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js'],
              charset='utf-8')
    page.div(class_='container', style='max-width: 520px')
    page.div(class_='page-header')
    page.h1(header, class_='text-center')
    page.div.close()
    page.div.close()
    return page


def fill_content(page, data):
    page.div(class_='container', style='max-width: 700px')                          # 1

    page.div(role='tabpanel')                                                       # 2
    page.div(class_='container', style='max-width: 640px')
    page.ul(class_='nav nav-pills navbar-right', role='tablist')
    f1 = 1
    for i in sorted(data):
        if f1:
            page.li(role='presentation', class_='active')
            f1 = 0
        else:
            page.li(role='presentation')
        kw = {'href': '#' + i, 'aria-controls': i, 'role': 'tab', 'data-toggle': 'tab'}
        page.a(i, **kw)
        page.li.close()
    page.ul.close()
    page.div.close()

    page.div(class_='tab-content')                                                  # 3

    f2 = 1
    for i in sorted(data):
        if f2:
            page.div(role='tabpanel ', class_='tab-pane active', id=i)              # 4
            f2 = 0
        else:
            page.div(role='tabpanel', class_='tab-pane', id=i)

        page.div(class_='col-xs-3')                                                 # 5

        page.ul(class_='nav nav-tabs tabs-left')
        ft3 = 1
        for j in sorted(data[i]):
            if ft3:
                page.li(class_='active')
                ft3 = 0
            else:
                page.li()
            kw = {'href': '#' + j, 'data-toggle': 'tab'}
            page.a(j, **kw)
            page.li.close()
        page.ul.close()
        page.div.close()                                                            # -5

        page.div(class_='col-xs-9')                                                 # 5
        ft4 = 1
        page.div(class_='tab-content')                                              # 6
        for j in sorted(data[i]):
            if ft4:
                page.div(class_='tab-pane active', id=j)                            # 7
                ft4 = 0
            else:
                page.div(class_='tab-pane', id=j)

            page.p(str(np.random.rand()))

            page.div.close()                                                        # -7

        page.div.close()                                                            # -6
        page.div.close()                                                            # -5


        page.div.close()                                                            # -4


    page.div.close()                                                                # -3

    page.div.close()                                                                # -2

    page.div.close()                                                                # -1


    pass


