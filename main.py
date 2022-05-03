from config import *
from readjson import ReadJson
from request import RequestInterface


class RequestsTest:
    """接口测试"""

    @staticmethod
    def requests_test():

        # 获取url，get/post，入参名称
        json_data = ReadJson(JSON_FILE).read_json(URL_PATH)
        # 遍历获取单个url，method，入参名称
        for i in json_data:

            params = {}
            url = i[0]
            method = i[1]
            # 判断列表长度大于2则有入参
            if len(i) > 2:
                if method == 'get':
                    for j in i[2:]:
                        dic = {j: ''}
                        params.update(dic)
                elif method == 'post':
                    for j in i[2:]:
                        dic = {j: ''}
                        param = {}
                        param.update(dic)
                        params = [param]
                else:
                    params = None
            interface_request = RequestInterface(URL_HOST + url, method, params)
            interface_request.request_interface()


if __name__ == '__main__':
    RequestsTest().requests_test()


