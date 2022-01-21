class Constants:

    BASE_URL = 'http://192.168.182.132:8080/openmrs/'

    UUIDS = {
        'encounter_type': 'e2790f68-1d5f-11e0-b929-000c29ad1d07',
        'encounter_role': 'a0b03050-c99b-11e0-9572-0800200c9a66',
        'provider': '7013d271-1bc2-4a50-bed6-8932044bc18f',
        'data_colheita_obs': 'f85e3f84-a255-412a-aa43-40174f69c305',
        'data_pedido_obs': '892a98b2-9c98-4813-b4e5-0b434d14404d',
        'valor_carga_concept': 'e1d6247e-1d5f-11e0-b929-000c29ad1d07',
        'qualidade_carga_question': 'e1da2704-1d5f-11e0-b929-000c29ad1d07',
        'hpt': 'a920a302-8c66-44d4-b4c1-6e4a7c30fabc',
        'form': '8377e4ff-d0fe-44a5-81c3-74c9040fd5f8'
    }

    QUALIDADE_CARGA = {
        'indectetavel': 23814,
        '< 400 copies / ml': 23908
    }

    MONTHS = {
        'JAN': '01',
        'FEV': '02',
        'MAR': '03',
        'ABR': '04',
        'MAI': '05',
        'JUN': '06',
        'JUL': '07',
        'AGO': '08',
        'SET': '09',
        'OUT': '10',
        'NOV': '11',
        'DEZ': '12'
    }

    YEARS = {
        '90': '1990',
        '91': '1991',
        '92': '1992',
        '93': '1993',
        '94': '1994',
        '95': '1995',
        '96': '1996',
        '97': '1997',
        '98': '1998',
        '99': '1999',
        '00': '2000',
        '01': '2001',
        '02': '2002',
        '03': '2003',
        '04': '2004',
        '05': '2005',
        '06': '2006',
        '07': '2007',
        '08': '2008',
        '09': '2009',
        '10': '2010',
        '11': '2011',
        '12': '2012',
        '13': '2013',
        '14': '2014',
        '15': '2015',
        '16': '2016',
        '17': '2017',
        '18': '2018',
        '19': '2019',
        '20': '2020',
        '21': '2021'

    }

    SLASH = '/'

    AUTH = (
        'xavier,nhagumbe', 'Go$btgo1'
    )

    def get_uuids(self):
        return self.UUIDS

    def get_qualidade_carga(self):
        return self.QUALIDADE_CARGA

    def get_months(self):
        return self.MONTHS

    def get_years(self):
        return self.YEARS
