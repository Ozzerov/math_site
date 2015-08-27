__author__ = 'Alex'

from collections import OrderedDict

data = OrderedDict([('Алгебра', OrderedDict([('уравнения', OrderedDict()),
                                             ('степени', OrderedDict()),
                                             ('логарифмы', OrderedDict())])),
                    ('Геометрия', OrderedDict([('треугольник', OrderedDict()),
                                               ('прямоугольник', OrderedDict()),
                                               ('квадрат', OrderedDict()),
                                               ('параллелограмм', OrderedDict()),
                                               ('ромб', OrderedDict()),
                                               ('трапеция', OrderedDict()),

                                               ('треугольник', OrderedDict())])),
                    ('Тригонометрия', OrderedDict([('уравнения', OrderedDict()),
                                                   ('степения', OrderedDict()),
                                                   ('логарифмы', OrderedDict())]))])

data['Алгебра']['уравнения']['формулы сокращенного умножения'] = ['$(a \pm b)^2 = a^2 \pm 2ab - b^2$',
                                                                  '$(a \pm b)^3 = a^3 \pm 3a^2 b + 3ab^2 \pm b^3$']
data['Алгебра']['уравнения']['формулы'] = ['$ax^2 + bx + c = 0$ <code>квадратное уравнение</code>',
                                           '$D = b^2 - 4ac$ <code>дискриминант</code>',
                                           '$x_{1,2} = \\frac{-b \pm \sqrt D}{2a}$ <code>корни</code>']
data['Алгебра']['степени']['свойства'] = ['$(ab)^n = a^n n^n$',
                                          '$\left(\\frac{a}{b}\\right)^n = \\frac{a^n}{b^n}$',
                                          '$a^n a^m = a^{n+m}$',
                                          '$\\frac{a^n}{a^m} = a^{n-m}$',
                                          '$\left(a^n\\right)^m = a^{n m}$',
                                          '$a^{-b} = \\frac{1}{a^b}$',
                                          '$a^{\\frac{p}{q}} = \sqrt[q]{a^p} = \left(\sqrt[q]{a}\\right)^p$']

data['Алгебра']['логарифмы']['определения'] = ['$x = \log_a{b}$ <code>логарифм</code> $a$ <code>по основанию</code> $b$',
                                               '<code>по определению является решением уравнения</code> $a^x = b$',
                                               '$\ln{b}$ <code>натуральный логарифм по основанию</code> $e$)']

data['Алгебра']['логарифмы']['свойства'] = ['$a^{\log_a{b}} = b$ <code>основное логарифмическое тождество</code>',
                                            '$\log_a{1} = 0$ <code>логарифм единицы равен нулю</code>',
                                            '$\log_a{a} = 1$',
                                            '$\log_a{x y} = \log_a{x} + \log_a{y}$ <code>логарифм произведения</code>',
                                            '$\log_a{\\frac{x}{y}} = \log_a{x} - \log_a{y}$ <code>логарифм частного</code>',
                                            '$\log_a{x^p} = p \log_a{x}$ <code>степень выносится за знак логарифма</code>',
                                            '$\log_a{\sqrt[p]{x}} = \\frac{\log_a{x}}{p}$ <code>корень выносится за знак логарифма</code>',
                                            '$\log_a{b} = \\frac{\log_c{b}}{\log_c{a}}$ <code>замена основания логарифма</code>']

data['Алгебра']['логарифмы']['следствия'] = ['$\log_a{b} = \\frac{1}{\log_b{a}}$',
                                             '$\log_{a^q}{b^p} = \\frac{p}{q} \log_a{b}$',
                                             '$c^{\log_a{b}} = b^{\log_a{c}}$']




data['Геометрия']['треугольник']['обозрачения'] = ['$a$ <code>сторона</code>',
                                                   '$S$ <code>площадь</code>',
                                                   '$p$ <code>полупериметр</code>']

data['Геометрия']['треугольник']['формулы'] = ['$S = \\frac{h a}{2} = \\frac{1}{2} h a = \sqrt{p (p-a) (p-b) (p-c)}$ <code>площадь</code>',
                                               '$S = \\frac{h a}{2} = \\frac{1}{2} h a = \sqrt{p (p-a) (p-b) (p-c)}$ <code>площадь</code>',
                                                   ]

data['Геометрия']['треугольник']['afgasfasfas'] = ['<code>1512512515</code>']


data['Геометрия']['квадрат']['свойства'] = ['все стороны равны',
                                            'все углы прямые $(90^{\circ})$',
                                            'диагонали равны, пересекаются под углом $90^{\circ}$, точкой пересечения делятся пополам и делят все углы квадрата пополам']

print(data)


import make_page