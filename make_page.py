__author__ = 'Alex'

import sys
from data import data
import markup
import numpy as np

width = 700


def create_page():
    page = markup.page()
    page.init(css=['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'],
              script=['https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js',
                      'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
                      'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js'],
              style="""
        .container {max-width: 700px;}
        .tabs-left, .tabs-right {
        border-bottom: none;
        padding-top: 0px;
        }
        .tabs-left {
        border-right: 1px solid #ddd;
        }
        .tabs-left>li {
        float: none;
        margin-bottom: 0px;
        }
        .tabs-left>li {
        margin-right: -1px;
        }

        .tabs-left>li.active>a,
        .tabs-left>li.active>a:hover,
        .tabs-left>li.active>a:focus {
        border-bottom: 1px solid #ddd;
        border-right-color: transparent;
        }
        .tabs-left>li>a:hover {
        border-bottom: 1px solid #eee;
        }

        .tabs-left>li>a {
        border-radius: 4px 0 0 4px;
        margin-right: 0;
        display:block;
        }
        code {
        color: #000;
        background-color: #eee
        }
         {
        font-size: 30px
        }
        """,
              charset='utf-8')
    page.script("""MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ["\\(","\\)"]], processEscapes: true}});""")

    page.div(class_='container')
    #page.h1('Репетитор по математике', class_='text-center')
    page.h2('<small>+7 926 211 3871</small>', class_='text-right')
    page.div(class_='jumbotron', style='margin-bottom: 10px; padding: 10px 25px')
    page.h2('Репетитор по математике', class_='text-center')
    page.p('Индивидуальные занятия для школьников и абитуриентов')
    page.p('Заполнение пробелов, подготовка к ОГЭ, ЕГЭ, олимпиадам')


    page.div.close()
    page.div.close()

    page.div(class_='container', style='padding-right: 0px; padding-left: 0px;')

    # page.div(role='tabpanel')
    page.div(class_='container')
    page.ul(class_='nav nav-pills pull-right')

    page.li(class_='active')
    kw = {'href': '#main', 'data-toggle': 'tab'}
    page.a('Репетитор', **kw)
    page.li.close()

    for object in data:
        page.li()
        kw = {'href': '#' + object, 'data-toggle': 'tab'}
        page.a(object, **kw)
        page.li.close()
    page.ul.close()
    page.div.close()

    page.div(class_='tab-content')  # , style='margin-top: 15px')

    page.div(class_='tab-pane active', id='main', style='padding-left: 30px; padding-right: 30px')

    page.h4('Березин Иван Евгеньевич')
    page.h5('Профессиональный репетитор школьной и высшей математики')
    page.p('Устранение пробелов в знаниях, подготовка к контрольным, пересдачам, экзаменам. Качественное освоение школьной программы, разъяснение сложных и непонятных тем.')

    page.p('Индивидуальный подход и подбор методики для каждого ученика. Проработка каждого занятия и общей индивидуальной программы с учетом особенностей развития ребенка, выделяемого родителями времени и степенью загруженности ребенка, уровня мотивации ученика, особенностей параллельно работающего школьного учителя, ранее допущенных ошибок и других факторов. Работа по любым учебникам. Составляю собственные задачи в дополнение к учебнику.')

    page.p('Учу понимать и думать, а не зубрить. Выезжаю на дом, а так же провожу занятия у себя.')

    page.h5('Стоимость')
    page.p('С учетом выезда на дом в удобное для Вас время 1000 рублей в час.')
    page.h5('Контакты')

    #page.span(class_='glyphicon glyphicon-phone')
    #page.span.close()
    page.p('tel: +7 926 211 3871')
    page.p('email: mosrepetit@gmail.com')
    page.span(class_='')

    #page.h4('header1')
    #page.p('kjsdf ssdgafh afhag asd asdas dgasd gasdgasd hasd asdfas dgas das dhasdga sdf')
    #page.h4('header2')
    #page.p('asd asdfas dagshas da sdas dfasd gasdgasdhasdhasdasg asdgasdg asd gasdfas dfasdf')
    page.div.close()

    for object in data:
        page.div(class_='tab-pane', id=object)
        page.div(class_='col-xs-3')
        page.ul(class_='nav nav-tabs tabs-left')
        for subject in data[object]:
            page.li()
            kw = {'href': '#' + object + subject, 'data-toggle': 'tab'}
            page.a(subject, **kw)
            page.li.close()
        page.ul.close()
        page.div.close()

        page.div(class_='col-xs-9')
        page.div(class_='tab-content')

        for subject in data[object]:
            page.div(class_='tab-pane', id=object + subject)

            for k in data[object][subject]:
                page.h4(k)  # , style='padding-top: 12px')
                # for m in data[i][j][k]:
                page.p('<br>'.join(data[object][subject][k]))

            page.div.close()  # tab-pane 2

        page.div.close()  # tab-content 2
        page.div.close()

        page.div.close()  # tab-pane 1

    page.div.close()  # tab-content 1



    # page.div.close()    # tabpanel


    page.div.close()  # container

    return page


page = create_page()
oldstdout = sys.stdout
sys.stdout = open('math.html', 'w', encoding='utf-8')
print(page, file=sys.stdout)
sys.stdout = oldstdout
print(page)