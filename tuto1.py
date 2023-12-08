#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
gros_carres = (n ** 2 for n in itertools.count() if n ** 2 >= 1000)
premier_gros_carres = next(gros_carres)
print(premier_gros_carres)  # 1024



