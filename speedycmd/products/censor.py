from base import AbstractProductAPI


class CensorAPI(AbstractProductAPI):
    BASE_PATH = 'api/v1/censor'

    def censor(self, url):
        return self.get(self.BASE_PATH, {'url': url})
