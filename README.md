server →　urls.py → 

#### command
新しいプロジェクトの作成  
django-admin startproject <prject_name>    (間のフォルダあり)  
django-admin startproject <prject_name> .  (間のフォルダなし)  
  
プロジェクトの実行  
python3 manage.py runserver   
  
新しいアプリの作成  
python3 manage.py startapp <app_name>  

### モデル
models.pyを作成

#### データベースを扱うためのコマンド
python3 manage.py makemigrations  migrations内にmigrateファイルを作成
python3 manage.py migrate

project内でmodel,viewを作るのではなくapp内で基本的に行う
projectでurlを降って各appのviewと繋ぐ

# TODO portが8000になっていないところ

# question
project内のviewはどうなる？ ->　いらない

### makemigration
models.pyとmigrate(データベース)の間の生成物  
細かい設定を作る

## CRUD
Create → CreateView
Read → ListView, DetailView
Update → UpdateView
Delete → DeleteView

### base.html
htmlのテンプレート的なやつ
基本的な構成を記載しておけば他のhtmlファイルに適応できる  

### other
Csrf_token:セキュリティのための記述
reverse:view内でurlに対応するタグを指定することでurlを指定できる
pk:プライマリーキー