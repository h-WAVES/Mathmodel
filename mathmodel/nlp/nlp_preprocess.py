# -*- coding: utf-8 -*- 

# @Time : 2021-03-19 16:47 
# @Author : hht 
# @File : nlp_preprocess.py
# @Desc:

import os
import sys
from mathmodel.nlp.langconv import *


def zh_hans_hant(ori_str, build_dict='zh2hans'):
    """

    :param build_dict: zh-hans 繁体转简体，zh2Hant简体转繁体
    :param ori_str:
    :return:
    """
    if build_dict == 'zh2hans':
        return Converter('zh-hans').convert(ori_str)
    elif build_dict == 'zh2hant':
        return Converter('zh-hant').convert(ori_str)
    else:
        return ori_str




# unicode
def full2half(ori_str):
    """

    :param ori_str:
    :return:

    Examples
    --------
    full_data = '１２３４５６７８９０'
    half=full2half(full_data)
    -->1234567890
    """
    new_str = ''
    for uchar in ori_str:
        code = ord(uchar)
        if code == 12288:
            code = 32
        elif (code >= 65281 and code <= 65374):
            code -= 65248
        new_str += chr(code)
    return new_str


def half2full(ori_str):
    """

    :param ori_str:
    :return:

    Examples
    --------
    half_data = '1234567890'
    full=half2full(half_data)
    -->１２３４５６７８９０
    """
    new_str = ''
    for uchar in ori_str:
        code = ord(uchar)
        if code == 32:
            code = 12288
        elif code >= 32 and code <= 126:
            code += 65248
        new_str += chr(code)
    return new_str


def to_lower(ori_str):
    """
    大小写转化
    :param ori_str:
    :return:
    """
    return ori_str.lower()


def to_upper(ori_str):
    """
    大小写转化
    :param ori_str:
    :return:
    """
    return ori_str.upper()


def replace_punc_by_space(ori_str):
    """
    用空格替换非数字、中文、字母、下划线以外的标点字符
    :param ori_str:
    :return:

    Examples
    --------
    input_text = '1～4北京_-!%^6-9love'
    output_text=replace_punc_by_space(input_text)
    --> 1 4北京_ 6 9love
    """
    return re.sub('\W+', ' ', ori_str)


def replace_punc_by_blank(ori_str):
    """
    用''替换非数字、中文、字母、下划线以外的标点字符
    :param ori_str:
    :return:

    Examples
    --------
    input_text = '1～4北京_-!%^6-9love'
    output_text=replace_punc_by_space(input_text)
    --> 14北京_69love
    """
    return re.sub('\W+', '', ori_str)


def is_digit(ori_str):
    """
    是否全是数字
    :param ori_str:
    :return:

    Examples
    --------
    input_text = '123abc'
    output_text=is_digit(input_text)
    --> False
    """
    for uchar in ori_str:
        code = ord(uchar)
        if not (ord('0') <= code <= ord('9')):
            return False
    return True


def is_alpha(ori_str):
    """
    是否全是英文
    :param ori_str:
    :return:

    Examples
    --------
    input_text = 'aBc'
    output_text=is_alpha(input_text)
    --> True
    """
    for uchar in ori_str:
        code = ord(uchar)
        if not ((ord('a') <= code <= ord('z')) or
                (ord('A') <= code <= ord('Z'))):
            return False
    return True


def is_digit_or_alpha(ori_str):
    """
    是否全是英文或者数字
    :param ori_str:
    :return:
    """
    for uchar in ori_str:
        code = ord(uchar)
        if not (ord('0') <= code <= ord('9') or
                (ord('a') <= code <= ord('z')) or
                (ord('A') <= code <= ord('Z'))):
            return False
    return True


def has_alphanum(ori_str):
    """
    是否包含英文、数字、空格
    :param ori_str:
    :return:
    """
    for uchar in ori_str:
        code = ord(uchar)
        if uchar == ' ' or ord('a') <= code <= ord('z') or \
                ord('A') <= code <= ord('Z') or ord('0') <= code <= ord('9'):
            return True
    return False


def text_cleaning(ori_str, lower=True, full_half='half', replace_punc='blank', zh_conv='zh2hans'):
    """

    :param ori_str:
    :param lower:
    :param full_half:
    :param replace_punc:
    :param zh_conv:
    :return:
    """

    if ori_str == '':
        return ori_str
    elif ori_str == ' ':
        return ori_str.strip()
    else:
        input_str = ori_str
    if lower:
        lu_str = to_lower(input_str)
    else:
        lu_str = to_lower(input_str)
    if full_half == 'half':
        fullhalf_str = full2half(lu_str)
    elif full_half == 'full':
        fullhalf_str = half2full(lu_str)
    else:
        fullhalf_str = lu_str
    if replace_punc == 'space':
        punc_str = replace_punc_by_space(fullhalf_str)
    elif replace_punc == 'blank' and replace_punc != '':
        punc_str = replace_punc_by_blank(fullhalf_str)
    else:
        punc_str = fullhalf_str

    return zh_hans_hant(punc_str,zh_conv)




