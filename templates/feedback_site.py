# -*- coding: utf-8 -*-
from templates.html_generator import HTMLGenerator


class FeedbackSiteGenerator:

    def get_comment_page(self):
        gen = HTMLGenerator()
        gen.h1(u'Оставить комментарий')
        gen.form(
            action='/comment/',
            method='post',
            items=[
                HTMLGenerator()
                .text(u'Фамилия:').br()
                .input(type='text', name='last_name').br()
                .text(u'Имя:').br()
                .input(type='text', name='first_name').br()
                .text(u'Отчество:').br()
                .input(type='text', name='middle_name').br()
            ]
        )
        return gen.get_full_html()
