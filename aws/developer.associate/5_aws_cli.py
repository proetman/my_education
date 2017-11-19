
# coding: utf-8

# # AWS CLI Command Line Interface

# ## Setup / Configure
# ---
# 
# * aws configure
#     * enter key id:
#     * enter Secret Access Key:
#     * enter default region     (google aws region list)
#     * enter detault output   
#     
#  ---
#  
# * Example:
#      * aws s3 ls
#      * aws s3 help     -- display options for this service
#      * aws ec2 describe-instances    -- list all instances
#      * aws ec2 terminate-instances --instance-ids i-123456

# ## Identity Access Mangement Roles Lab
# ---
# * if you loose your credentials, someone will upload a huge bitcoin miner and drain your account.
# * select IAM
# * Create Service Role (note this is GLOBAL)
#     * click Amazon EC2
#     * Filter by S3
#     * Select S3 Full Access > Next
#     * name: S3-Admin-Access
# * Create EC2
#     * On configure Instance Details, add IAM Role: S3-Admin-Access
#     * everything else default.
# * Note: can add additional policies on the fly 
#     * EC2 > Actions > Instance Settings > Add/Replace IAM Role
# * Log into EC2
#     * aws s3 ls     -- Now works without adding any credentials!!! Yay.
#     * can still set default region using aws credentials, but add no key or id.

# # S3 CLI and Regions
# ---
# * create a default instance
# * Create S3 buckets
# * copy from buckets to EC2
#     * aws s3 cp --recursive s3://{s3-name}/ /home/ec2-user/target_dir 
#     * aws s3 cp --recursive s3://{s3-name}/ /home/ec2-user/target_dir --region eu-west-2   
#     * --region flag only required to copy from some regions; but if copying across regions, prob good idea to get into habit of using it.
#     
