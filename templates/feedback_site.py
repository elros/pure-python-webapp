# -*- coding: utf-8 -*-
from templates.html_generator import HTMLGenerator


class FeedbackSiteGenerator:

    def __init__(self, db):
        self._db = db

    def get_comment_page(self):
        gen = HTMLGenerator()
        gen.h1(u'Оставить комментарий')
        gen.form(
            action='/comment/',
            method='post',
            items=[
                HTMLGenerator()

                .span(u'Фамилия:').span('*', style='color: red').br()
                .input(type='text', name='last_name', size='30').br()

                .span(u'Имя:').span('*', style='color: red').br()
                .input(type='text', name='first_name', size='30').br()

                .span(u'Отчество:').br()
                .input(type='text', name='middle_name', size='30').br()

                .span(u'Регион:').br()
                .select(
                    name='region',
                    items=[
                        HTMLGenerator().option(
                            inner_text='',
                            style='display:none',
                            selected='true',
                        )
                    ] + [
                        HTMLGenerator().option(
                            inner_text=name,
                            value=unicode(id),
                        )
                        for (id, name,) in self._db.get_regions_list()
                    ]
                )
                .br()

                .span(u'Город:').br()
                .select(
                    name='city',
                    items=[
                        HTMLGenerator().option(
                            inner_text=u'(Выберите регион)'
                        )
                    ],
                    disabled='true',
                )
                .br()

                .span(u'Контактный телефон:').br()
                .input(type='text', name='phone_number', size='30').br()

                .span(u'E-mail:').br()
                .input(type='text', name='email', size='30').br()

                .span(u'Комментарий:').span('*', style='color: red').br()
                .textarea(
                    inner_text='',
                    rows='12',
                    cols='50',
                )
                .br()

                .span(u'* - обязательные поля', style='color: red').br()

                .br()
                .input(type='submit', value=u'Отправить').br()
            ]
        )
        return gen.get_full_html()
