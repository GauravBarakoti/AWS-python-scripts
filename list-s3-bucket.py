import boto3

s_ob=boto3.resource('s3')

for i in s_ob.buckets.all():
    print (i.name)
