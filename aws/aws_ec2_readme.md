# Elastic Compute Cloud.

## Useful links:
* [Automated Draining of spot instance nodes](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-supports-automated-draining-for-spot-instance-nodes-on-kubernetes/)

**Benchmarking**:
* [Tool for benchmarking EC2/S3 throughput](https://github.com/dvassallo/s3-benchmark)
* [EC2 instance connect](https://github.com/glassechidna/ec2connect)
* [EC2 instance connect - AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)



## Notes:
* Default maximum EC2 instance limit per region is 20.
* Within each family of instance type, there are several choices that scale
  up linearly in size. The hourly price for each size scales linearly as well.
* When the host on which an EC2 instance restarts, the instance will stay
  with the same EC2 host. But if the instance is stopped and then restarted 
  or if AWS stops the instance for maintenance etc on their end, then the 
  instance will be reassigned to another host in the same AZ.

* Instance metadata: http://169.254.169.254/latest/meta-data/                                
                                                                                
**Termination Protection**                                                      
* Prevents from accidental Termination from console, CLI or API.                
* It does not prevent termination triggered by an OS shutdown command,          
  termination from an ASG, or termination of a spot instance due to spot price  
  changes.  


## Instance types:

### General purpose

*T3*
* Low cost general purpose
* Burstable performance instances
* Provide a baseline level of CPU performance with ability to burst above the
  baseline.
* The baseline performancee and ability to burst are governed by CPU credits.
* Uses: webservers, developer environments and databases.

*T4*:
* Arm based Gavitron2 processors and delivers up to 40% better price performance
  over T3 instances.

*M5*:
* Latest generation of general purpose instances.
* Powered by Intel Xenon 8175M processors.
* 25 Gbps network bandwiidth using enhanced networking.
* Instance storage offered via EBS or 
* NVMe SSDs that are physically attached to the host server - provide block
  storage that is coupled to the lifetime of the M5 instances.

*MAC*:
* Powered by Apple Mac minni computers and built on AWS Nitro system.

*A1*:
* AMD based instances.
* Ideally usited for ARM based workloads.
* AWS Gravitron Processors - feature 64-bit Arm Neoverse cores.
   

### Compute optimized:
Ideal for compute bound applications that benefit from high performance processors.

*C5*:
* Delivers cost-effective high performance at low price per compute ratio.
* Requires HVM AMIs that include drivers for ENA and NVMe
* Up to 25 Gbps of n/w bandwidtth and 19 Gbps of dedicated bw to Amazon EBS.


### Memory optimized:
Deliver fast performance for workloads that process large data sets in memory.

*R4, R5*:
* High Frequency Intel Xeon E5-2686 v4 (Broadwell) processors
* DDR4 Memory
* Support for Enhanced Networking
* R5 delivers 5% additionnal memory per vCPU than R4.


### Accelerated computing:
Uses hardware accelerators, or co-processors to perform functions, such as
floating point number calculations, graphics processing or data pattern match.

*P3,P3,P4*
* GPU based instances, provide highest performance for ML training and
  HP computing in the cloud.

* 400 Gbps instance networkin support for Elastic Fiber Adapter and 
  NVIDIA GPUDirect RDMA (remote direct memory access)
* 600 GB/s peer to peer GPU communication with NVIDIA NVswitch

*F1*:
* Offers customizable hardware  acceleration with field programmable gate
  arrays (FPGA).


### Storage optimized:
Designed for workloads that reuire high, sequential read and write access to
very large data sets on local storage.

*I3*:
* Provides NVMe  SSD-backed instance storage, optimized for low latency,
  very high random I/O performance, high sequential read throughput and high
  IOPS at low cost.
* I3 also provides bare metal instances (I3.metal)
* Up to 25 Gbps of n/w bandwidth using ENA based enhanced networking.

*D2, D3*:
* Optimized for applications that require high sequential I/O performance
  and disk throughput.
* Up to 48 TB of HDD instance storage.
* D3 offers Up to 45% higher read and write disk throughput than D2 instances.


### Instance features:

*Burstable Performance Instances*:

* A CPU Credit provides the performance of a full CPU core for one minute.

* Eg: a t2.small instance receives credits continuously at a 
  rate of 12 CPU Credits per hour. 
* This provides baseline performance equivalent to 20% of a CPU core (20% x 60 mins = 12 mins). 
* If the instance does not use the credits it receives, they are stored in 
  its CPU Credit balance up to a maximum of 288 CPU Credits. 
* When the t2.small instance needs to burst to more than 20% of a core, it draws 
  from its CPU Credit balance to handle this surge automatically.

*Multiple storage options*:

*EBS-optimized instances*:

*Cluster networking*:


### Measure instance performance:


## AMIs
* AMIs define the initial software that will be on an instance when launched.
* OS, Initial state of any patches, application or system software.

There are 4 sources:
* Published by AWS
* AWS Marketplace
* Generated from existing instances
* Uploaded virtual servers

* When launching windows instance, EC2 generates a random password for the
  local admin account and encrypts the password using a public key. initial
  access is obtained by decrypting the password with the private key, either
  in the console or using API.
  The decrypted password can be used to login into the instance with local
  admin account via RDP.

* You can only export previously imported EC2 instances. Instances launched     
  within AWS from AMIs cannot be exported.                                      
                                                                                
                                                                                

## Security Groups:
* Virtual firewall
* Security groups have different capabilities depending on whether they are
  associated with a VPC or EC2 classic.
EC2 classic SG -- Control outgoing instance traffic
VPC SG         -- Control outgoing and incoming instance traffic.

* SG is stateful firewall; that is an outgoing message is remembered so that
  the response is allowed through the SG without an explicit inbound rule
  being required.
* Changes to SG are immediate.
* Everything is denied by default. You can add a SG Rule to allow traffic,
  you cannot add a rule to deny traffic.















