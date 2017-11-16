
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
