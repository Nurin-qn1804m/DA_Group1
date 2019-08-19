import requests
import scrapy
import unittest

url = 'http://172.18.58.238/multi/'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t",r.status_code)

if r.status_code == 200:
    print("OK.")
if r.status_code == 404:
    print("Not Found.")

print ("*********")

h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t",x,".",h.headers[x])
print("**********")

headers = {
    'User-Agent':'Mobile'
}

url2 ='http://172.18.58.238/headers.php'
rh=requests.get(url2,headers=headers)
print(rh.text)
print("**********")

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/multi/']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

class test(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(r.status_code, 200)

    def test_header(self):
        self.assertNotEqual(h.headers, x)

    def test_user_agent(self):
        self.assertNotEqual("User-Agent", "Mobile")


if __name__=='__main__':
    unittest.main()








