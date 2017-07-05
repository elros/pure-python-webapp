# -*- coding: utf-8 -*-
from html_generator import HTMLGenerator


class FeedbackSiteGenerator:

    def get_comment_page(self):
        gen = HTMLGenerator()
        gen.h1(u'Оставить комментарий')
        gen.form(
            action='/comment/',
            method='post',
            items=[
                HTMLGenerator()
                .p('will be here...')
                .p('another one')
            ]
        )
        return gen.get_full_html()
