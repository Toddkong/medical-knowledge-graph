# 生物医药图谱分析平台

这是一个基于ECharts的生物医药知识图谱可视化分析平台。

## 功能特性

- 知识图谱可视化展示
- 实体搜索和筛选
- 关系查看和分析
- 多语言支持（中文/英文）
- 数据导出功能

## 快速开始

### 安装和运行

1. 克隆项目到本地
2. 使用Python启动本地服务器：

```bash
# 使用提供的server.py脚本
python server.py

# 或者使用Python内置的HTTP服务器
python -m http.server 3000
```

3. 打开浏览器访问：http://localhost:3000/pages/graph_canvas.html

## 项目结构

```
.
├── js/                    # JavaScript库文件
│   └── echarts.min.js    # ECharts图表库
├── pages/                # 页面文件
│   ├── graph_canvas.html # 主图谱页面
│   └── test_graph.html   # 测试页面
├── case_data.json        # 案例数据
├── config.js             # 配置文件
├── server.py             # 服务器脚本
└── README.md             # 项目说明
```

## 技术栈

- HTML5
- CSS3
- JavaScript
- ECharts
- Tailwind CSS

## 数据说明

项目包含生物医药领域的实体和关系数据，包括：
- 疾病
- 药物
- 专家
- 论文
- 公司

## 许可证

本项目仅供学习和研究使用。
