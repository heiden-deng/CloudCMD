# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class CacheAPI(AbstractProductAPI):
    def list(self):
        # 缓存列表
        return self.get('/api/v1/products/caches/')