import json


class ReadJson:
    """读写json文件"""

    def __init__(self, json_file):

        self.json_file = json_file

    def read_json(self, url_path):
        """打开json文件"""

        with open(self.json_file, 'r+', encoding='utf-8') as f:

            content = f.read()
            # 将读取的内容加载成json格式
            re = json.loads(content)[url_path]

            interface = []
            # 输出URL_PATH下面的key：url，value：post/get，params转化成列表
            for k, v in re.items():
                res = []
                # k为url，list(v.keys())[0] 将dict_keys类型转化成list取[0]为post/get
                res.extend([k, list(v.keys())[0]])
                # 取post/get下标下parameters下key为name的值作为接口入参名称
                resp = v[list(v.keys())[0]].get('parameters')
                if resp:
                    for x in range(len(resp)):
                        res.append(resp[x].get('name'))
                interface.append(res)

            return interface
