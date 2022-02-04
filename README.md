## package
```
pip install webdriver-manager beautifulsoup4 selenium requests
```

<!-- fake-useragent -->

## use
```
python main.py
```
### 指定 city
```
python main.py --city 臺北市
```

### city list
```
{'10017': '基隆市', '63': '臺北市', '65': '新北市', '68': '桃園市', '10018': '新竹市', '10004': '新竹縣', '10005': '苗栗縣', '66': '臺中市', '10007': '彰化縣', '10008': '南投縣', '10009': '雲林縣', '10020': '嘉義市', '10010': '嘉義縣', '67': '臺南市', '64': '高雄市', '10013': '屏東縣', '10002': '宜蘭縣', '10015': '花蓮縣', '10014': '臺東縣', '10016': '澎湖縣', '09020': '金門縣', '09007': '連江縣'}
```

## response
```
{"today": {"img": "https://www.cwb.gov.tw//V8/assets/img/cwb-logoBlue.svg", "tem": "13~14"}, "week": [{"date": "02/05\u661f\u671f\u516d", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/11.svg", "tem": "13\u2002-\u200215"}, {"date": "02/06\u661f\u671f\u65e5", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/11.svg", "tem": "13\u2002-\u200216"}, {"date": "02/07\u661f\u671f\u4e00", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/07.svg", "tem": "14\u2002-\u200221"}, {"date": "02/08\u661f\u671f\u4e8c", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/11.svg", "tem": "15\u2002-\u200216"}, {"date": "02/09\u661f\u671f\u4e09", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/10.svg", "tem": "15\u2002-\u200217"}, {"date": "02/10\u661f\u671f\u56db", "img": "https://www.cwb.gov.tw//V8/assets/img/weather_icons/weathers/svg_icon/day/07.svg", "tem": "15\u2002-\u200217"}], "city": "\u81fa\u5317\u5e02", "city_code": "63"}
```