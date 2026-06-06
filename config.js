const prototypeConfig = {
    project: {
        title: "图谱分析项目",
        version: "v1.0",
        updatedAt: "2024-01-01",
        type: "web" // 项目类型为web
    },
    modules: [
        {
            id: "graph_analysis",
            title: "图谱分析",
            icon: "fa-solid fa-project-diagram",
            type: "web",
            pages: [
                {
                    id: "graph_canvas",
                    title: "分析画布",
                    path: "./pages/graph_canvas.html",
                    status: "finished",
                    type: "web",
                    description: {
                        summary: "图谱分析的核心画布，支持本体展示、关系显示和交互操作。",
                        flows: ["1. 选择要分析的实体类型", "2. 在画布上添加/拖拽实体", "3. 建立实体间的关系", "4. 分析实体间的关联"],
                        features: ["支持疾病、药品、专家、论文、公司等本体", "显示本体关系", "支持10+实体", "支持新建、拖拽、删除、添加、拓展等交互"]
                    }
                }
            ]
        }
    ]
};