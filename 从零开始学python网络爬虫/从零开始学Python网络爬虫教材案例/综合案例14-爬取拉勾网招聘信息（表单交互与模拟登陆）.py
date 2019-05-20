import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
lagou = mydb['lagou']

headers = {
    'Cookie':'user_trace_token=20190414191544-84a8d01e-ff64-4b3a-9e1a-01c776d0ad0d; _ga=GA1.2.2095772546.1555240550; LGUID=20190414191545-a5ef3791-5ea6-11e9-845d-525400f775ce; _gat=1; JSESSIONID=ABAAABAAADEAAFI05F77196736FD85A50E95DB5D753B47C; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558244470,1558244474; LGSID=20190519134112-b5cb8d6e-79f8-11e9-a2dd-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Ddz-aCG-KTH4MZYZnMdbHshRdfKRCNZNMYtBbgt-vlr3%26wd%3D%26eqid%3Dd1b5f78e00067430000000045ce0ec6b; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gid=GA1.2.1099624729.1558244474; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216acea1852d20-00c7b5055990c7-70193c4f-1327104-16acea1852e7f5%22%2C%22%24device_id%22%3A%2216acea1852d20-00c7b5055990c7-70193c4f-1327104-16acea1852e7f5%22%7D; sajssdk_2015_cross_new_user=1; _putrc=A48A77205F69ED17; login=true; unick=%E9%AD%8F%E7%AB%8B%E5%A5%8E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=f737b64f7cd42db2394a0256c6ba387b445556235c3da236; X_HTTP_TOKEN=a16fa8e59b775fc80694428551379fc76b89620f4a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558244963; LGRID=20190519134920-d921cea1-79f9-11e9-a2dd-525400f775ce; SEARCH_ID=3b24e15241b74f7d8e9a28e44930910d',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
    'Connection':'keep-alive'
}

def get_page(url,params):
    html = requests.post(url, data=params, headers=headers)
    json_data = json.loads(html.text)
    total_Count = json_data['content']['positionResult']['totalCount']
    page_number = int(total_Count/15) if int(total_Count/15)<30 else 30
    get_info(url,page_number)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first': 'true',
            'pn': str(pn),
            'kd': 'Python'
        }
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {
                    'businessZones':result['businessZones'],
                    'city':result['city'],
                    'companyFullName':result['companyFullName'],
                    'companyLabelList':result['companyLabelList'],
                    'companySize':result['companySize'],
                    'district':result['district'],
                    'education':result['education'],
                    'explain':result['explain'],
                    'financeStage':result['financeStage'],
                    'firstType':result['firstType'],
                    'formatCreateTime':result['formatCreateTime'],
                    'gradeDescription':result['gradeDescription'],
                    'imState':result['imState'],
                    'industryField':result['industryField'],
                    'jobNature':result['jobNature'],
                    'positionAdvantage':result['positionAdvantage'],
                    'salary':result['salary'],
                    'secondType':result['secondType'],
                    'workYear':result['workYear']
                }
                lagou.insert_one(infos)
                time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first': 'true',
        'pn': '1',
        'kd': 'Python'
    }
    get_page(url,params)