# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class CloudVolumeAPI(AbstractProductAPI):
    BASE_PATH = '/api/v1/products/cloud_volumes/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def provision(self, az, size):
        '''
        创建云硬盘

        az: 可用数据中心
        size: 云硬盘容量

        '''
        path = self._get_path("provision")
        params = {
            'az': az,
            'size': size,
        }
        return self.post(path, params)

    def list(self):
        # 云硬盘列表
        return self.get(self.BASE_PATH)

    def detail(self, id):
        '''
        云硬盘详细信息

        id: 云硬盘id

        '''
        path = self._get_path(str(id))
        return self.get(path)

    def snapshots(self, cloud_volume_id):
        '''
        云硬盘快照列表

        id: 云硬盘id

        '''
        path = self._get_path("%s/snapshots" % str(id))
        return self.get(path)

    def jobs(self, id):
        '''
        云硬盘任务列表

        id: 云硬盘id

        '''
        path = self._get_path("%s/jobs" % str(id))
        return self.get(path)

    def set_tag(self, id, tag):
        '''
        为云硬盘设置标签

        id: 云硬盘id
        tag: 标签名

        '''
        path = self._get_path("%s/tag" % str(id))
        return self.post(path, {'tag': tag})

    def set_alias(self, id, alias):
        '''
        为云硬盘设置别名

        id: 云硬盘id
        alias: 别名

        '''
        path = self._get_path("%s/alias" % str(id))
        return self.post(path, {'alias': alias})

    def set_group(self, id, group):
        '''
        为云硬盘设置分组

        id: 云硬盘id
        group: 组名

        '''
        path = self._get_path("%s/group" % str(id))
        return self.post(path, {'group': group})

    def create_snapshot(self, id):
        '''
        创建快照

        id: 云硬盘id

        '''
        path = self._get_path("%s/snapshot" % str(id))
        return self.post(path)

    def rollback_snapshot(self, id, snapshot):
        '''
        回滚快照

        id: 云硬盘id
        snapshot: 快照名

        '''
        path = self._get_path("%s/snapshots/%s/rollback" % (str(id), snapshot))
        return self.post(path)

    def delete_snapshot(self, id, snapshot):
        '''
        删除快照

        id: 云硬盘id
        snapshot: 快照名

        '''
        path = self._get_path("%s/snapshots/%s/delete" % (str(id), snapshot))
        return self.post(path)

    def get_available_zone(self):
        # 获得可用数据中心
        azs = self.get('/api/v1/availability_zones/names')
        return azs
