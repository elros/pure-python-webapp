# -*- coding: utf-8 -*-
from templates.html_generator import HTMLGenerator


class FeedbackSiteGenerator:

    def __init__(self, db):
        self._db = db

    def get_comment_form_page(self):
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
                            inner_text=region.name,
                            value=unicode(region.id),
                        )
                        for region in self._db.get_regions_list()
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

    def get_comments_list_page(self):
        comments = self._db.get_comments_list()
        comments_sorted_by_newest = sorted(
            comments,
            key=(lambda comment: comment.id),
            reverse=True,
        )

        gen = HTMLGenerator()
        gen.h1(u'Список комментариев')
        for comment in comments_sorted_by_newest:
            full_name = comment.last_name + comment.first_name + (comment.middle_name)
            gen.p(
                HTMLGenerator()
            )
        return gen.get_full_html()

    def get_thanks_page(self):
        gen = HTMLGenerator()
        gen.h2(u'Спасибо за ваш комментарий!')
        gen.a(u'Назад к форме', '/comment/')
        return gen.get_full_html()