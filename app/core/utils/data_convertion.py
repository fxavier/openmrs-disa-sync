from datetime import datetime
from core.utils.constants import Constants


class DataConversion:
    @staticmethod
    def format_nid(str_nid):
        if str_nid.startswith('ART') and str(str_nid).find('_') == -1:
            if len(str_nid.split('.')[1]) == 16:
                nid = str_nid.split('.')[1]
                return '0' + str(nid[0:9]) + Constants.SLASH + \
                    str(Constants().get_years().get(
                        nid[9:11])) + Constants.SLASH + str(nid[11:])
            elif str(str_nid).find('/') == -1 and len(str(str_nid)) == 21:
                return str(str_nid)
            elif str(str_nid).startswith('0'):
                return ''
            elif str(str_nid).find('_') == -1 or str(str_nid).find('/') == -1 and len(str(str_nid)) < 21:
                return ''
        else:
            return ''

    @staticmethod
    def convert_to_datetime(str_date):
        if str_date == '':
            date_str_format = '1900-01-01 00:00:00'
        else:
            date_str_format = str_date[5:] + '-' + \
                Constants().get_months().get(
                    str_date[2:5]) + '-' + str_date[0:2] + ' 00:00:00'
        return datetime.strptime(date_str_format, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def format_datetime(date):
        return date.strftime('%Y-%m-%d %H:%M:%S')
