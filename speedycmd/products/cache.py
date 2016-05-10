# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class CacheAPI(AbstractProductAPI):
    def list(self):
        # 缓存列表
        return self.get('/api/v1/products/caches/')

    def create_cache(self, az, isp, image, memory, disk, bandwidth):
        '''
        创建缓存

        az: 可用数据中心,
        memory: 内存大小,
        disk: 硬盘大小,
        bandwidth: 带宽大小,
        isp: 数据中心支持的网络运营商,
        image: 数据库镜像

        '''
        configurations = {
            'az': az,
            'memory': memory,
            'disk': disk,
            'bandwidth': bandwidth,
            'isp': isp,
            'image': image,
        }
        return self.post("/api/v1/products/caches/provision", configurations)

    def get_az(self):
        # 获得可用数据中心
        azs = self.get('/api/v1/availability_zones/names')
        return azs

    def get_support_isps(self, az_name):
        # 获得数据中心支持运营商
        azs = self.get('/api/v1/availability_zones/')
        for az in azs:
            if az['name'] == az_name:
                return az['support_isps']
        return ''

    def get_images(self):
        # 获得缓存镜像列表
        images = self.get('/api/v1/products/database_images_names/')
        imgs = []
        for image in images:
            if image['type'] != 'MySQL' and image['type'] != 'MongoDB':
                imgs.append(image['name'])
        return imgs
