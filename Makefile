.PHONY: help install run test lint format typecheck security up down logs download-secom tree
help:
	@echo "install         安装全部依赖"
	@echo "run             启动 FastAPI"
	@echo "test            运行测试"
	@echo "lint            Ruff 检查"
	@echo "format          Ruff 格式化"
	@echo "typecheck       mypy 类型检查"
	@echo "security        安全检查"
	@echo "up/down/logs    Docker Compose"
	@echo "download-secom  下载并登记 SECOM"
install:
	uv sync --all-extras --group dev
run:
	uv run uvicorn semiconops.api.app:app --reload
test:
	uv run pytest
lint:
	uv run ruff check .
format:
	uv run ruff format .
typecheck:
	uv run mypy
security:
	uv run bandit -r src/semiconops
	uv run pip-audit
up:
	docker compose up -d --build
down:
	docker compose down
logs:
	docker compose logs -f api
download-secom:
	uv run python scripts/download_secom.py
tree:
	tree -a -L 4 -I '.git|.venv|__pycache__'
