# -*- coding: utf-8 -*-
from templates.html_generator import HTMLGenerator
import util


class FeedbackSiteGenerator:

    def __init__(self, db):
        self._db = db

    def get_comment_form_page(self):
        page = HTMLGenerator()

        page.js_script(util.get_js_scipt('scripts.js'))

        page.h1(u'Оставить комментарий')
        page.form(
            action='/comment/',
            method='post',
            onsubmit='return checkCommentForm();',
            items=[
                HTMLGenerator()

                .span(u'Фамилия:').span('*', style='color: red').br()
                .input(type='text', id='last_name_input', name='last_name', size='30').br()

                .span(u'Имя:').span('*', style='color: red').br()
                .input(type='text', id='first_name_input', name='first_name', size='30').br()

                .span(u'Отчество:').br()
                .input(type='text', id='middle_name_input', name='middle_name', size='30').br()

                .span(u'Регион:').br()
                .select(
                    id='region_selector',
                    name='region_id',
                    onchange='loadCitiesForSelectedRegion()',
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
                    id='city_selector',
                    name='city_id',
                    items=[
                        HTMLGenerator().option(
                            inner_text=u'(Выберите регион)'
                        )
                    ],
                    disabled='true',
                )
                .br()

                .span(u'Контактный телефон (формат: (999)9999999):').br()
                .input(type='text', id='phone_number_input', name='phone_number', size='30').br()

                .span(u'E-mail:').br()
                .input(type='text', id='email_input', name='email', size='30').br()

                .span(u'Комментарий:').span('*', style='color: red').br()
                .textarea(
                    name='feedback_text',
                    id='feedback_text_input',
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

        page.br().br().div(self._get_site_navigation_panel())

        return page.get_full_html()

    def get_comments_list_page(self):
        comments = self._db.get_comments_list()
        comments_sorted_by_newest = sorted(
            comments,
            key=(lambda comment: comment.id),
            reverse=True,
        )

        page = HTMLGenerator()
        page.h1(u'Список комментариев')

        for comment in comments_sorted_by_newest:
            page_part = HTMLGenerator()

            full_name = ' '.join([comment.last_name, comment.first_name, (comment.middle_name or '')])
            page_part.b(u'ФИО: ').span(full_name).br()

            region_name = self._db.get_region_name(comment.region_id)
            city_name = self._db.get_city_name(comment.city_id)
            page_part.b(u'Регион/город: ').span(
                (region_name or '-' ) +
                '/' +
                (city_name or '-')
            ).br()

            page_part.b(u'Контактный телефон:').span(comment.phone_number or '-').br()
            page_part.b(u'E-mail: ').span(comment.email or '-').br()

            page_part.b(u'Комментарий:').br()
            page_part.span(
                comment.feedback_text.replace('\n', '<br>')
            ).br()

            page_part.form(
                action='/comment/{id}/delete/'.format(id=comment.id),
                method='post',
                items=[
                    HTMLGenerator()
                        .input(type='submit', value=u'Удалить')
                ]
            )

            page.div(page_part)
            page.br().br()

        page.br().br().div(self._get_site_navigation_panel())

        return page.get_full_html()

    def get_thanks_page(self):
        page = HTMLGenerator()
        page.h2(u'Спасибо за ваш комментарий!')
        page.br().br().div(self._get_site_navigation_panel())
        return page.get_full_html()

    def get_regions_statistics_summary_page(self):
        page = HTMLGenerator()
        page.h1(u'Статистика комментариев по регионам')

        page.table(
            thead=[
                u'Регион',
                u'Количество комментариев',
            ],
            tbody=[
                [
                    HTMLGenerator().a(
                        text=region_name,
                        href='/stat/region/{id}/'.format(id=region_id),
                    ),
                    comments_count
                ]
                for (region_id, region_name, comments_count) in self._db.get_regions_comment_statistics()
            ]
        )

        page.br().br().div(self._get_site_navigation_panel())
        return page.get_full_html()

    def get_region_detailed_statistics_page(self, region_id):
        page = HTMLGenerator()
        region_name = self._db.get_region_name(region_id)
        page.h1(u'Статистика комментариев ({name})'.format(name=region_name))

        page.table(
            thead=[
                u'Город',
                u'Количество комментариев'
            ],
            tbody=[
                [
                    city.name,
                    self._db.get_city_comments_count(city.id),
                ]
                for city in self._db.get_cities_by_region(region_id)
            ]
        )

        page.br().br().div(self._get_site_navigation_panel())
        return page.get_full_html()

    def _get_site_navigation_panel(self):
        page_part = HTMLGenerator()
        page_part.h2(u'Навигация')
        page_part.ul(
            items=[
                HTMLGenerator().a(text, link)
                for (text, link) in [
                    (u'Форма создания комментария', '/comment/'),
                    (u'Список комментариев', '/view/'),
                    (u'Статистика комментариев', '/stat/'),
                ]
            ]
        )
        return page_part
