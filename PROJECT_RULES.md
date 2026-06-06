# Project Engineering Rules (工程化规范)

## 1. 项目目标
本项目旨在构建一个**自动化工作流**，用于快速将需求文档转换为可视化的 HTML 原型。
核心架构：`左侧功能导航` + `中间 HTML 预览` + `右侧功能说明`。

## 2. 文件结构规范
- **Prototype Viewer**: `prototype_viewer.html` (静态核心)。
  - **重要规则**: 此文件是**通用脚手架**，在新项目中**严禁生成或修改**。它直接从标准库中复制使用。
  - AI 的任务是生成与之配套的 `config.js` 和 `pages/` 下的页面。
- **Config**: `config.js` (数据驱动)。AI 必须生成此文件，且结构必须严格符合 `prototype_viewer.html` 的接口要求（见下文 Schema）。
- **Pages**: 所有的原型页面应作为独立的 HTML 文件存储在 `pages/` 目录下。

## 2.1 核心协议 (Core Protocol)

`prototype_viewer.html` 依赖 `config.js` 驱动。为了支持**多端适配 (Mobile/Web)**，AI 生成的配置必须遵循以下结构：

```javascript
const prototypeConfig = {
    project: { 
        title: "项目名称", 
        version: "v1.0", 
        updatedAt: "YYYY-MM-DD",
        // 可选: 全局视图类型 ('mobile' | 'admin' | 'web')。如果不填，默认为 'mobile'。
        // type: "mobile" 
    },
    modules: [
        {
            id: "module_id",
            title: "模块名称",
            icon: "fa-solid 图标类名", 
            // 可选: 模块级视图类型。如果该模块全是后台页面，请设置为 'admin'。
            // type: "admin", 
            pages: [
                {
                    id: "page_unique_id",
                    title: "页面标题",
                    path: "./pages/xxx.html", 
                    status: "finished", // fixed: finished
                    // 可选: 页面级视图类型。优先级最高。
                    // type: "admin", 
                    description: {
                        summary: "功能概述文本...",
                        flows: ["用户操作步骤1", "步骤2..."],
                        features: ["核心功能点1", "功能点2..."]
                    }
                }
            ]
        }
    ]
};
```

**视图类型 (Type) 说明**:
- `mobile` (默认): 页面将显示在模拟手机容器中 (宽 ~400px)。
- `admin` / `web` / `pc`: 页面将显示在全屏/桌面容器中 (宽 100%)。

## 3. 代码生成通用规范 (General Coding Rules)

无论是移动端还是 Web 端，生成的代码必须遵循：

### 3.1 技术栈
- **CSS**: 仅使用 TailwindCSS CDN (`https://cdn.tailwindcss.com`)。
- **JS**: 仅使用原生 JavaScript (ES6+)，无 Vue/React/jQuery。
- **Icons**: FontAwesome CDN。
- **Charts**: ECharts CDN。

### 3.2 交互与体验
- **禁止 Alert**: 严禁使用系统原生 `alert()`，必须使用自定义 Toast 组件。
- **响应式布局**: 必须使用 Tailwind 的响应式类，禁止 JS 硬编码尺寸。
- **图片占位**: 必须使用 `zhanweifu.com`，且**必须包含 `font_size` 参数**。
  - 格式: `https://www.zhanweifu.com/300x200?text=中文&font_size=30`。

### 3.3 演示流程
- 所有的链接跳转若无实际页面，统一使用 `href="javascript:void(0)"` 并配合 `showToast('进入xxx页面')` 提示。
- 表单提交统一模拟成功状态，不进行实际网络请求。

## 4. 自动化交付与注册 (Automation)
- **Auto-Save**: AI 必须明确指出建议的文件名（如 `pages/xxx.html`）。
- **Auto-Register**: AI 必须生成 `config.js` 的配置片段，并尽可能自动插入到 `config.js` 中。
- **Check**: 注册完成后，提示用户刷新 `prototype_viewer.html` 查看。
