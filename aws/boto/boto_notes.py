
# coding: utf-8

# # Boto

# ## Session
# 
# * initiate the connectivity to AWS services. 
# * e.g. following is default session that use the default credential profile(e.g. ~/.aws/credentials, or assume your EC2 using IAM instance profile )
# 
# ```
# sqs = boto3.client('sqs')
# s3 = boto3.resource('s3')
# ```
# 
# * Default session is limit to the profile or instance profile used
# * sometime you need to use the custom session to override the default session configuration (e.g. region_name, endpoint_url, etc. ) e.g.
# 
# ```
# # custom resource session must use boto3.session to do the override
# my_west_session = boto3.session(region_name = 'us-west-2')
# my_east_sesison = boto3.session(region_name = 'us-east-1')
# backup_s3 = my_west_session.resource('s3')
# video_s3 = my_east_sesison.resource('s3')
# ```
# ```
# # you have two choices of create custom client session. 
# backup_s3c = my_west_session.client('s3')
# video_s3c = boto3.client("s3", region_name = 'us-east-1')
# ```
# 
# ## Resource
# 
# * high level service class recommended to be used. 
# * allow you to tied particular AWS resources and pass it along
# * just use this abstraction than worry which target services is pointed to. 
# * As you notice from the session part, if you have a custom session, you just pass this abstract object than worrying of all custom region,etc to pass along. Following is a complicate example 
# * Example: 
# 
# ```
# import boto3 
# my_west_session = boto3.session(region_name = 'us-west-2')
# my_east_sesison = boto3.session(region_name = 'us-east-1')
# backup_s3 = my_west_session.resource("s3")
# video_s3 = my_east_sesison.resource("s3")
# backup_bucket = backup_s3.Bucket('backupbucket') 
# video_bucket = video_s3.Bucket('videobucket')
# 
# # just pass the instantiated bucket object
# def list_bucket_contents(bucket):
#    for object in bucket.objects.all():
#       print(object.key)
# 
# list_bucket_contents(backup_bucket)
# list_bucket_contents(video_bucket)
# 
# ```
# 
# ## Client
# 
# * low level class object. 
# * For each client call, you need to explicitly specify the targeting resources, the designated service target name must be pass long. 
# * You will lost the abstraction ability.
# * For example, if you only deal with default session, this looks similar to boto3.resource.
# 
# ```
# import boto3 
# s3 = boto3.client('s3')
# 
# def list_bucket_contents(bucket_name):
#    for object in s3.list_objects_v2(Bucket=bucket_name) :
#       print(object.key)
# 
# list_bucket_contents('Mybucket') 
# ```
# 
# * However, if you want to list objects from bucket in different region, you need to specify explicit bucket parameter required for client.
# 
# ```
# import boto3 
# backup_s3 = my_west_session.client('s3',region_name = 'us-west-2')
# video_s3 = my_east_sesison.client('s3',region_name = 'us-east-1')
# 
# # you must pass boto3.session.client and the bucket name 
# def list_bucket_contents(s3session, bucket_name):
#    for object in s3session.list_objects_v2(Bucket=bucket_name) :
#       print(object.key)
# 
# list_bucket_contents(backup_s3, 'backupbucket')
# list_bucket_contents(video_s3 , 'videobucket') 
# ```

# # EC2

# ## Display VPCS Info
# 
# ```
# l_session = boto3.Session(profile_name = g_profile)
# ec2_resource = l_session.resource('ec2') 
# for r in ec2_resource.meta.client.describe_vpcs()[ 'ResponseMetadata']: 
#     print(r)
# ```
# - RetryAttempts
# - HTTPStatusCode
# - RequestId
# - HTTPHeaders
# 
# ---
# 
# ```
# l_session = boto3.Session(profile_name = g_profile)
# ec2_resource = l_session.resource('ec2') 
# for r in ec2_resource.meta.client.describe_vpcs()[ 'Vpcs']: 
#     print(r)
# ```
# ```
# {u'VpcId': 'vpc-1c6aec64', u'InstanceTenancy': 'default', u'State': 'available', u'DhcpOptionsId': 'dopt-76acce0f', u'CidrBlock': '10.0.0.0/28', u'IsDefault': False}
# {u'VpcId': 'vpc-f58d378d', u'InstanceTenancy': 'default', u'State': 'available', u'DhcpOptionsId': 'dopt-76acce0f', u'CidrBlock': '172.31.0.0/16', u'IsDefault': True}
# ```

# ## Display EC2 info
# 
# ```
# for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
#     print(status)
# ```    
# 
# ```
# import boto3
# 
# instances = [i for i in boto3.resource('ec2', region_name='ap-southeast-2').instances.all()]
# 
# # Print instance_id of instances that do not have a Tag of Key='Foo'
# for i in instances:
#   if 'Foo' not in [t['Key'] for t in i.tags]:
#     print i.instance_id
# ```
# 
