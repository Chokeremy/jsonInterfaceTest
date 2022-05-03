import requests


class RequestInterface:
    """请求接口"""

    def __init__(self, url, method, params=None):

        self.url = url
        self.method = method
        self.params = params

    def request_interface(self):

        if self.method == 'get':

            response = requests.request(method=self.method, url=self.url, params=self.params)
            print('接口地址：{}\t\t请求方式：{}\t返回状态码：{}'.format(self.url, self.method, response.status_code))

        elif self.method == 'post':

            response = requests.request(method=self.method, url=self.url, params=self.params)
            print('接口地址：{}\t\t请求方式：{}\t返回状态码：{}'.format(self.url, self.method, response.status_code))

        else:
            print('接口地址：{}\t\t请求方式：{}\t暂不支持测试！'.format(self.url, self.method))

RequestInterface('http://synyi-cdss-op-manager-1817-test.sy/api/ops/PlatformConfig/reload-config', 'get', '').request_interface()
# RequestInterface('http://synyi-cdss-op-manager-1817-test.sy/api/ops/Config/reload-memory-cache', 'post', '').request_interface()
RequestInterface('http://synyi-cdss-op-manager-1817-test.sy/api/ops/PlatformConfig/delete', 'delete', '').request_interface()

