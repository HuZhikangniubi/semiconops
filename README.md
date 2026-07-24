# SemiconOps

**SemiconOps: Semiconductor Yield Risk Analysis and Evidence-Grounded Investigation Copilot**

半导体制造良率风险分析与证据化调查平台。

## 项目定位

基于公开真实制造数据与权威资料，提供良率失败风险预测、概率校准、SHAP 模型行为解释、统计相似案例、独立证据化知识检索、受控调查工作流、人工反馈与审计记录。

本项目是工程师决策支持原型，不是自动根因判定系统，不控制真实产线。

## 快速开始

```bash
cp .env.example .env
uv sync --all-extras --group dev
docker compose up -d db
uv run uvicorn semiconops.api.app:app --reload
```

访问：

- API 文档：http://127.0.0.1:8000/docs
- 健康检查：http://127.0.0.1:8000/health

## 下载 SECOM

```bash
uv run python scripts/download_secom.py
```

脚本会从 UCI 官方地址下载、计算 SHA256、解压到 `data/raw/secom/`，并写入 `data/manifests/secom.json`。原始数据不进入 Git。

## 真实性边界

- 匿名特征不得解释为具体工艺参数；
- 预测、SHAP 和统计相似不得写成根因或因果证明；
- SECOM、WM-811K、PHME 2022 不做样本级融合；
- 材料知识库不能自动解释 SECOM 匿名特征。
