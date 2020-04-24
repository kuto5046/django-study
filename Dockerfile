FROM ubuntu:18.04
 
# update
RUN apt-get -y update && apt-get install -y \
sudo \
wget \
vim \
git \
python3.7 \
python3-pip

# set path
ENV PATH /usr/bin:$PATH

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
RUN mkdir /work
ADD requirements.txt /work

# isntall module
RUN pip3 install --upgrade pip && \
    pip3 install -r /work/requirements.txt

# set shell
# RUN touch ~/.xonshrc
