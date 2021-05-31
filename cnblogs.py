import requests

import json
from bs4 import BeautifulSoup


class cnblogs:
    def __init__(self):
        self.url = 'https://zzk.cnblogs.com/s/blogpost?Keywords={}&pageindex={}'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'cookie': '_ga=GA1.2.799958.1591953635; Hm_lvt_d8d668bc92ee885787caab7ba4aa77ec=1613145654; Hm_lvt_39b794a97f47c65b6b2e4e1741dcba38=1617545742; __gads=ID=e14819fb61b75779:T=1619404476:R:S=ALNI_MZM8lR_InLUFUt_AnbnA_wYbRABKQ; UM_distinctid=1796b4668e4ba4-0c209b6e458af4-2363163-144000-1796b4668e5885; .Cnblogs.AspNetCore.Cookies=CfDJ8L-rpLgFVEJMgssCVvNUAjsuqLGsC7FgfvEE_vs78kM5Jxzyxn95lqK8asL9MEr5DGWUTdgIG14UoC4SJ4LXvx9cC3fTg7ANBrxYlPbyPGvJXD0wxLrHdoMTBPl-T-WSCEqU4tVoOJF-_A0lxKvBeoh7Qo109v85E-Fq31rE0FZYUFoLZKpjR14XCTdW90tUb4M5VbQxamjMVAktE4HP0FfUGLv4GNUtRKafBWagj9M1yrtIHYk856PmHOS0dOiphUPCjiSzFOtcNiU_auZM1Iunh3l2mkyqIT8bpm0YDfZdrN4h78RNXdzb-AeFlgtzPfgFjjCiyAdOG962YCCk8k9mkkj2iAxY9yqdTL3sva_-St3BKFITQx7keBizQYO0HCU4P_a2VaG-hfROjAOntEUCAG3AB3f9hLqrHqLmVG3hOPOKDLkxpotOUrbwXdP9PDirSMokMRM7mHkSMbn0xpyVevoTDZCTwLsIEDX_W8pOd-w92ro35lG9uKpHnzKavz_1rJRLj1fRPH3_0rlBuO3r40SC1Zs1tU70iz6-bt_50KzfYx7RY0ll300EPhSN1Q; _gid=GA1.2.148971386.1622250455; __utma=59123430.799958.1591953635.1608965644.1622299214.2; __utmc=59123430; __utmz=59123430.1622299214.2.2.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=59123430.6.10.1622299214'
        }

    def get_requests(self, url):
        return requests.get(url).content.decode()

    def parse_data(self, data):
        print(data)
        blog_list = BeautifulSoup(data).find(attrs={'class': 'searchURL'})
        print(blog_list)
        pass

    def write_to_file(self, data):
        pass

    def run(self, Keywords='python', pageindex=1):
        for i in range(0, pageindex):
            url = self.url.format(Keywords, i + 1)
            content = self.get_requests(url)
            data = self.parse_data(content)
            self.write_to_file(data)


if __name__ == '__main__':
    cnblogs().run()
