# -*- coding: utf-8 -*-
def to_quoted_list(items, quotes='\'', sep=', '):
    quoted = lambda s: quotes + str(s) + quotes
    return sep.join(quoted(item) for item in items)
