# Download sourcecode to your enviroment
```
$ git clone https://github.com/so1/kroon-kintone.git
```


# Setup AWS Lambda
## How to create zip to upload
You need upload sourcecode and libraries to AWS Lambda.

```
$ pip install -r requirements.txt -t ./ # installing required libraries
$ zip -r ./lambda-function.zip . 
```

## Create AWS Lambda instance
https://ap-northeast-1.console.aws.amazon.com/lambda/home?region=ap-northeast-1#/create/select-blueprint
Upload zip file from UI of AWS Lambda
https://slack-files.com/T3D8575L6-F3QJEUZ55-37177da051

# Get page token to post facebook page
see facebook_token/README.md

# github usage for me
kroon-kintone のdirで
```
$git pull #最新をとってくる
$git commit -am "write my commit message" filename #addしつつコミットする。 filenameを.にすると、そのdir全部
$git push #レポジトリに送る
$git add filename #
