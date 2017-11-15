
# coding: utf-8

# # Security Token Service (STS)

# * grants users limited and temp access to aws resources
# * users from
#     * federation (typically AD)
#         * users SAML - security assertion markup language
#         * temp access based on AD cred; does not need to be user in IAM
#         * signle sign on allows users to log in to aws console without assigning IAM credentials
#     * federation with mobile apps
#         * use facebook/amazon/google or other openID
#     * cross account access
#         * users from one aws account access resources in another.
# 
# 
# 
# ## Key Terms
# 
# * Federation: combine/join list of users in one domain (eg IAM) to another (AD, or Facebook)
# * Identity Broker: service allows take id from point A, and join it (federate it) to point B. This does not normally come out of the box, you need to develop it yourself.
# * Identity Store: Service like AD, Facebook, Google, etc
# * Identities: user of a service
# 
# 

# ## Scenario
# 
# ### Scenario 1
# you are hosting company website on ec2 web servers in your VPC. Users log in to site which then authenticates against company AD server based on site at companies HQ. Your VPC is connnected to your company HQ via securiyt IPSEC VPN. Once logged in, user can only have access to there own S3 bucket.
# 
# How do you set this up?
# 
# ![STS Scenario](images/STS_example.png)
# 
# 1. Employee enters username/password
# 1. app call id broker, broker captures u/p
# 1. id broker uses org's LDAP dir to validate u/p
# 1. id broker call new GetFederationToken function using IAM credentials. Call must include IAM policy and duartion (1 to 36 hours), along with policy that specifies permission to be granted to the temp security credentials.
# 1. the STS confirms policy of IAM user making call to GetFederationToken gives perm to create new tokens and then returns four values
#     * access key
#     * secret access key
#     * token
#     * duration
# 1. id broker returns temp security cred to reporting app
# 1. data storage app uses temp security cred (including tokens) to make requests to S3
# 1. S3 uses IAM to verify the creds allow the requested op on give s3 bucket and key
# 1. IAM provides s3 with go-ahead to perform requested app.
# 
# Broken down into major steps only:
# 
# 1. Develop ID Broker to communicate with LDAP and AWS STS
# 1. ID Broker always authenticates with LDAP first, then with AWS STS
# 1. App then get temp access to AWS resources.
# 
# 
# ### Scenario 2
# 
# 1. develop ID Broker to communicate with LDAP and AWS STS
# 1. ID Broker always auth to LDAP first, gets IAM ROLE associated with user
# 1. App then auth with STS and assumes that IAM Role
# 1. App user IAM role to interact with S3
# 
# 
# 
