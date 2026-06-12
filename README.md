# Fast API Demo

前后端分离的起步项目：**Vue3** + **FastAPI** + **MySQL**。当前只包含健康检查与数据库连通性测试，方便你从 0 到 1 逐步加功能。

## 目录结构

```
fast-api-demo/
├── backend/          # FastAPI 后端
│   ├── app/
│   │   ├── main.py       # 入口与 API 路由
│   │   ├── config.py     # 配置（读取 .env）
│   │   └── database.py   # SQLAlchemy 数据库连接
│   ├── requirements.txt
│   └── .env.example
└── frontend/         # Vue3 前端（Vite）
    └── src/
        ├── App.vue
        └── api/
```

## MySQL 账号（来自本地 ruoyi 项目配置）

在 `ruoyi-vue-pro` 的 `application-local.yaml` 中，本地 MySQL 配置为：

| 项 | 值 |
|---|---|
| 主机 | `127.0.0.1` |
| 端口 | `3306` |
| 用户名 | `root` |
| 密码 | `root` |
| 若依库名 | `ruoyi-vue-pro` |

同目录下 `RuoYi-Vue`、`RuoYi-Flowable-Plus` 等项目的 MySQL 账号/password 也是 **root / root**。

本项目使用独立库名 **`fast_api_demo`**，请先创建：

```sql
CREATE DATABASE fast_api_demo DEFAULT CHARACTER SET utf8mb4;
```

## 快速启动

### 1. 后端

```bash
cd backend
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
copy .env.example .env   # 已存在可跳过
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**停止后端：** 在运行 uvicorn 的终端按 `Ctrl + C`（无单独的 `uvicorn stop` 命令）。

**已找不到原始终端时（强制结束）：** 若 8000 端口仍被占用（启动报 `WinError 10013`），可先查 PID 再结束进程：

```powershell
# 1. 查看占用 8000 端口的进程（最后一列为 PID）
netstat -ano | findstr ":8000"

# 2. 结束进程（将 41064 替换为上一步查到的 PID）
Stop-Process -Id 41064 -Force

# 或使用 taskkill
taskkill /PID 41064 /F

# 3. 确认端口已释放（无输出即表示已关闭）
netstat -ano | findstr ":8000"
```

API 文档：http://127.0.0.1:8000/docs

### 2. 前端

```bash
cd frontend
npm install
npm run dev
```

浏览器访问：http://localhost:5173

前端通过 Vite 代理将 `/api` 转发到 `http://127.0.0.1:8000`。

## 当前 API

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/health` | 服务是否正常运行 |
| GET | `/api/db/ping` | MySQL 是否可连接 |

## 下一步可以做什么

- 在 `backend/app/models/` 添加数据模型
- 在 `backend/app/api/` 添加业务路由
- 在前端 `src/views/`、`src/router/` 扩展页面与路由
- 接入登录、JWT、CRUD 等
