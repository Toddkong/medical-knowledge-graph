import requests
import os

# 创建js文件夹
os.makedirs('js', exist_ok=True)

# 下载ECharts库
url = 'https://cdn.jsdelivr.net/npm/echarts@5.4.4/dist/echarts.min.js'
response = requests.get(url)
with open('js/echarts.min.js', 'wb') as f:
    f.write(response.content)

print('ECharts库已下载到js/echarts.min.js')