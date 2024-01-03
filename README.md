# [CareerLog](http://career-log.s3-website-ap-northeast-1.amazonaws.com/)

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

インストールされた全てのパッケージが含まれる requirements.txt ファイルを作成
```
$ source venv/bin/activate  # Activate your virtual environment
$ pip freeze > requirements.txt  # Generate requirements.txt
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

### 開発過程

まずは、S3を使って簡単な静的なビューを表示した
- http://career-log.s3-website-ap-northeast-1.amazonaws.com/
- S3：https://s3.console.aws.amazon.com/s3/buckets/career-log?region=ap-northeast-1&bucketType=general&tab=properties

LambdaからEFSのファイルを編集しようとした際に権限がないと指摘されたので、権限を変更するために下記の設定を行った
- EFSにアクセスするためのEC2インスタンスをEFSと同じVPN何に作成
- VPN内のEC2インスタンスがSSHで外部と通信できるようにGateWayを設置
- EC２が外部と通信するために、パブリックIPアドレスを作成して設定
- VPCでGateWayを紐づけるため、Route tablesから紐付け
- EC2用のセキュリティグループを作成
上記の設定を行ってから、EC2へSSH接続をした
```
# EFSにアクセスするだけのEC2インスタンスあので、OSは相性の良いAWSにした
# 57.181.10.163は作成したバプリックIP
$ ssh -i ./dambo3987fnos.pem ec2-user@57.181.10.163

# efsの操作に必要なパッケージのインストール
$ sudo yum install -y amazon-efs-utils
$ rpm -q amazon-efs-utils
amazon-efs-utils-1.35.0-1.amzn2023.noarch

# botocoreをインストールするために、pip3をインストール
$ sudo yum install python3-pip

# botocoreのインストール
$ sudo pip3 install botocore

# AWSの資格情報を設定
$ aws configure
AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: ap-norheast-1
Default output format [None]: json

# マウントの設定
# EFSマウントターゲットのIPアドレス: 10.0.1.250
# EFS: fs-01da562a3e9cce07d
$ sudo mount -t efs -o tls,mounttargetip=10.0.1.250 fs-01da562a3e9cce07d /mnt/efs

# マウントされたか確認
$ df -hT | grep efs
127.0.0.1:/    nfs4      8.0E     0  8.0E   0% /mnt/efs

# ディレクトリ作成
$ sudo mkdir -p /mnt/efs

# 権限変更
$ sudo chmod 777 /mnt
$ sudo chmod 777 /mnt/efs
```

EFSにアクセスしなくなったら、課金対策としEC2を使用するために作成したリソースを削除する
- EC2関連
  - インスタンスの停止
  - パブリックIPの削除
- VPC関連
  - Gatewayt(career-log-ec2-gateway)削除
  - ルートテーブルの設定削除
