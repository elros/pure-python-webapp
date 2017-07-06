# -*- coding: utf-8 -*-
from templates.html_generator import HTMLGenerator
from database.feedback_db import FeedbackDatabase


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

                .text(u'Фамилия:').br()
                .input(type='text', name='last_name', size='30').br()

                .text(u'Имя:').br()
                .input(type='text', name='first_name', size='30').br()

                .text(u'Отчество:').br()
                .input(type='text', name='middle_name', size='30').br()

                .text(u'Регион:').br()
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

                .text(u'Город:').br()
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

                .text(u'Контактный телефон:').br()
                .input(type='text', name='phone_number', size='30').br()

                .text(u'E-mail:').br()
                .input(type='text', name='email', size='30').br()

                .text(u'Комментарий:').br()
                .textarea(
                    inner_text='',
                    rows='12',
                    cols='50',
                )
                .br()

                .br()
                .input(type='submit', value=u'Отправить').br()
            ]
        )
        return gen.get_full_html()
