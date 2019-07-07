# Chalice-Linebot

透過 [AWS Chalice](https://github.com/aws/chalice) 建立你 Line bot

你需要
  * 建立 Line Bot: [https://developers.line.biz/console/](https://developers.line.biz/console/)
  * AWS Console: [https://aws.amazon.com/tw/console/](https://aws.amazon.com/tw/console/)

## Install

```
pip install chalice
```

### 設定權限

Chalice 可以透過 Deploy 的指令，自動幫你設定 `API Gateway` 以及佈署 `lambda`
所以需要提供 `IAM` 權限給 Chalice

[AWS IAM](https://console.aws.amazon.com/iam/home#/users)
1. Create User
2. AWS access type 選 `Programmatic acces`
3. Policy 選 `IAMFullAccess`, `AWSLambdaFullAccess`, `AmazonAPIGatewayAdministrator`
4. Download credentials

### 設定 .aws config

下載完後 credentials 需要設定你的 .aws 環境

```
$ mkdir ~/.aws
$ vi ~/.aws/config
```

```
[default]
aws_access_key_id=<aws_access_key_id>
aws_secret_access_key=<aws_secret_access_key>
region=ap-northeast-1
```

備註：
* aws_access_key_id: 填 credentials 裡面 `Access key ID`
* aws_secret_access_key: 填 credentials 裡面 `Secret access key`
* region 會決定把你的機器到哪個區域，[參考連結](https://docs.aws.amazon.com/zh_tw/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

## 下載範例程式

```
git clone https://github.com/jiunjiun/chalice-linebot.git
cd chalice-linebot
```

### 設定 Line Secret, Token

```
$ cp .chalice/config.json.sample .chalice/config.json
```

### 修改 .chalice/config.json

* LINEBOT_CHANNEL_SECRET: 填入你 [Line Bot](https://developers.line.biz/console/) 的 `Channel secret`
* LINEBOT_CHANNEL_ACCESS_TOKEN: 填入你 [Line Bot](https://developers.line.biz/console/) 的 `Channel access token`

![Alt text](/docs/imgs/p2.png?raw=true "Title")
![Alt text](/docs/imgs/p3.png?raw=true "Title")

## Deploy

設定完上面項目就可以開始 `Deploy`

```
$ chalice deploy
```

deploy 完後會顯示你的 Rest API URL:

```
Rest API URL: https://<random>.execute-api.ap-northeast-1.amazonaws.com/api
```

接著再回去 Line Channel Settings 的 Webhook URL，填入進去並在後面加 `/callback`
```
<random>.execute-api.ap-northeast-1.amazonaws.com/api/callback
```
![Alt text](/docs/imgs/p4.png?raw=true "Title")


## 設定 Line Bot

你在建立完 Line Bot，預設是不會開啟 Webhook 機制

需要從 [Line Account Manager](https://manager.line.biz/)

1. 點選你的 Line Bot
2. 點選右上角 `設定`
3. 點選左邊 `回應設定`
4. 停用`自動回應訊息`, 啟用`Webhook`

![Alt text](/docs/imgs/p1.png?raw=true "Title")

這個時候你加你的Line Bot 就會回應你的訊息
