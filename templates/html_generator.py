# -*- coding: utf-8 -*-
class HTMLGenerator:

    def __init__(self):
        self._html_head = u''
        self._html_body = u''

    def __unicode__(self):
        return self._html_body

    def __str__(self):
        return unicode(self).encode('utf-8')

    def get_full_html(self):
        return u'<html><head>{head}</head><body>{body}</body></html>'.format(
            head=self._html_head,
            body=self._html_body,
        )

    def text(self, text):
        self._html_body += unicode(text)
        return self


    def p(self, text, **attrs):
        self._html_body += HTMLGenerator._paired_tag(
            tag='p',
            inner_text=text,
            **attrs
        )
        return self

    def a(self, text, href, **attrs):
        self._html_body += HTMLGenerator._paired_tag(
            tag='a',
            inner_text=text,
            href=href,
            **attrs
        )
        return self

    def h1(self, text, **attrs):
        self._html_body += HTMLGenerator._paired_tag(
            tag='h1',
            inner_text=text,
            **attrs
        )
        return self

    def h2(self, text, **attrs):
        self._html_body += HTMLGenerator._paired_tag(
            tag='h2',
            inner_text=text,
            **attrs
        )
        return self

    def ul(self, items, **attrs):
        self._html_body += HTMLGenerator._open_tag('ul', **attrs)
        for item in items:
            self._html_body += HTMLGenerator._paired_tag(
                tag='li',
                inner_text=unicode(item),
            )
        self._html_body += HTMLGenerator._close_tag('ul')
        return self

    def ol(self, items, **attrs):
        self._html_body += HTMLGenerator._open_tag('ol', **attrs)
        for item in items:
            self._html_body += HTMLGenerator._paired_tag(
                tag='li',
                inner_text=unicode(item),
            )
        self._html_body += HTMLGenerator._close_tag('ol')
        return self

    def form(self, action, method, items):
        self._html_body += HTMLGenerator._open_tag(
            tag='form',
            action=action,
            method=method,
        )
        for item in items:
            self._html_body += unicode(item)
        self._html_body += HTMLGenerator._close_tag('form')
        return self

    def input(self, **attrs):
        self._html_body += HTMLGenerator._single_tag('input', **attrs)
        return self

    def br(self, **attrs):
        self._html_body += HTMLGenerator._single_tag('br', **attrs)
        return self

    @staticmethod
    def _single_tag(tag, **attrs):
        return HTMLGenerator._open_tag(tag, **attrs)

    @staticmethod
    def _paired_tag(tag, inner_text, **attrs):
        return HTMLGenerator._open_tag(tag, endl='', **attrs) + unicode(inner_text) + HTMLGenerator._close_tag(tag)

    @staticmethod
    def _open_tag(tag, endl='\n', **attrs):
        if attrs:
            attrs_list = (u'{}="{}"'.format(attr, val) for (attr, val) in attrs.items())
            attrs_str = ' ' + ' '.join(attrs_list)
        else:
            attrs_str = ''

        return u'<{tag}{attrs}>{endl}'.format(
            tag=tag,
            attrs=attrs_str,
            endl=endl
        )

    @staticmethod
    def _close_tag(tag, endl='\n'):
        return u'</{tag}>{endl}'.format(
            tag=tag,
            endl=endl
        )