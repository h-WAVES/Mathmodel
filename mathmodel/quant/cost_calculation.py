# -*- coding: utf-8 -*- 

from decimal import Decimal, ROUND_HALF_UP


"""
eg:
get_cost(b_dict={7.26:4000},s_dict={7.30:4000})


"""
def is_five(cost:int)->int:
    """
    判断是否超过5元
    :param cost:
    :return:
    """
    if cost < 5.0:
        return 5.0
    else:
        return cost
def b_cost(amount,commission_rate=0.00017, transfer_fees=0.00002, zhengquan=0.0000487,
             jiaoyisuo=0.00002):
    """
    买入费用
    :param amount:
    :param commission_rate:
    :param transfer_fees:
    :param zhengquan:
    :param jiaoyisuo:
    :return:

    1.印花税为成交金额的1‰，仅卖出时收取；
    2.过户费为成交金额的0.02‰，买卖双向收取；
    3.交易所费用为成交金额的0.0687‰，买卖双向收取；0.0687‰  分为交易所和证监会
    4.佣金收取比例不高于成交金额的3‰，买卖双向收取，最低5元。
    commission_rate = 0.00017  # 佣金率  证券公司手续
    transfer_fees = 0.00002  # 过户费 证券公司监管费  中国证监会
    zhengquan = 0.0000487  # 证券交易经手费  交易所
    jiaoyisuo = 0.00002  # 交易过户费 中国证券等级结算有限公司
    tax_rate = 0.001

    """
    commission = round(amount * (commission_rate + zhengquan + jiaoyisuo + transfer_fees), 2)
    commission = is_five(commission)
    return commission
def s_cost(s_amount,commission_rate=0.00017, transfer_fees=0.00002, zhengquan=0.0000487,
             jiaoyisuo=0.00002,tax_rate= 0.001):
    """
    卖出费用
    :param s_amount:
    :param commission_rate:
    :param transfer_fees:
    :param zhengquan:
    :param jiaoyisuo:
    :param tax_rate:
    :return:
    """
    s_commission = round(s_amount * (commission_rate + zhengquan + jiaoyisuo + transfer_fees) + s_amount * tax_rate, 2)
    s_commission = is_five(s_commission)
    return s_commission
def get_cost(b_dict={0:0},s_dict=None):
    """
    交易收益
    :param b_dict:
    :param s_dict:
    :return:
    """
    b_comm=0
    b_amount=0
    b_cnt=0

    for b_price,b_stcok_cnt in b_dict.items():
        b_cnt+=1
        amount = b_price * b_stcok_cnt
        b_amount+=amount
        commission = b_cost(amount)
        b_comm += commission
        print("buy:{}*{}={},  {}_cost={}".format(b_price,b_stcok_cnt,amount,b_cnt,commission))
    #print("buy stock total cost={}".format(b_comm))
    if s_dict != None:
        s_amount=0
        s_comm=0
        s_cnt=0
        for s_price, s_stock_cnt in s_dict.items():
            s_cnt+=1
            samount = s_price * s_stock_cnt
            s_commission=s_cost(samount)
            s_amount += samount
            s_comm += s_commission
            print("sale:{}*{}={},  {}_cost={}".format(s_price, s_stock_cnt, s_amount, s_cnt, s_commission))
        total_cost=s_comm + b_comm
        #print("卖出手续费（sale stock cost）={},总计手续费（total）={}".format(s_comm,total_cost))

        #print("total profit={}".format(s_amount-b_amount-total_cost))

    outstr="卖出手续费（sale stock cost）={},总计手续费（total）={} \n{}".format\
        (s_comm,total_cost,s_amount-b_amount-total_cost)

    return outstr