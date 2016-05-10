# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class LoadBalancerAPI(AbstractProductAPI):
    BASE_PATH = '/api/v1/products/load_balancers/'

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def list(self):
        # 负载均衡列表
        return self.post(self.BASE_PATH)

    def create_load_balance(self, az, isp, bandwidth):
        '''
        创建负载均衡

        az: 可用数据中心
        isp: 数据中心支持的运营商
        bandwidthnet: 带宽

        '''
        configurations = {
            'az': az,
            'isp': isp,
            'bandwidth': bandwidth,
        }
        path = self._get_path("provision")
        return self.post(path, configurations)

    def add_backend_cloud_server(self, lbid, csid, weight, ip):
        '''
        添加后端云主机

        lbid: 负载均衡id
        csid: 云主机id
        weight: 权重
        ip: ip地址

        '''
        params = {
            'cloud_server_id': csid,
            'weight': weight,
            'ip_address': ip,
        }
        path = self._get_path(str(lbid) + '/backends/add')
        return self.post(path, params)

    def add_backend_database(self, lbid, did, weight, ip):
        '''
        添加后端数据库

        lbid: 负载均衡id
        did: 数据库id
        weight: 权重
        ip: ip地址

        '''
        params = {
            'database_id': did,
            'weight': weight,
            'ip_address': ip,
        }
        path = self._get_path(str(lbid) + '/backends/add')
        return self.post(path, params)

    def add_backend_cache(self, lbid, cid, weight, ip):
        '''
        添加后端缓存

        lbid: 负载均衡id
        cid: 缓存id
        weight: 权重
        ip: ip地址

        '''
        params = {
            'database_id': cid,
            'weight': weight,
            'ip_address': ip,
        }
        path = self._get_path(str(lbid) + '/backends/add')
        return self.post(path, params)

    def update_backend(self, lbid, bid, weight, ip):
        '''
        更新后端

        lbid: 负载均衡id
        bid: 后端id
        weight: 权重
        ip: ip地址

        '''
        path = self._get_path(str(lbid) + '/backends/' + str(bid) + '/update')
        params = {
            'weight': weight,
            'ip_address': ip,
        }
        return self.post(path, params)

    def delete_backend(self, lbid, bid):
        '''
        删除后端

        lbid: 负载均衡id
        bid: 后端id

        '''
        path = self._get_path(str(lbid) + '/backends/' + str(bid) + '/delete')
        return self.post(path)

    def add_app(self, lbid, frontend, backend, protocol, strategy, check_interval, rise_times,
                        fall_times):
        '''
        添加应用

        lbid: 负载均衡id
        frontend: 前端端口
        backend: 后端端口
        protocol: 协议
        strategy: 负载均衡策略
        check_interval: 健康检查间隔
        rise_times: 下线监测阀值
        fall_times: 在线监测阀值

        '''
        params = {
            'frontend': frontend,
            'backend': backend,
            'protocol': protocol,
            'strategy': strategy,
            'check_interval': check_interval,
            'rise_times': rise_times,
            'fall_times': fall_times
        }
        path = self._get_path(str(lbid) + '/applications/add')
        return self.post(path, params)

    def detail(self, lbid):
        '''
        负载均衡详细信息

        lbid: 负载均衡id

        '''
        path = self._get_path(str(lbid))
        return self.post(path)

    def update_app(self, lbid, appid, frontend, backend, protocol, strategy,
                           check_interval, rise_times, fall_times):
        '''
        更新应用

        lbid: 负载均衡id
        appid: 应用id
        frontend: 前端端口
        backend: 后端端口
        protocol: 协议
        strategy: 负载均衡策略
        check_interval: 健康检查间隔
        rise_times: 下线监测阀值
        fall_times: 在线监测阀值

        '''
        params = {
            'frontend': frontend,
            'backend': backend,
            'protocol': protocol,
            'strategy': strategy,
            'check_interval': check_interval,
            'rise_times': rise_times,
            'fall_times': fall_times
        }
        path = self._get_path(str(lbid) + '/applications/' + str(appid) + '/update')
        return self.post(path, params)

    def delete_app(self, lbid, appid):
        '''
        删除应用

        lbid: 负载均衡id
        appid: 应用id

        '''
        path = self._get_path(str(lbid) + '/applications/' + str(appid) + '/delete')
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
