# -*- coding: utf-8 -*-

B = {
    'select_in' : {'t': 'x', 's': '//A[@class="changeBoxContainer"][text()="Вход"]'},
    'login'     : {'t': 'x', 's': '//INPUT[@id="inputLogin"]'},
    'password'  : {'t': 'x', 's': '//INPUT[@id="inputPassword"]'},
    'a-button'  : {'t': 'x', 's': '//INPUT[@name="submit_login"]'},
    'tiles'     : {'t': 'x', 's': '//DIV[@class="tiles-list-wrapper"]//A[@href]'},
    'tiles-name': {'t': 'x', 's': '//DIV[@class="tiles-list-wrapper"]//A[@href]', 'a': 'text'},
    'tiles-href': {'t': 'x', 's': '//DIV[@class="tiles-list-wrapper"]//A[@href]', 'a': 'href'},
    'tiles-img' : {'t': 'x', 's': '//DIV[@class="tiles-list-wrapper"]//IMG[@src]', 'a': 'src'},
    'tiles-offl': {'t': 'x', 's': '//I[@class="icn icn-circleOnline-small icn-small info-online js-info-online"]'
                                  '/..', 'a': 'href'},
    'tiles-onln': {'t': 'x', 's': '//I[@class="icn icn-circleOnline-small icn-small info-online js-info-online show"]'
                                  '/..', 'a': 'href'},
  'anketa-about': {'t': 'x', 's': '//DIV[@class="b-anketa_inset b-anketa_inset-info"]', 'a': 'outerHTML'},
   'anketa-msg' : {'t': 'x', 's': '//DIV[@class="b-profile-cloud-inner__message alien"]', 'a': 'text'},
 'anketa-favour': {'t': 'x', 's': '//DIV[@class="in clearFix"]', 'a': 'text'},
    'anketa-btn': {'t': 'x', 's': '//A[@class="button button-blue first  _openChateg "]', 'a': 'href'},
'anketa-locator': {'t': 'x', 's': '//SPAN[@class="info info-misc__distance"]', 'a': 'text'},
    'back-find' : {'t': 'x', 's': '//A[@class="widget-title js-widget-title"][text()="Результаты поиска"]'},

    'open-fotos': {'t': 'x', 's': '//DIV[@class="anketa-photo"]/IMG'},
    'big-foto'  : {'t': 'x', 's': '//IMG[@class="photo-image"]', 'a': 'src'},
    'all-fotos' : {'t': 'x', 's': '//IMG[@class="album-image"]'},
   'close-fotos': {'t': 'x', 's': '//DIV[@class="close-button close-button-hovered"]|//DIV[@class="close-button"]'},
}



#   'okved-listA': {'t': 'x', 's': '//DIV[@sbisname="okvedSelector"]//TR[@data-id]//DIV[@title]', 'a': 'title'},
#   'okved-listD': {'t': 'x', 's': '//DIV[@sbisname="okvedSelector"]//TR[@data-id]//DIV[@title="'},


LINK = [
    'Нет интереса',
    'Пара',
    'Не начинал',
    'Мой интерес',
    'Переписка',
    'Взаимная симп.',
    'Встреча',
    'Доверие',
]

PEOPLE = [
    'Упырь',
    'Продажа',
    'Барыга',
    'Недалекая',
    'Нет КПД',
    'Не верит',
    'Нет места',
    'Неизвестная',
    'Услышала',
    'Проводник',
]

ONLINE = [
    '3 дня',
    'пофиг'
]

ISHTML = [
    'Нет',
    'Есть',
    'пофиг'
]

