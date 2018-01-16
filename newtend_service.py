# -*- coding: utf-8 -*-
'''
    Test cases execution combinations
    === Open EU ===
    bin/op_tests -s openProcedure -A robot_tests_arguments/openeu_testing.txt -v broker:Newtend -v role:tender_owner -v api_version:2.4
    bin/op_tests -s auction –A robot_tests_arguments/openeu_testing.txt -v broker:Newtend -v role:tender_owner –v api_version:2.4
    bin/op_tests -s qualification –A robot_tests_arguments/openeu_testing.txt -v broker:Newtend -v role:tender_owner –v api_version:2.4
    bin/op_tests –s contract_signing –A robot_tests_arguments/openeu_testing.txt -v broker:Newtend -v role:tender_owner –v api_version:2.4

'''
from datetime import datetime
from pytz import timezone
from iso8601 import parse_date
from op_robot_tests.tests_files.service_keywords import get_now
from calendar import monthrange


# def newtend_date_picker_index(isodate):
#     now = get_now()
#     date_str = '01' + str(now.month) + str(now.year)
#     first_day_of_month = datetime.strptime(date_str, "%d%m%Y")
#     mod = first_day_of_month.isoweekday() - 2
#     iso_dt = parse_date(isodate)
#     # last_day_of_month = monthrange(now.year, now.month)[1]
#     # LOGGER.log_message(Message("last_day_of_month: {}".format(last_day_of_month), "INFO"))
#     if now.day > iso_dt.day:
#         mod = monthrange(now.year, now.month)[1] + mod
#     return mod + iso_dt.day

def get_time_with_offset(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    time_zone = timezone('Europe/Kiev')
    localized_date = time_zone.localize(date_obj)
    return localized_date.strftime('%Y-%m-%d %H:%M:%S.%f%z')


def convert_budget(budget):
    budget_convertion = format(budget, '.2f')
    return budget_convertion


def substract(dividend, divisor):
    return int(dividend) - int(divisor)


def update_data_for_newtend(role_name, tender_data):
    if role_name == 'tender_owner':
        tender_data.data.procuringEntity['name'] = u'ten2312 gov comp'
        tender_data.data.procuringEntity.identifier['id'] = u'99002312'   # edrpou
        tender_data.data.procuringEntity.identifier['legalName'] = u'ten2312 gov comp'   # edrpou
        tender_data.data.procuringEntity.contactPoint['telephone'] = u'+380661602886'  # phone number
        tender_data.data.procuringEntity.address['streetAddress'] = u'Ruakaka, Northland, New Zealand'  # street
        tender_data.data.procuringEntity.address['region'] = u'Northland'  # region
        tender_data.data.procuringEntity.address['postalCode'] = u'34453'  # zip
        tender_data.data.procuringEntity.address['locality'] = u'Ruakaka'  # city
        tender_data.data.procuringEntity.contactPoint['name'] = u'ten2312 gov comp familija-11 '  # contact point
        tender_data.data.procuringEntity.contactPoint['url'] = u'http://www.site.com'  # contact point
    return tender_data


# Converting data from tendering palce into CDB common values
def convert_to_newtend_normal(string):
    return {
    # Our value: CBD value (CDB is expecting in such format)
    u'(Предложение принято)': u'active',    # for reporting procedure
    u'Active purchase': u'pending',
    u'ACTIVE PURCHASE': u'pending',
    u'Активна закупівля': u'pending',
    u'Активная закупка': u'pending',
    u'COMPLETED': u'active',
    u'ЗАВЕРШЕН': u'active',
    u'ЗАВЕРШЕНО': u'active',
    u"грн.": u"UAH",
    u"VAT incl.": True,
    u" VAT incl": True,
    u"c НДС": True,
    u"DC 021:2015 classifier": u"ДК021",
    u"Классификатор ДК 021:2015": u"ДК021",
    u"Класифікатор ДК 021:2015": u"ДК021",
    u"ДКПП Classifier": u"ДКПП",
    u"Классификатор ДКПП": u"ДКПП",
    u"Класифікатор ДКПП": u"ДКПП",
    u"pack": u"упаковка",
    u"set": u"набір",
    u"accounting unit": u"Одиниця",
    u"block": u"блок",
    u"bobbin": u"Бобіна",
    u"box": u"ящик",
    # u"cubic metre": u"
    # u"gigacalorie": u"
    # u"gram": u"
    # u"hectare": u"
    # u"hour": u"
    # u"job": u"
    # u"kilocalorie(international table)": u"
    u"kilogram": u"кілограми",
    u"килограммы": u"кілограми",
    # u"kilometre": u"
    # u"kilovar": u"
    # u"kilowatt": u"
    # u"kilowatt hour": u"
    # u"kit": u"
    # u"linear metre": u"
    # u"litre": u"
    u"lot [unit of procurement]": u"лот",
    u"lot[unit of procurement]": u"лот",
    # u"megawatt hour per hour": u"
    # u"metre": u"
    # u"month": u"
    # u"number of packs": u"
    # u"pair": u"
    # u"person": u"
    u"piece": u"штуки",
    # u"ream": u"
    # u"roll": u"
    # u"running or operating hour": u"
    # u"service": u"
    # u"unit": u"
    # u"square metre": u"
    # u"thousand cubic metre": u"
    # u"thousand piece": u"
    # u"tonne(metric ton)": u"
    # u"trip": u"
    # u"var": u"
    # u"vial": u"
    # u"working day": u"
    u"article 35, paragraph 2 of the Absence of competition (including technical reasons)relevant market, resulting in a purchase agreement can be concluded with only one provider, in the absence of the alternatives": u"noCompetition",
    u"ст. 35, п. 2 Отсутствие конкуренции (в том числе по техническим причинам) на соответствующем рынке, вследствие чего договор о закупке может быть заключен только с одним поставщиком, при отсутствии при этом альтернативы": u"noCompetition",
    u"cт. 35, п. 2 Відсутність конкуренції (у тому числі з технічних причин) на відповідному ринку, внаслідок чого договір про закупівлю може бути укладено лише з одним постачальником, за відсутності при цьому альтернативи": u"noCompetition",

    u"ст. 35, п. 1 Закупка произведений искусства или закупка, связанная с защитой прав интеллектуальной собственности, или заключения договора о закупке с победителем архитектурного или художественного конкурса": u"artContestIP",
    u"cт. 35, п. 1 Закупівля творів мистецтва або закупівля, пов’язана із захистом прав інтелектуальної власності, або укладення договору про закупівлю з переможцем архітектурного чи мистецького конкурсу": u"artContestIP",
    u"art. 35, item 1 Purchase of works of art or procurement related to the protection of intellectual property rights, or contract to purchase with the winner of an architectural or artistic competition": u"artContestIP",

    u"ст. 35, п. 4 Если заказчиком был дважды отменен тендер из-за отсутствия достаточного количества участников, при этом предмет закупки, его технические и качественные характеристики, а также требования к участникам не должны отличаться от требований, которые были определены заказчиком в тендерной документации": u"twiceUnsuccessful",
    u"cт. 35, п. 4 Якщо замовником було двічі відмінено тендер через відсутність достатньої кількості учасників, при цьому предмет закупівлі, його технічні та якісні характеристики, а також вимоги до учасника не повинні відрізнятися від вимог, що були визначені замовником у тендерній документації": u"twiceUnsuccessful",
    u"article 35, paragraph 4 If the customer was twice cancelled the tender due to the lack of a sufficient number of participants, the subject of the procurement, its technical and qualitative characteristics, requirements to the participant should not be different from requirements identified by the customer in tender documentation": u"twiceUnsuccessful",

    u"article 35, paragraph 6 the need for additional construction work,specified in the original draft, but which were in unexpected force the circumstances necessary to carry out the project with the combination of such terms: contract will be concluded with the previous contractor for these works, these works technically or economically related with the main (primary) contract; General the cost of additional works does not exceed 50 percent of the cost of main (primary) of contract": u"additionalConstruction",
    u"cт. 35, п. 6 необхідність проведення додаткових будівельних робіт, не зазначених у початковому проекті, але які стали через непередбачувані обставини необхідними для виконання проекту за сукупності таких умов: договір буде укладено з попереднім виконавцем цих робіт, такі роботи технічно чи економічно пов’язані з головним (первинним) договором; загальна вартість додаткових робіт не перевищує 50 відсотків вартості головного (первинного) договору": u"additionalConstruction",
    u"ст. 35, п. 6 необходимость проведения дополнительных строительных работ, не указанных в первоначальном проекте, но которые стали в силу непредвиденных обстоятельства необходимыми для выполнения проекта при совокупности таких условий: договор будет заключен с предыдущим исполнителем этих работ, такие работы технически или экономически связаны с главным (первичным) договором; общая стоимость дополнительных работ не превышает 50 процентов стоимости главного (первичного) договора": u"additionalConstruction",

    u"article 35, paragraph 5 of the need to make additional purchases from the same supplier for the purpose of unification, standardization or compatibility with the existing goods, technologies, works or services, if the replacement the previous supplier (contractor, provider) may result the incompatibility or the occurrence of technical problems associated with the operation and maintenance": u"additionalPurchase",
    u"cт. 35, п. 5 потреба здійснити додаткову закупівлю в того самого постачальника з метою уніфікації, стандартизації або забезпечення сумісності з наявними товарами, технологіями, роботами чи послугами, якщо заміна попереднього постачальника (виконавця робіт, надавача послуг) може призвести до несумісності або виникнення проблем технічного характеру, пов’язаних з експлуатацією та обслуговуванням": u"additionalPurchase",
    u"ст. 35, п. 5 потребность осуществить дополнительную закупку у того самого поставщика с целью унификации, стандартизации или обеспечения совместимости с имеющимися товарами, технологиями, работами или услугами, если замена предыдущего поставщика (исполнителя работ, предоставителя услуг) может привести к несовместимости или возникновения проблем технического характера, связанных с эксплуатацией и обслуживанием": u"additionalPurchase",

    u"article 35, paragraph 7 of the purchase of legal services related to the protection of the rights and the interests of Ukraine, including to protect national security and the defense, during the settlement of disputes consideration in the foreign jurisdiction the authorities of Affairs on the participation of a foreign entity and Ukraine based on the decision Of the Cabinet of Ministers of Ukraine or put into practice according to the law decisions The national security Council and defense of Ukraine": u"stateLegalServices",
    u"cт. 35, п. 7 закупівля юридичних послуг, пов’язаних із захистом прав та інтересів України, у тому числі з метою захисту національної безпеки і оборони, під час врегулювання спорів, розгляду в закордонних юрисдикційних органах справ за участю іноземного суб’єкта та України, на підставі рішення Кабінету Міністрів України або введених в дію відповідно до закону рішень Ради національної безпеки і оборони України": u"stateLegalServices",
    u"ст. 35, п. 7 закупка юридических услуг, связанных с защитой прав и интересов Украины, в том числе с целью защиты национальной безопасности и обороны, во время урегулирования споров, рассмотрения в заграничных юрисдикционных органах дел с участием иностранного субъекта и Украины на основании решения Кабинета Министров Украины или введенных в действие согласно закону решений Совета национальной безопасности и обороны Украины": u"stateLegalServices",

    }.get(string, string)
