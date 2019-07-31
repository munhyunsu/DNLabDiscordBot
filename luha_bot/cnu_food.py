import time
import datetime
import random
import urllib.request
import urllib.parse

import pandas

class CNUFood(object):
    def __init__(self):
        """
        Load saved cache, ready to save data
        """
        self.last_time = time.time()
        self.table = self._scrap_menu()

    def _scrap_menu(self):
        table = dict()
        url = 'http://cnuis.cnu.ac.kr/jsp/etc/toWeekMenu.jsp'
        data = {'cafe_div_cd': None, 
                'food_div_cd': None,
                'langType': None}
        cafe_op = {'교직원': 'CCS01.10',
                   '학생': 'CCS01.20'}
        food_op = {'조식': 'CCS02.10',
                   '중식': 'CCS02.20',
                   '석식': 'CCS02.30',
                   '일품(중식)': 'CCS02.40',
                   '일품(석식)': 'CCS02.50'}
        lang_op = {'한글': '1',
                   '영어': '2',
                   '중국어': '3'}
        
        for ckey in cafe_op.keys():
            #for fkey in food_op.keys():
            for fkey in ['중식', '일품(중식)']:
                #for lkey in lang_op.keys():
                for lkey in ['한글']:
                    data['cafe_div_cd'] = cafe_op[ckey]
                    data['food_div_cd'] = food_op[fkey]
                    data['langType'] = lang_op[lkey]
                    body = urllib.parse.urlencode(data).encode('utf-8')
                    with urllib.request.urlopen(url, data=body) as r:
                        tdata = pandas.read_html(r)
                        key = '&'.join([ckey, fkey, lkey])
                        table[key] = tdata[1]
                    time.sleep(random.randint(0, 2))
        return table

    def update_table(self):
        now = time.time()
        if (now - self.last_time) > 60*60*24:
            self.table = self.scrap_menu()
            self.last_time = now
            return True
        return False

    def get_food(self):
        self.update_table()
        w = datetime.datetime.now().isoweekday()
        if w == 7:
            return '일요일 영업 안 함'
        w = w + 1
        table = self.table
        foods = '[2학생회관:학생]'
        for food in table['학생&중식&한글'][4][w].split():
            if food.isdigit() or '(' in food or ')' in food or 'beef' in food:
                continue
            foods = '{0}\n{1}'.format(foods, food)
        foods = '{0}\n{1}'.format(foods, '[2학생회관:일품]')
        for food in table['학생&일품(중식)&한글'][4][w].split():
            if food.isdigit() or '(' in food or ')' in food or 'beef' in food:
                continue
            foods = '{0}\n{1}'.format(foods, food)
        foods = '{0}\n{1}'.format(foods, '[2학생회관:교직원]')
        for food in table['교직원&중식&한글'][4][w].split():
            if food.isdigit() or '(' in food or ')' in food or 'beef' in food:
                continue
            foods = '{0}\n{1}'.format(foods, food)
        return foods


if __name__ == '__main__':
    cf = CNUFood()
    print(cf.get_food(None, None))

