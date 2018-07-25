# coding:utf-8
import re
import random
import requests
from bs4 import BeautifulSoup

# 处理页面标签工具类
class Tool():
    # 将超链接广告剔除
    removeADLink = re.compile('<div class="link_layer.*?</div>')
    # 去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeADLink, "", x)
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        # strip()将前后多余内容删除
        return x.strip()

    pass


# 反反爬虫之随机浏览器响应头
def getRandomRequest(self,url):

    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        ]
    randdom_header = random.choice(my_headers)
    return randdom_header
    pass


#反反爬虫之代理服务器
class AgentIp():

    def __init__(self):
        self.update_agent()
        pass

    #更新代理ip
    def update_agent(self):
        agent_ips = []
        #代理获取地址
        self.agent_url = 'http://www.xicidaili.com/nn/'
        #网站响应头
        head = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        html = requests.get(self.agent_url,headers=head).text
        soup = BeautifulSoup(html)
        #解析网页
        for i in soup.select('#ip_list tr')[1:]:
            prox = {}
            tds = i.select('td')
            prox[tds[5].text] = tds[1].text +":"+ tds[2].text

            agent_ips.append(prox)
            pass
        #更新
        self.ips = agent_ips
        pass

    #得到代理地址
    def get_ips(self):
        return self.ips
        pass

    #获取随机的ip
    def get_random_ip(self):
        return random.choice(self.ips)
        pass

   #验证代理是否可用
    def verfiy_ip(self,prox):
        try:
            re = requests.get('http://www.baidu.com', proxies=prox)
            print(re.status_code)
            pass
        except:
            print('cuowu')
            pass
        else:
            pass
        pass
    pass


if __name__ == '__main__':

    print('未完待续')
    pass