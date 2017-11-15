
# coding: utf-8

# # 10000 foot overview

# * Region: Geographical area. Each region consists of 2 (or more) Availability Zones
# * Availability Zone: Data Centre  
# e.g. Region may consist of 3  data centres, AZ-A, AZ-B, AZ-C
# 
# 

# ### Edge Location
# * CDN End Point for CloudFront (content delivery network)
# * used to cache very large media file distribution
#     * first access, needs to be downloaded from source (eg New York)
#     * second time it is called, it would have been cached in Oz on Edge Location, so much faster.
# * many more edge locations than there are regions.

# ## Services

# ### Networking and Content Delivery
# 
#     

# #### VPC - Virtual Private Cloud
# * VPC: virtual private cloud
# * think of it as a virtual data centre
# * multiple VPC per region
# * can connect one VPC to another VPC   
# * Huge part of exam....
# 

# #### Rout53 - DNS
# * Route53: Amazon DNS system
# * 53 is DNS port on the static port list, named after Route 66 (first interstate opened in USA
# 

# #### Cloud Front
# * used to be in storage section
# * basically a collection of edge locations

# #### Direct Connect
# * Dedicated telephone line connection directly into AWS data centre
#     * security
#     * high speed

# ### Compute

# #### EC2 - Elastic Compute Cloud
# * Virtual machine in cloud (like VMWare)
# 

# #### EC2 Container Service
# * Hightly Scalable Highly Performing  Container Management Service
# * docker containers
# * run app on managed cluster of ec2 instances
# * no need to install, manage, etc your own hardware

# #### Elastic Beanstalk
# * You upload your code
# * beanstalk will provision/deploy code that is suitable for your app

# #### Lambda
# * on EC2, you can log into server (via ssh, login:, etc)
# * on lambda, serverless
# * no OS
# * you upload your code
# * code will respond

# #### Lightsail
# * out of the box cloud
# * eg for wordpress
# * 

# ### Storage

# #### S3
# * Simple Storage Service
# * virtual disk in cloud
# * disk only, not database files, etc.
# * place objects in cloud

# #### Glacier
# * store files from S3 to Glacier
# * very slow recovery (3 to 4 hours minimum recovery time)
# * store files for compliance reasons

# #### EFS
# * Elastic File Service
# * file based storage, can be shared
# * you could install application or db files.

# #### Storage Gateway
# * Connect S3 to your on prem servers
# * usually a virtual machine you install on-prem

# ### Databases

# #### RDS
# * MySql, Oracle, Sql Server, Postgress SQL, MariaDB, 
# * Aroura (2 flavours Postress, MySql)

# #### Redshift
# * Data Warehouse
# * mainly for a copy of your Prod DB
# * used for reports

# #### DynamoDB
# * Non Relation DB
# * NoSql DB
# * High Perf, High Scalable

# #### Elasticache
# * cache your data in the cloud
# * takes load of DB

# ### Migration Service

# #### Snowball
# * started out as Import/Export
# * Enterprise level to move terrabytes of data to the cloud
# * ready for Amazon to load for you.

# #### DMS
# * migrate on prem to cloud
# * migrate AWS region to region
# * no downtime
# * migrate from Oracle to Aurara (for example)

# #### SMS
# * Server Migration Service
# * migrate virtual machine to cloud

# ### Analytics

# #### Athena
# * run sql queries directly on S3
# * turns flat files into a pseudo database

# #### EMR 
# * Elastic Map Reduce
# * Process large amount of data (uses hardoop)

# #### Cloud Search / Elastic Search
# * cloud - fully managed search managed by AWS
# * Elastic - open source framework
# * create search capabilities within your application.

# #### Kinesis
# * stream and analys real time data
# * financial transactions analyzed on the fly
# * social media streams analyzed on the fly

# #### Data Pipeline
# * move data from one place to another
# * eg s3 to dynamo db or visa versa

# #### Quick Sight
# * business analytics tool

# ### Security and Identity

# #### IAM
# Identity Access Management
# create users, groups, assign users to groups

# #### Inspector
# Agent to install on virtual machine
# Does Security reporting

# #### Certificate Manager
# free SSL cert for your domain name

# #### Directory Service
# Use AD, connect AWS to your AD

# #### WAF
# Web Application Firewall
# application level protection to your firewall
# stop sql injection, cross site scripting, etc

# #### Artifacts
# Doc in console
# Compliance Reports
# eg get iso27001 certification

# ### Management Tools
# #### Cloud Watch
# monitor Performance of AWS environment
# disk utilization, cpu, etc
# 
# #### Cloud Formation
# turn intrastructure into code
# instead of having network / switch / etc / load balancers
# it is a doc that describes your env.
# Then deploy at will.
# 
# #### Cloud Trail
# Audit AWS Resource
# 
# #### Opsworks
# Automate deployments using "chef" -- i guess its like puppet
# 
# #### Config
# monitor env
# audit env, can set alerts for changes in policy
# 
# #### Service Catalog
# for Larger enterprises
# Can authorize certain types of eg ec2, and not auth other types of ec2.
# 
# #### Trusted Advisor
# Aws Sol Arch Team will come to your org, make a series of recommendataions
# trusted advisor will automate this process
# eg build a more fault tolerant env.
# 

# 
# ### Application Services
# #### Step Functions
# visualize what is going on in your application
# 
# #### SWF
# simple workflow services
# co-ordinate automated tasks and human tasks
# 
# #### API Gateway
# door
# create, monitor, secure gateways at scale
# door for apps to access backend data.
# 
# #### AppStream
# stream desktop app to users
# 
# #### Elasic Transcoder
# Transform a video to any different type required for diff machine
# 
# 

# 
# 
# ### Developer Tools
# ####Code Commit
# basically github
# 
# #### Code Build
# compile code
# pay by minute
# 
# #### Code deploy
# deploy code to ec2 instances
# 
# #### code pipeline
# keep track of code in diff environments (diff version in uat to prod).
# 
# 
# 

# ### Mobile Services
# 
# ####  Mobile Hub
# add, configure and design features for mobile apps
# user auth, backend storage, etc
# 
# #### Cognito
# users sign up and sign into your apps using social media id
# 
# #### Device Farm
# quality of ios / android improved by testing on hundreds of real world apps
# 
# #### Mobile Analytics
# simply and cost effectivly collect app usage data
# 
# #### pinpoint
# enable understand mobile users - google analytics for mobile app.
# 
# 
# 

# ### Business Productivity 
# #### Work Docs
# store docs in cloud, lots of security
# 
# #### WorkMail
# exchange for AWS
# 

# ### IOT
# #### iOT
# internet of things
# 

# ### Desktop and App Streaming
# 
# #### WorkSpaces
# vdi - desktop in cloud
# 
# #### AppStream 2.0
# stream desktop app to users
# 

# ### Artificial Intelligence
# 
# Read this book: Superintelligence by Nick Bostrom; Paths, Dangers, Strategies
# 
# #### alexa
# lex is the service, no longer need an echo
# 
# #### polly
# take any text, turn into voice
# diff voice, diff language
# 
# #### Machine Learning
# give a data set
# give it outcomes
# predict outcome
# 
# #### Rekognition
# upload picture
# will tell you what is in that picture
# 
# 

# ### Messaging
# 
# #### SNS 
# simple notification services
# email
# sms/text
# publishing
# http/https
# 
# #### SQS
# decouple app
# queue system
# 
# #### SES
# simple email service
