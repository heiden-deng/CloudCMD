# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class NetworkAPI(AbstractProductAPI):
    BASE_PATH = "/api/v1/products/networks/"

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def create(self, az):
        '''
        创建网络

        az: 可用数据中心

        '''
        path = self._get_path("create")
        return self.post(path, {'az': az})

    def list(self):
        # 网络列表
        return self.get(self.BASE_PATH)

    def detail(self, id):
        '''
        私有网络信息

        id: 私有网络id

        '''
        path = self._get_path(id)
        return self.get(path)

    def delete(self, id):
        '''
        删除私有网络

        id: 私有网络id

        '''
        path = self._get_path("%s/delete" % str(id))
        return self.post(path)

    def set_alias(self, id, alias):
        '''
        为网络设置别名

        id: 私有网络id,
        alias: 别名

        '''
        path = self._get_path("%s/alias" % str(id))
        return self.post(path, {'alias': alias})

    def set_group(self, id, group):
        '''
        为网络设置分组

        id: 私有网络id,
        group: 组名

        '''
        path = self._get_path("%s/group" % str(id))
        return self.post(path, {'group': group})

    def groups(self):
        # 私有网络分组列表
        path = self._get_path('groups')
        return self.get(path)
