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
        self._html_body += HTMLGenerator._html_tag(
            tag='p',
            inner_text=text,
        )
        return self

    def a(self, text, href):
        self._html_body += HTMLGenerator._html_tag(
            tag='a',
            inner_text=text,
            href=href,
        )
        return self

    def h1(self, text):
        self._html_body += HTMLGenerator._html_tag(
            tag='h1',
            inner_text=text,
        )
        return self

    def h2(self, text):
        self._html_body += HTMLGenerator._html_tag(
            tag='h2',
            inner_text=text,
        )
        return self

    @staticmethod
    def _html_tag(tag, inner_text, **attributes):
        if attributes:
            attrs_list = (attr + '="' + val + '"' for (attr, val) in attributes.items())
            attrs_str = ' ' + ' '.join(attrs_list)
        else:
            attrs_str = ''

        return '<{tag}{attrs}>{text}</{tag}>\n'.format(
            tag=tag,
            attrs= attrs_str,
            text=inner_text,
        )