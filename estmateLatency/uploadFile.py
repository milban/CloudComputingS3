import boto3
import time

regoinList = [
    'us-east-2', #미국 동부(오하이오) O
    'us-east-1', #미국 동부(버지니아 북부) O
    'us-west-1', #미국 서부(캘리포니아 북부 지역) O
    'us-west-2', #미국 서부(오레곤) O
    'ap-south-1', #아시아 태평양(뭄바이) O
    'ap-southeast-1', #아시아 태평양(싱가포르)
    'ap-southeast-2', #아시아 태평양(시드니)
    'ap-northeast-1', #아시아 태평양(도쿄)
    'ca-central-1', #캐나다(중부)
    'eu-central-1', #EU(프랑크푸르트)
    'eu-west-1', #EU(아일랜드)
    'eu-west-2', #EU(런던)
    'eu-west-3', #EU(파리)
    'eu-north-1', #EU(스톡홀름)
    'sa-east-1', #남아메리카(상파울루)
]

s3 = boto3.client('s3', region_name='ap-northeast-2')

bucketNameList = []
for region in regoinList:
    bucketNameList.append('milbans-{0}'.format(region))

fileNameList = ['../examFile/1KB', '../examFile/10KB', '../examFile/1MB', '../examFile/10MB',]

beforeTime = 0
afterTime = 0
for bucketName in bucketNameList:
    for fileName in fileNameList:
        beforeTime = time.time()
        for i in range(0, 10):
            s3.upload_file(fileName, bucketName, fileName.split('/')[-1])
        afterTime = time.time()
        with open('./uploadResult.txt', 'a') as file:
            realFileName = fileName.split('/')[-1]
            file.write("{0} file to {1} region: {2}\n".format(realFileName, bucketName.split('-')[1:], (afterTime-beforeTime)/float(10)))