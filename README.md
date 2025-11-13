```sh
$ uv sync
$ uv run django-admin startproject config web

$ uv run python web/manage.py runserver
http://127.0.0.1:8000/

$ uv run python web/manage.py makemigrations
$ uv run python web/manage.py migrate

$ touch .envrc
$ cp .envrc.example .envrc
$ direnv allow

# app 追加
$ mkdir web/stock
$ uv run django-admin startapp stock web/stock

$ uv run web/manage.py createsuperuser --noinput

# ruff によるフォーマッターの実行
$ uv run ruff format
# ruff によるリンターの実行
$ uv run ruff check --fix

# mypy による型ヒントチェック
$ uv run mypy .

# pytest によるテスト
$ uv run pytest

# djlint によるフォーマット
$ uv run djlint web/templates/*/*.html --extension=html.j2 --reformat
$ uv run djlint web/templates/*/*.html --extension=html.j2 --lint

# ライブラリ追加
$ uv add "Django==5.2.8"
# dev用のライブラリ追加
$ uv add "djlint==1.36.4" --dev
```

