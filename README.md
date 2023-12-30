# CareerLog

## ディレクトリ構成
```
career-log/
│
├── myproject/            # Djangoプロジェクトの設定ディレクトリ
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Django設定ファイル
│   ├── urls.py           # プロジェクトレベルのURL設定
│   └── wsgi.py
│
├── myapp/                # Djangoアプリケーションディレクトリ
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # データモデル
│   ├── tests.py
│   └── views.py
│
├── manage.py             # Djangoのコマンドラインツール
└── README.md
```

## 管理画面
http://127.0.0.1:8000/admin/

## DB設計

**初段リリースの方針**

スコープとしては、個人利用のプロトタイプとして開発したサービスのため、DBは軽量でシンプルなSQLiteを採用した

**SQliteの注意点**

- 並列書き込み
  - SQLiteは、同時に複数の書き込みを行うことができないため、書き込みの競合が発生する可能性がある
- スケーラビリティ
  - 大規模なデータや高負荷の環境では、SQLiteのパフォーマンスが他のデータベース管理システム（DBMS）に比べて劣る可能性がある
- 高度な機能
  - PostgreSQLやMySQLなどの他のDBMSには、パーティショニング、レプリケーション、フルテキスト検索などの高度な機能がありますが、SQLiteではこれらはサポートされていない
  
## 開発

### 依存関係の更新
大きな変更や新しい依存関係がある場合は下記のコマンドを実行して依存関係の更新を行なってから、updateして下さい。
```
$ pip install -r requirements.txt

$ zappa update dev
```

### マイグレーション
モデルの変更があった場合は、マイグレーションファイルを作成してからマイグレーションを実行して下さい。
```
$ python manage.py makemigrations

$ python manage.py migrate
```

### 仮想環境の起動停止
仮想環境をアクティブにする
```
$ source venv/bin/activate
(venv) (career-log)
```
仮想環境を非アクティブにする
```
$ deactivate
```

### front

- CSS、JavaScript、画像などを更新した際は、S3へアップロードすること
- HTMLファイルは一般的に静的ファイルとは見なされず、Djangoのテンプレートシステムを通じて動的にレンダリングされるので、Lambdaにアップロードするで問題ない
