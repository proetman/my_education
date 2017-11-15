
# coding: utf-8

# # Identity Access Managment 101

# * Manage users
# * level of access
# 
# * Centralized control of AWS account
# * Shared access to AWS console
# * Granular Permissions
# * Identity Federations (including AD, Facebook, Linkedin, etc)
# * Multi-factor Authentication
# * temp access to users/devices and services where necessary
# * setup own password rotation policy
# * supports PCI DSS Compliance
# 
# Critical Terms
# * Users - end users
# * Groups - collection of users under one set of permissions
# * Roles - create roles assign them to aws resources (eg assign role that ec2 can write directly to s3, so it is not user based!)
# * Policies - doc that defines one (or more) permissions. Can attach to user, or group, or role, or all three!
# 
# 

# # 101 - Lab

# First, customize your account name. Click customize, then select a name (needs to be unique in the world).
# ![customize](images/customize_name.png)
# 
# After changing, your IAM User sign-in link changes to   
#     https://new_username.signin.aws.amazon.com/console

# ### Enable MFA - Multi Function Device
# 
# Under Security Status, there are a bunch of "bad" security options.
# * click enable MFA
# * Select virtual MFA device, click the "here" button to see full list of apps [here](https://aws.amazon.com/iam/details/mfa/)
# * Install Google Authenticator on Apple Phone, then scan QR code
# * Add the next two codes that show up on app onto screen
# * finilize
# 

# ### Add Users
# 
# Create two users 
# * bob
# * mary
# 
# For both, select programmatic access and AWS Management Console Access
# 
# Assign password/change at next login/etc
# 
# * On "next" it flicks to next screen to "set permissions for BOB and MARY".
# * can
#     * add users to group
#     * copy perm from existing user
#     * attach existing policies directly
# * here , we are going to create a group (eg group for dev, group for finance, etc)
# * create group for system-admins
# * "policy type" type in Admin, list will be filtered
# * for this case, we will select adminstrator access, which is god level.

# ### Create Group Names and Roles
# * Groups
# * create group: testgroup_hr
# * assign policy S3 read only
# * remove bob from Admin, add to testgroup_hr
# * you can then add permissions directly to bob, rather than using groups.
# 
# * if you loose the access key, deactivate the lost key, then create new access key in Security Credentials section
# 
# * Can also allocate a ROLE to a user
# * role in this case will allow EC2 to call an AWS Service on your behalf.
# * EC2 will call Lambda on your behalf.
# * on Permissions window, select Full S3 access
# * give it a name "S3-Admin-Access", desc: This is full access to S3 for EC2
# * now that ROLE exists
# * can apply that role to an EC2 instance when it is created.
