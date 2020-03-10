# Getting started with Elasticache

# Scenario #1:

# #1: No Cluster Mode
# #2: No Replicas


Sign in to the AWS Management Console and open the Amazon ElastiCache console at https://console.aws.amazon.com/elasticache/.

Choose Get Started Now.

If you already have an available cluster, choose Launch Cluster.

From the list in the upper right corner, choose the AWS Region that you want to launch this cluster in.

For Cluster engine, choose Redis.

Make sure that Cluster Mode enabled (Scale Out) is not chosen.

Complete the Redis settings section as follows:

For Name, type a name for your cluster.

Cluster naming constraints are as follows:

Must contain 1–40 alphanumeric characters or hyphens.

Must begin with a letter.

Can't contain two consecutive hyphens.

Can't end with a hyphen.

From the Engine version compatibility list, choose the Redis engine version you want to run on this cluster. Unless you have a specific reason to run an older version, we recommend that you choose the latest version.

In Port, accept the default port, 6379. If you have a reason to use a different port, enter the port number.


For Node type, choose the node type that you want to use for this cluster. For this exercise, above the table choose the t2 instance family, choose cache.t2.small, and finally choose Save.

For more information, see Choosing Your Node Size.

From Number of replicas, choose the number of read replicas you want for this cluster. Because in this exercise we're creating a standalone cluster, choose None.


Choose Advanced Redis settings and complete the section as follows:


For Availability zone(s), you have two options.

No preference – ElastiCache chooses the Availability Zone.

Specify availability zones – You specify the Availability Zone for your cluster.

For this exercise, choose Specify availability zones and then choose an Availability Zone from the list below Primary.

For Availability zone(s), you have two options.

No preference – ElastiCache chooses the Availability Zone.

Specify availability zones – You specify the Availability Zone for your cluster.

For this exercise, choose Specify availability zones and then choose an Availability Zone from the list below Primary.

For more information, see Choosing Regions and Availability Zones.

From the Security groups list, choose the security groups that you want to use for this cluster. For this exercise, choose default.

For more information, see Amazon VPCs and ElastiCache Security.

Because this is not a production cluster, clear the Enable automatic backups check box.

I didnt enter anything here - If you are going to seed your cluster with data from a .RDB file, in the Seed RDB file S3 location box, enter the Amazon S3 location of the .RDB file.


