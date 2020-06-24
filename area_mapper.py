#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : area_mapper.py
# @Author: Cedar
# @Date  : 2020/6/23
# @Desc  : https://blog.csdn.net/qq_33256688/article/details/79445792

import cpca
from cpca import drawer


location_str = ["徐汇区虹漕路461号58号楼5楼", "11月15日早上9点到11月18日下班前王大猫。在观山湖区", "浙江省杭州市下城区青云街40号3楼"]
df = cpca.transform(location_str, pos_sensitive=True, cut=False)
drawer.draw_locations(df, "df.html")
print(df)
