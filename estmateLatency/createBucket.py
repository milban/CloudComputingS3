import boto3
regoinList = [
    'us-east-2', #미국 동부(오하이오) O
    'us-east-1', #미국 동부(버지니아 북부) O
    'us-west-1', #미국 서부(캘리포니아 북부 지역) O
    'us-west-2', #미국 서부(오레곤) O
    'ap-south-1', #아시아 태평양(뭄바이) O
    'ap-northeast-2', #아시아 태평양(서울)
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

for region in regoinList:
    s3 = boto3.client('s3', region_name=region)
    s3.create_bucket(Bucket='milbans-{0}'.format(region), CreateBucketConfiguration={'LocationConstraint': region})