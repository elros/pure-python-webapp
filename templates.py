# -*- coding: utf-8 -*-

class HTMLGenerator:

    def __init__(self):
        self._html_head = ''
        self._html_body = ''

    def __str__(self):
        return self._html_body

    def get_full_html(self):
        return '<html><head>{head}</head><body>{body}</body></html>'.format(
            head=self._html_head,
            body=self._html_body,
        )

    def p(self, text):
        self._html_body += '<p>{text}</p>\n'.format(
            text=text,
        )
        return self

    def a(self, text, href):
        self._html_body += '<a href="{href}">{text}</a>\n'.format(
            text=text,
            href=href,
        )

    def h1(self, text):
        return self._add_heading(text, '1')

    def h2(self, text):
        return self._add_heading(text, '2')

    def _add_heading(self, text, level):
        tag = 'h{level}'.format(level=level)
        self._html_body += '<{tag}>{text}</{tag}>\n'.format(
            tag=tag,
            text=text,
        )
        return self