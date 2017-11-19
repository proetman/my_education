
# coding: utf-8

# # EC2
# 

# * EC2 stands for Elastic Compute Cloud
# 
# * web service that provides resizable compute compute capacity in cloud.
# * reduce time req to obtain, boot new server to minutes
# * allows quick scale in capacity both up and down and requirements change.
# 
# * what is it? It is a virtual linux|windows server
# 
# * Startups now do not require dollars for hardware, they can experiment!
# 
# * allow you to pay only for the capacity that you actually use.
# * provides dev the tools to build failure resilient applications and isolate themselves from common failure scenarios
# 
# ## EC2 Options
# 
# * __On Demand__ allow you to pay fixed rate by hour or second with no commitment
#     * users want low cost, flexibility of ec2 without up front payment or commitment
#     * apps with short term, spiky or unpredictable workloads that cannot be interrupted
#     * apps developed or tested on ec2 for first time
#     
# * __reserved__ provide you with capacity reservation, offer significant discount on hourly charge, 1 year or 3 year terms.
#     * steady state or predicatable usage
#     * apps that require reserved capacity
#     * user able to make up front payments to reduce compute costs even further
#     * standard RI (up to 75% discount)  RI = reserved instance; 
#     * convertible RI ( up to 54% discount) capability to change attributes of RI as long as the exchange results in the createion of RI of equal or greater value
#     * scheduled RI's available to launch within timeframe you reserve. Match capacity to predictable recurrinng schedule (eg batch jobs)
#     
# * __spot__ bid whatever price you want for instance capacity, providing for even greater savings if your applications have flexible start and end times. You set your bid price (how much you are willing pay), if the price goes above your price, your machine shuts down. If below, then your machine fires up!
#     * flexible start/end times
#     * apps that are only feasible at very low compute prices
#     * users with urgent computing needs for large amounts of additional capacity
#     * if you terminate instance before hour is complete, you pay for whole hour anyway.
#     * if amazon terminates instance, you get the hour it was terminated in for free!  :)
#     
# * __Dedicated Hosts__ physical ec2 server dedicated for your use. reduce cost by allowing you to use your existing server-bound software licenses.
#     * useful for regulatory req that doesn't support multi tenant virtualization
#     * great for licensing that doesn't support multi tenant v.
#     * can be purchased on-demand (hourly)
#     * can be purchased as a reservation for up to 70% off the on demand price.
# 
# 

# Letter is type, Number is generation
# 
# eg D for Dense, 2 for 2nd generation!
# 
# 
# | Family | Speciality | Use Case |
# | ---    | ---        | ---      |
# | d2 | Dense Storage | Fileservers / Data Warehouse|
# | r4 | Memory Optimized | Mem intesive apps  (r = ram)|
# | m4 | General Purpose | Application SErvers  (m = main choice)|
# | c4 | Compute Optimized | CPU intensive |
# | g2 | Graphics intesive| video encoding/3d app streaming|
# | i2 | High Speed Storage | nosql, data warehsouse  (i = iops)|
# | f1 | field programmable gate array | hardware accelarate your code |
# | t2 | low cost general purpose | web servers/ small db (t= tiny) |
# | p2 | graphics / general purpose GPU | machine learning, bit coin mining  |
# | x1 | memory optimized| SAP Hana/Apache Spark/etc (x=extream memory)|
# 
# 
# ##### ec2 intance types
# * d - density
# * r - ram
# * m - main choice
# * c - compute
# * g - graphics
# * i - iops
# * f - fpga
# * t - tiny general purpose
# * p - graphics
# * x - extreame memory
# 
# dr mc gift px
# 
# 
# 

# # EBS

# __ebs__ allows you to
# * create storage volumes and attach them to ec2 instance
# * create file system on that volume
# * they are placed in a specific availability zone where they are automatically replicated to protect from failure of a single component.
# * block based storage (so can install OS, DB, etc), not file based like S3
# 
# * you cannot mount 1 EBS volume to multiple EC2 instances, instead use EFS
# 
# ### EBS Volume Types
# * 4 or 5 of them
# * General Purpose SSD (GP2)
#     * balance price and performance
#     * 3 IOPS per gig, up to 10,000 IPOS; ability to burst up to 3000 IOPS for extended periods of time for volumns at 3334 GiB and above
# * Provisioned IOPS SSD (IO1) 
#     * IO intensive apps like large db or nosql db
#     * use if need more than 10,000 IOPS
#     * up to 20,000 IOPS
# * Throughput Optimized HDD (ST1) 
#     * old style hard drive (magnetic)
#     * big data]
#     * data warehaouse
#     * log processing
#     * cannot be a boot volume
# * Cold HDD (SC1)
#     * lowest cost storage for infrequence accessed workloads
#     * file server
#     * not boot volume
# * magnetic (standard)
#     * lowest cost per gig that is bootable. mag vol ideal for workloads where data is access infrequently, apps where lowest storage cost is important
# 
# 

# ## Launch EC2 - ec2 lab 101

# Two types of virtualization
# * HVM hyper virtual machine
# * PVM Para virtual machine   NFI what the difference is.
# 
# Launch
# * select Amazon Linux AMI (HVM), includes bunch of stuff including aws cli)
# * subnet: one subnet = one availability zone, a subnet cannot cross av. zones.
# * In Advanced Details > User Data: can add details like download and install anaconconda, install product x, etc.
# * Security Groups === Firewall
# 

# * Connect to EC2
# ```
# ssh -i "cloudops_training.pem" ec2-user@ec2-13-54-65-78.ap-southeast-2.compute.amazonaws.com
# ```
# 
# * Install Apache
# ```
# yum update
# yum install httpd
# cd /var/www/html
# vi index.html
# <html><h1>Hello Cloud Gurus!</h1></html>
# :wq
# service httpd start
# chkconfig httpd on      # start httpd on boot.
# ```
# * Navigate on web browser to public name, and web page will start!

# * EC2 Console
# 
# * System Status Check - verifies that the hardware to connect to your virtual machine is ok.
# * Instance Status Check - verifies that your machine is ok.

# * Reserved Instances
# * select reserved instance from menu
# * select options
# * review costs

# Note:
# * Termination Protection is turned off by default, you must turn it on
# * on EBS instance, default actions if for root EBS vol to be deleted when instance is terminated.
# * EBS root vol of DEFAULT ami cannot be encrypted.
#     * can use 3rd party tools to encrypt (eg bit locker on windows)
#     * create your own AMI, in process - encrypt root vol.
# * Additional volumes can be encrypted.

# ## PUTTY and PUTTYKeyGen

# * when creating an EC2, save PEM file
# * use puttykeygen to convert PEM to PPK
# * save PPK file into putty config
# * good to go!

# ## Security Groups
# 
# * From security Groups on AWS console
# * any change applied immediatly
# * if remove HTTP from a rule, then HTTP is no longer available.
# 
# * Rules are STATEFUL
# * if you allow something IN, then it is automatically allowed back out.
# * you can remove the rules for OUTBOUND, and everything still works.
# * ssh session freezes though
# 
# * Everything is deny by default.
# * can add multiple security groups to a single machine, they are cumulative.
# * there is no deny, so cannot be a conflict.
# 
# * NACL are STATELESS (inbound does not allow outbound). NACL network access control list
# * cannot block using SG, need to use NACL

# ## Storage  
# ---
# 
# * create an EC2 with a bunch of different storage types
# * navigate to volumes 
#     * select gp2 (boot volume)
#     * actions > create snapshot
# * Once created, navigate to snapshots, then you can create a volumn from a snapshot
# * you can determine the availability zone it should reside in
# * you can change the volume type (SSD, Cold HDD, etc)
# ---
# * more in snapshots
# * copy - can copy a snapshot to anywhere in the world (ie change region).
# * so, to move an instance from one region to another
#     * create snapshot
#     * copy snapshot to other region
#     * create image from snapshot
#     * create ec2 from volume
#     
# --- 
# * To create a new image:
#     * create snapshot
#     * select snapshot, actions > create image
#     * navigate to Images > AMI (takes a while to show up)
#     
# ---
# * NOTE: if create image from snapshot from machine with multiple disks, it fucks up.
# * instead, create image from working machine and in the process, remove the extra disks
# * running machine > actions > create image > remove extra disks > go
# 
# --- 
# * NOTE2: when terminating (deleting) instances, only the root volume is removed. ANy other volume needs to be manully removed from the volume tab.
# 
# ---
# * Volumes exist on EBS - they are just a virtual hard disk
# * root devise is where OS installed
# * snapshot exist on S3 (but it is not visible)
# * snapshot is a point in time of volume
# * after time, next snap is just the diff from the prev snap.
# 
# * to backup a EBS root vol, should probably stop instance first.
# * but you can take a snap while running
# * create AMI from volume or snapshot
# * can change EBS vol size on fly... and also change storage type on the fly
# * volumes always in the same availability zone as the  ec2 
# ---
# * snapshots of encrypted vol are encrypted automatically
# * vol restored from encrypted snapshot are encrypted automatically
# * you can share snapshot, but only if unencrypted
# * snapshot can be shared with other aws accounts, or made public.
# ---
# 
# 
# 

# ## EFS - Elastic File System
# ---
# * file storage for Elastic compute Cloud (EC2)
# * create and configure file systems quickly 
# * storage is elastic, grow and shrink automagically as you add/remove files
# ---
# * support NFSv4 - Network File System ver 4
# * only pay for what you use (no pre-provisioning)
# * scale up to petabyte
# * can support thousands of concurrent NFS connections
# * data is stored across multiple AZ within a region
# * block based storage (not object based storage), can share with other ec2 instances
# * Read after Write consistency
# 

# ### Setup Web Server with load balancing

# * Navigate to EFS > create filesystem > defaults and Tags > Create
# * Create 2 EC2 instances with httpd installed, on each, set the subnet to a different AZ
#     * check that EC2 instances are in same security group as the EFS 
# * Create a Load Balancer > give it a name > default VPC > Security Group > Add in both EC2 instances
# * Install httpd on both, and start
# * verify /var/www/html is empty on both machines
# * Navigate back to EFS > Select your EFS > click on "ec2 mount instructions". Most of the software has already been installed...just need the last command.
#     * sudo mount -t nfs $(curl -a http://x.x.x.x/latest/meta-data/placement/availability-zone).fs...com:/ efs
#     * default is to mount onto /efs (last part of command above)
#     * change to sudo mount -t nfs $(curl -a http://x.x.x.x/latest/meta-data/placement/availability-zone).fs...com:/ /var/www/html
#     * create index.html with stuff in it
# * go to Load Balancer > instances > check health - shoudl be "in service"
# * description tab gives DNS name, navigate to there, should be your web page!
