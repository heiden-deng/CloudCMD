# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class CloudServerAPI(AbstractProductAPI):
    BASE_PATH = '/api/v1/products/cloud_servers/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self):
        # 云主机列表
        return self.get(self.BASE_PATH)

    def detail(self, id):
        '''
        云主机详细信息

        id: 云主机id

        '''
        path = self._get_path(str(id))
        return self.get(path)

    def backups(self, id):
        '''
        云主机备份列表

        id: 云主机id

        '''
        path = self._get_path("%s/backups" % str(id))
        return self.get(path)

    def jobs(self, id):
        '''
        云主机认为列表

        id: 云主机id

        '''
        path = self._get_path("%s/jobs" % str(id))
        return self.get(path)

    def provision(self, az, isp, image, cpu, memory, disk, bandwidth):
        '''
        创建云主机

        az: 可用数据中心,
        isp: 数据中心支持的运营商,
        image: 操作系统镜像,
        cpu: cpu核心数,
        memory: memory大小,
        disk: disk大小,
        bandwidth: 带宽大小

        '''
        path = self._get_path('provision')
        configurations = {
            'az': az,
            'isp': isp,
            'image': image,
            'cpu': cpu,
            'memory': memory,
            'disk': disk,
            'bandwidth': bandwidth,
        }
        return self.post(path, configurations)

    def start(self, id):
        '''
        启动云主机

        id: 云主机id

        '''
        return self._cloud_server_simple_operations('start', id)

    def restart(self, id):
        '''
        重启云主机

        id： 云主机id

        '''
        return self._cloud_server_simple_operations('restart', id)

    def stop(self, id):
        '''
        关闭云主机

        id: 云主机id

        '''
        return self._cloud_server_simple_operations('stop', id)

    def suspend(self, id):
        '''
        挂起云主机

        id: 云主机id

        '''
        return self._cloud_server_simple_operations('suspend', id)

    def resume(self, id):
        '''
        回复云主机

        id: 云主机id

        '''
        return self._cloud_server_simple_operations('resume', id)

    def backup(self, id, name):
        '''
        备份云主机

        id: 云主机id
        name: 备份名

        '''
        path = self._get_path("%s/backup" % str(id))
        return self.post(path, {'name': name})

    def restore_backup(self, id, name):
        '''
        恢复云主机备份

        id: 云主机id
        name: 备份名

        '''
        path = self._get_path("%s/backups/%s/restore" % (str(id), name))
        return self.post(path)

    def delete_backup(self, id, name):
        '''
        删除云主机备份

        id: 云主机id
        name: 备份名

        '''
        path = self._get_path("%s/backups/%s/delete" % (str(id), name))
        return self.post(path)

    def set_tag(self, id, tag):
        '''
        为云主机设置标签

        id: 云主机id
        tag: 标签名

        '''
        path = self._get_path("%s/tag" % str(id))
        return self.post(path, {'tag': tag})

    def set_alias(self, id, alias):
        '''
        为云主机设置别名

        id: 云主机id
        alias: 别名

        '''
        path = self._get_path("%s/alias" % str(id))
        return self.post(path, {'alias': alias})

    def set_group(self, id, group):
        '''
        为云主机设置分组

        id: 云主机id
        group: 组名

        '''
        path = self._get_path("%s/group" % str(id))
        return self.post(path, {'group': group})

    def change_image(self, id, image_name):
        '''
        变更操作系统

        id: 云主机id
        image: 操作系统镜像

        '''
        path = self._get_path("%s/change_image" % str(id))
        return self.post(path, {'image': image_name})

    def attach_disk(self, id, volume_name):
        '''
        挂在云硬盘

        id: 云主机id
        volume_name: 云硬盘名

        '''
        path = self._get_path("%s/attach/%s" % (str(id), volume_name))
        return self.post(path)

    def detach_disk(self, id, volume_name):
        '''
        卸载云硬盘

        id: 云主机id
        volume_name: 云硬盘名

        '''
        path = self._get_path("%s/detach/%s" % (str(id), volume_name))
        return self.post(path)

    def _cloud_server_simple_operations(self, operation, id):
        path = self._get_path("%s/%s" % (str(id), operation))
        return self.post(path)

    def get_az(self):
        # 获得可用数据中心
        azs = self.get('/api/v1/availability_zones/names')
        return azs

    def get_support_isps(self, az):
        # 获得数据中心支持运营商
        azs = self.get('/api/v1/availability_zones/')
        for az in azs:
            if az['name'] == az:
                return az['support_isps']
        return ''

    def get_os_images(self, az):
        # 获得操作系统镜像列表
        images = self.get('/api/v1/products/images/')
        ret = []
        for image in images:
            ret.append(image['name'])
        azs = self.get('/api/v1/availability_zones/')
        for az in azs:
            if az['name'] == az:
                for private_image in az['private_images']:
                    if private_image['name'] not in ret:
                        ret.append(private_image['name'])
                for public_image in az['public_images']:
                    if public_image['name'] not in ret:
                        ret.append(public_image['name'])
        return ret
