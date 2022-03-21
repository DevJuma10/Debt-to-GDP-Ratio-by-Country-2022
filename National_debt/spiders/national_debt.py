import scrapy


class NationalDebtSpider(scrapy.Spider):
    name = 'national_debt'
    allowed_domains = ['www.worldpopulationreview.com/']
    start_urls = ['https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath('//table[@class="jsx-1878461898 table table-striped tp-table-body"]/tbody/tr')

        # national_debt_row = response.xpath('//table[@class="jsx-1878461898 table table-striped tp-table-body"]/tbody/tr/td[2]/text()').getall()
        # countries = response.xpath('//table[@class="jsx-1878461898 table table-striped tp-table-body"]/tbody/tr/td/a/text()').getall()

        for row in rows:
            name = row.xpath('./td/a/text()').get()
            debt = row.xpath('td[2]/text()').get()

            yield{
                "country_name" : name,
                "national_Debt_to_GDP_Ratio" : debt
            }