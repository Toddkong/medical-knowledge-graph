# 云企汇 AI 原型工程化指南 (Workflow Guide v2.0)

这份文档旨在指导如何将**AI 原型生成工作流**应用到新项目中，实现从需求到高保真原型（Mobile/Web Admin）的自动化产出。

## 1. 核心架构理念

本项目采用 **"自适应主框架 + 双模引擎 + 自动化协议"** 的架构：

*   **自适应主框架 (`prototype_viewer.html`)**: 
    *   智能识别页面类型，自动切换 **手机壳模式** (Mobile) 或 **全屏浏览器模式** (Web Admin)。
    *   支持左侧导航、右侧说明面板、Toast 消息等通用能力。
*   **双模提示词引擎**:
    *   **`PROMPT_MOBILE.md`**: 专用于生成 App、小程序等移动端页面。
    *   **`PROMPT_WEB_APP.md`**: 专用于生成 WEB端应用页面。
    *   **`PROMPT_WEB_ADMIN.md`**: 专用于生成 B 端管理后台、数据大屏等桌面端页面。
*   **自动化执行协议 (Auto-Execution)**:
    *   **意图校准 (Intent Alignment)**: AI 会优先阅读功能描述而非文件名，防止将“身份(等级)”误判为“实名认证”。
    *   **防重复机制 (Pre-flight Check)**: AI 会自动检查 `config.js`，跳过已存在的页面，避免重复劳动。
    *   **TDD 流程**: 遵循 "自动拆解 -> 批量生成 -> 自动注册" 的闭环。

---

## 2. 标准目录结构 (Scaffold)

在一个标准的原型项目中，你应该保持以下文件结构：

```text
ProjectRoot/
├── prototype_viewer.html    # [核心] 预览器 (请勿修改，直接复制)
├── config.js                # [核心] 数据中心 (AI 自动维护)
├── PROJECT_RULES.md         # [规范] 全局工程规范 (约束 AI 行为)
├── PROMPT_MOBILE.md         # [提示词] 移动端专用
├── PROMPT_WEB_ADMIN.md      # [提示词] 后台端专用
├── pages/                   # [产物] 存放所有生成的 HTML 页面
│   ├── home.html
│   ├── admin_dashboard.html
│   └── ...
└── 需求文档.md               # [输入] 你的原始需求
```

---

## 3. 如何初始化新项目 (Migration Guide)

当你需要在一个新的文件夹（新项目）中开始工作时，请执行以下 **"脚手架初始化"** 步骤：

### 第一步：复制核心资产
将以下文件从本仓库复制到新项目根目录：
1.  `prototype_viewer.html`
2.  `config.js`
3.  `PROJECT_RULES.md`
4.  `PROMPT_MOBILE.md`
5.  `PROMPT_WEB_ADMIN.md`
6.  创建空的 `pages/` 文件夹

### 第二步：重置配置 (`config.js`)
打开新项目中的 `config.js`，将其重置为初始状态：

```javascript
const prototypeConfig = {
    project: {
        title: "新项目名称", // 修改这里
        version: "v1.0",
        updatedAt: "202X-XX-XX"
    },
    modules: [] // 清空模块列表，等待 AI 填充
};
```

### 第三步：准备就绪
现在，你已经拥有了一个干净的、支持多端适配的 AI 原型开发环境。

---

## 4. 日常工作流程 (Daily Workflow)

### 步骤 0：需求预处理 (Standardization) - *推荐*
为了让 AI 更精准地执行自动化任务，建议先使用 **需求拆解工具** 对原始需求进行清洗。
1.  **投喂工具**: 将 `需求拆解提示词.md` 的内容发送给 AI。
2.  **输入需求**: 发送你的原始需求文档（脑图/PDF/会议纪要）。
3.  **获取产物**: AI 会输出两部分内容：
    *   **Part 1 业务需求规格书**: 用于与客户确认业务逻辑。
    *   **Part 2 工程化执行映射表**: 包含精确的 `Mobile/Web_APP/Admin` 分类和文件名。
4.  **分发任务**: 复制 **Part 2** 中的表格内容，作为指令发送给开发 AI。

### 场景 A：开发移动端页面 (App/小程序)

1.  **上下文投喂**: 将 `PROMPT_MOBILE.md` 和 `PROJECT_RULES.md` 发送给 AI。
2.  **输入需求**: 粘贴需求文档或直接描述（例如：“做一个个人中心，包含头像、订单入口、设置”）。
3.  **自动化执行**: 
    *   AI 会自动规划页面（如 `profile.html`, `settings.html`）。
    *   AI 会连续生成代码文件。
    *   AI 会自动更新 `config.js` 注册页面。
4.  **验收**: 刷新 `prototype_viewer.html`，在左侧菜单点击查看，效果默认为**手机框视图**。

### 场景 B：开发管理后台 (Web Admin)

1.  **上下文投喂**: 将 `PROMPT_WEB_ADMIN.md` 和 `PROJECT_RULES.md` 发送给 AI。
2.  **输入需求**: 描述后台需求（例如：“做一个用户管理列表，要有搜索、分页和操作按钮”）。
3.  **自动化执行**: AI 将生成全屏布局的页面，并在配置中标记 `type: 'admin'`。
4.  **验收**: 刷新预览器，点击菜单，主框架会自动切换为**全屏 Web 视图**。

### 场景 A：开发WEB端应用页面 (PC/pad)

1.  **上下文投喂**: 将 `PROMPT_WEB_APP.md` 和 `PROJECT_RULES.md` 发送给 AI。
2.  **输入需求**: 粘贴需求文档或直接描述（例如：“做一个个人中心，包含头像、订单入口、设置”）。
3.  **自动化执行**: 
    *   AI 会自动规划页面（如 `profile.html`, `settings.html`）。
    *   AI 会连续生成代码文件。
    *   AI 会自动更新 `config.js` 注册页面。
4.  **验收**: 刷新 `prototype_viewer.html`，在左侧菜单点击查看，效果默认为**全屏WEB视图**。

---

## 5. 关键规范备忘 (Cheatsheet)

虽然 AI 会自动处理大部分规范，但人工 Review 时请关注：

1.  **图片**: 必须使用 `zhanweifu.com` 且带 `&font_size=30` 参数。
2.  **滚动条**: 必须在 CSS 中隐藏滚动条 (`::-webkit-scrollbar { display: none; }`)，保持界面整洁。
3.  **交互**: 禁止 `alert()`，必须用 `showToast()`。
4.  **Web 模式**: 确保生成的 Web 页面在 `config.js` 中被标记了 `type: "admin"`（模块级或页面级均可），否则会被默认装进手机壳里。

---

## 6. 常见问题 (FAQ)

**Q: 为什么我的后台页面被装进了手机壳里？**
A: 检查 `config.js`。该页面或其所属的模块必须包含 `type: "admin"` 属性。
```javascript
// 正确示例
{
    id: "admin_module",
    type: "admin", // <--- 加上这个
    pages: [...]
}
```

**Q: AI 生成了一半停住了？**
A: 我们设置了熔断机制（每 3 个页面暂停一次）。只需回复 "继续"，AI 就会继续生成剩下的页面。

**Q: 我可以手动修改 pages 下的 HTML 吗？**
A: 当然可以。`prototype_viewer.html` 只是一个读取器，它实时读取 `pages/` 下的文件。你手动修改 HTML 后，刷新浏览器即可看到变化。
