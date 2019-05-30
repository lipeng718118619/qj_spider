# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver

COOKIE_JAR = 'cookiejar'

options = webdriver.ChromeOptions()
# options.headless = True  # 设置启动无界面化
# options.add_argument('window-size=1920,1080')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')


class QjSpider(RedisSpider):
    """

    """
    name = 'qj_spider'

    allowed_domains = ['m.qj.com.cn', 'www.qj.com.cn']

    def __init__(self, name=None, **kwargs):
        self.options = options
        self.driver = webdriver.Chrome(options=self.options)  # 启动时添加定制的选项
        super(QjSpider, self).__init__(name, **kwargs)

    def start_requests(self):
        start_urls = ['https://www.qj.com.cn/so/']

        for url in start_urls:
            yield Request(url=url, meta={COOKIE_JAR: 1}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # 提取二级界面links
        for next_url_selector in response.css(".brandbutbox .on"):
            next_url = next_url_selector.attrib['href']

            yield Request(url=next_url, meta={COOKIE_JAR: 1}, callback=self.next_parse, dont_filter=False)

        main_url = response.css('.propage').css('a')[-1].attrib['href']

        yield Request(url=main_url, meta={COOKIE_JAR: 1}, callback=self.parse, dont_filter=True)

    def next_parse(self, response):
        # 二级解析函数
        brand_txt = response.css('.brandtxt')
        pro_logo = response.css('.roundimgx').css('img')[0].attrib['src']
        # 标题
        title = brand_txt.css('h3::text')[0].extract()
        corp_info = brand_txt.css('li::text')
        # 经营模式
        corp_business_model = corp_info[0].extract()
        # 品牌源地
        brand_source = corp_info[1].extract()
        # 门店总数
        total_number_of_store = corp_info[2].extract()
        # 合同期限
        contract_period = corp_info[3].extract()
        operating_products = None
        if len(corp_info) >= 5:
            # 经营产品
            operating_products = corp_info[4].extract()
        # 适合人群
        suitable_for_the_crowd = None
        if len(corp_info) >= 6:
            suitable_for_the_crowd = corp_info[5].extract()

        brand_box_dd_p = response.css('.brandbox .brandconz dd')[0].css('p')
        # 投资金额
        investment_amount = brand_box_dd_p[0].css('b::text').extract_first().replace("\n", "").strip()

        # 一级行业
        primary_industry = brand_box_dd_p[1].css('a::text').extract()[0].replace("\n", "").strip()

        # 二级行业
        secondary_industry = brand_box_dd_p[1].css('a::text').extract()[1].replace("\n", "").strip()

        group_box = response.css('div .groupbox')
        # 公司地址
        corp_address = group_box.css('p::text')[0].extract()

        # 公司名称
        corp_name = group_box.css("h6::text").extract_first()

        if not corp_name:
            corp_name = group_box.css("h6").css('a::text').extract_first()

        # 公司成立时间
        corp_create_time = group_box.css('p::text')[1].extract()

        join_details = response.css('.joindetails')

        # 项目介绍
        product_introduce = "".join(
            response.xpath('//*[@id="joindetails"]/div/p | //*[@id="joindetails"]/div/center').extract())

        # 项目优势
        project_benefits = join_details.css('#youshi').extract_first()

        # 支持
        project_support = join_details.css('#support').extract_first()

        # 流程
        project_flow = join_details.css('#flow').extract_first()

        # 条件
        project_condition = join_details.css('#condition').extract_first()

        # 加盟费用
        project_feiyong = join_details.css('#feiyong').extract_first()

        if not (project_benefits or project_support or project_flow or project_condition or project_feiyong):
            product_introduce = "".join(join_details.css(".joincon").extract())

        yield {"title": title,
               "corp_business_model": corp_business_model,
               "brand_source": brand_source,
               "investment_amount": investment_amount,
               "total_number_of_store": total_number_of_store,
               "contract_period": contract_period,
               "operating_products": operating_products,
               "suitable_for_the_crowd": suitable_for_the_crowd,
               "primary_industry": primary_industry,
               'secondary_industry': secondary_industry,
               "corp_address": corp_address,
               "corp_name": corp_name,
               'corp_create_time': corp_create_time,
               "product_introduce": product_introduce,
               'project_benefits': project_benefits,
               'project_support': project_support,
               'project_flow': project_flow,
               'project_condition': project_condition,
               'pro_logo': pro_logo,
               'project_feiyong': project_feiyong
               }

    def close(self, spider):
        self.driver.close()
        self.driver.quit()
