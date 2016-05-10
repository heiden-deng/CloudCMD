# -*- coding: utf-8 -*-
from base import AbstractProductAPI


class VideoAPI(AbstractProductAPI):
    BASE_PATH = "/api/v1/video/"

    def _get_path(self, suffix):
        return "%s%s" % (self.BASE_PATH, suffix)

    def create_vod(self, name, uploaded_video_file, origin_image_file=None, introduction=None, labels=None):
        # 创建视频
        params = {
            'name': name,
            'uploaded_video_file': uploaded_video_file,
            'origin_image_file': origin_image_file,
            'introduction': introduction,
            'labels': labels,
        }
        path = self._get_path('vods/create')
        return self.post(path, params)

    def vods(self):
        # 获取点播视频列表
        path = self._get_path("vods")
        return self.get(path)

    def detail(self, id):
        # 获取视频详细信息
        path = self._get_path("vods/%s" % id)
        return self.get(path)

    def modify_vod(self, id, name, labels, introduction, origin_image_file):
        # 修改VOD视频
        params = {
            'name': name,
            'labels': labels,
            'introduction': introduction,
            'origin_image_file': origin_image_file
        }
        path = self._get_path('vods/%s/modify' % id)
        return self.post(path, params)

    def delete_vod(self, id):
        # 删除VOD视频
        path = self._get_path('vods/%s/delete' % id)
        return self.post(path)
