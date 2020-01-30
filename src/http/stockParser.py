import requests
from lxml import html


def getUrl(stockid):
    Titles = ['NCI', 'EPS', 'MBG', 'NPG', 'NP', 'NOR']
    url = []
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='
               + stockid + '&typecode=MANANETR&cate=xjll0')       # 经营活动产生的现金流量净额
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinancialGuideLineHistory.php?stockid='
               + stockid + '&typecode=financialratios61')         # 每股收益
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinancialGuideLineHistory.php?stockid='
               + stockid + '&typecode=financialratios43')         # 主营业务增长率
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinancialGuideLineHistory.php?stockid='
               + stockid + '&typecode=financialratios44')         # 净利润增长率
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='
               + stockid + '&type=NETPROFIT&cate=liru0')          # 净利润
    url.append('http://money.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='
               + stockid + '&type=BIZTOTINCO&cate=liru0')         # 营业总收入
    return url, Titles


def parse_stock(stockid):
    url, Titles = getUrl(stockid)
    data = {}
    timeReg = '//div[@id="con02-2"]//table//tbody//tr//td[1]/text()'
    itemReg = '//div[@id="con02-2"]//table//tbody//tr//td[2]/text()'
    page = requests.Session().get(url[0])
    htmlPage = html.fromstring(page.text)
    timeRegVal = htmlPage.xpath(timeReg)
    data["time"] = timeRegVal
    for i in range(0, len(url)):
        page = requests.Session().get(url[i])
        htmlPage = html.fromstring(page.text)
        titleNameVal = htmlPage.xpath(itemReg)
        data[Titles[i]] = titleNameVal
    return data
