
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Readme.md-from-Course" data-toc-modified-id="Readme.md-from-Course-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Readme.md from Course</a></span><ul class="toc-item"><li><span><a data-toc-modified-id="list-of-files-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>List of files</a></span></li><li><span><a data-toc-modified-id="setup-instructions-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setup Instructions</a></span><ul class="toc-item"><li><span><a data-toc-modified-id="aws-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>AWS</a></span></li><li><span><a data-toc-modified-id="azure-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Azure</a></span></li><li><span><a data-toc-modified-id="ubuntu-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Ubuntu</a></span></li></ul></li></ul></li><li><span><a href="#Setup-instructions-for-AWS" data-toc-modified-id="Setup-instructions-for-AWS-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Setup instructions for AWS</a></span><ul class="toc-item"><li><span><a href="#Config-Notes-for-setup-automagically...." data-toc-modified-id="Config-Notes-for-setup-automagically....-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Config Notes for setup automagically....</a></span><ul class="toc-item"><li><span><a href="#Steps-to-build-an-a-machine-for-fast.ai" data-toc-modified-id="Steps-to-build-an-a-machine-for-fast.ai-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Steps to build an a machine for fast.ai</a></span></li><li><span><a href="#Elastic-machine" data-toc-modified-id="Elastic-machine-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Elastic machine</a></span></li><li><span><a href="#Build-machine-from-Template" data-toc-modified-id="Build-machine-from-Template-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Build machine from Template</a></span></li></ul></li><li><span><a href="#Configure-AWS" data-toc-modified-id="Configure-AWS-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Configure AWS</a></span><ul class="toc-item"><li><span><a href="#Profiles" data-toc-modified-id="Profiles-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Profiles</a></span></li></ul></li></ul></li></ul></div>

# # Readme.md from Course

# In[1]:


# Display the README.md file supplied with the course.
from IPython.display import display, Markdown

with open('README.md', 'r') as fh:
    content = fh.read()

display(Markdown(content))


# # Setup instructions for AWS

# * Local Machine
#     * Requires Anaconda python 2.7, 64 bit
#     * pip install awscli
#     * require Access Key ID and Secret Access Key (after create user); may not be able to get these later.
#     * run 
#         * aws configure, requires access key id, secret access key
#         * Region: us-west-2
#         * output: text
#     
#             
#     
# 

# ## Config Notes for setup automagically....

# * Screen "Choose AMI"
#     * for fast.ai in us-west-2
#     
# | ami          | where           | desc     | cost           | bid
# | ---          | ---             | ---      | ---            | --- |
# | ami-f8fd5998 |  us-west-2      | Oregon   |  0.29 to 0.31  | 0.3, sometimes not available    
# | ami-9c5b438b |  us-east-1      | Virginia |  0.19 to 0.38  | 0.23, often not available
# | ami-9e1a35ed |  eu-west-1      | Ireland  |  0.22 to 0.23  | 0.23, usually available
# | ami-00000000 |  ap-southeast-2 | Sydney   |  0.23 to 1.54  | 0.23, usually available
#         
# * Screen "Choose Instance Type"
#     * p2.xlarge   (real)  4cpu, 61 gig ram, 
#     * t2.xlarge   (test)  4cpu, 16 gig ram, cannot use spot rates on t2.xlarge
#     * m4.xlarge   (test)  4cpu, 16 gig ram, 
#     * Spot price for m4.large is about 4cents per hour, stable around 0.035
#     * Spot price for m4.xlarge is about 4cents per hour, stable around 0.038
# 
#     * to get pricing history Services > EC2 > Spot Requests > Pricing History
# 
# * Screen "Configure Instance"
#     * check "Request Spot Instanace"
#     * Set Max Price = 0.40   (40 c USD)
#     
# * Screen "Add Storage"
#     * default is 128 gig General Purpose SSD (GP2)
#     
# * Screen "Add Tag"
#     * Name "Paul Roetman"
#     * Shutdown "1800"
#     
# * Screen  "Configure security group"   
#     * Add additional rule for 8888 to 8891
#     
# 
# 

# ### Steps to build an a machine for fast.ai

# ### Elastic machine

# Notes: Build machine from scratch each time
# 
# 

# ### Build machine from Template

# * create template
# * build machine
# * run job
# * save results
# * shutdown machine
# 
# * Qu: How to handle fails

# Steps
# * build a m3.xlarge that can use all the libraries required for fast.ai (is this possible without GPU?)
# * automate this
# * Repeat for p2.xlarge, see how it goes.
# * introduce deliberate bug, see how it handles it.
# * -
# * Can test this on t2.micro, as it is free! 

# ## Configure AWS

# ### Profiles

# ```
# [default]
# aws_access_key_id=foo
# aws_secret_access_key=bar
# region = ap-southeast-2
# output = text
# 
# [profile us_east]
# aws_access_key_id=foo
# aws_secret_access_key=bar
# region = us-east-1
# output = text
# ```
# 
