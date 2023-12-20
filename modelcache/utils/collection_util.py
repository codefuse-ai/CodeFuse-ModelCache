# -*- coding: utf-8 -*-
"""
   Alipay.com Inc.
   Copyright (c) 2004-2023 All Rights Reserved.
   ------------------------------------------------------
   File Name : collection_util.py
   Author : fuhui.phe
   Create Time : 2023/12/20 21:36
   Description : description what the main function of this file
   Change Activity: 
        version0 : 2023/12/20 21:36 by fuhui.phe  init
"""


def get_collection_iat_name(model, iat_type):
    return 'multicache' + '_' + model + '_' + iat_type
