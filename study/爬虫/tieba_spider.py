import requests


class TieBaSpider():

    def __init__(self, keyword):
        self.keyword=keyword
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw=" + keyword + "&fr=search&pn={}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    def get_url_list(self):
        url_list = []
        for i in range(1000):
            url_list.append(self.url.format(i*50))
        return  url_list

    def parese_url(self,url):#发送请求，获取响应
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    def save_html(self,html,page_num):
        #利用文件存储保存
        file_path="{}-第{}页.html".format(self.keyword,page_num)
        with open(file_path,"w",encoding='utf-8') as f:
            f.write(html)


    def run(self):
        #构造url列表
        url_list = self.get_url_list()
        #遍历 发送请求
        for url in url_list:
            content = self.parese_url(url)
            #获取页码 即url 在列表中的下标位置+1
            page_num=url_list.index(url)+1
            self.save_html(content,page_num)


if __name__ == '__main__':
    #构造实例对象
    spider = TieBaSpider('福州')
    spider.run()



