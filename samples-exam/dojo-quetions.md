Here are 10 AWS Certified Security Specialty SCS-C03 practice exam questions to help you gauge your readiness for the actual exam.

Question 1
A leading hospital has a web application hosted in AWS that will store sensitive Personally Identifiable Information (PII) of its patients in an Amazon S3 bucket. Both the master keys and the unencrypted data should never be sent to AWS to comply with the strict compliance and regulatory requirements of the company.

Which S3 encryption technique should the Security Engineer implement?

Implement an Amazon S3 client-side encryption with a KMS key.
Implement an Amazon S3 client-side encryption with a client-side master key.
Implement an Amazon S3 server-side encryption with a KMS managed key.
Implement an Amazon S3 server-side encryption with customer provided key.
Show me the answer!
Question 2
An enterprise monitoring application collects data and generates audit logs of all operational activities of the company’s AWS Cloud infrastructure. The IT Security team requires that the application retain the logs for 5 years before the data can be deleted.

How can the Security Engineer meet the above requirement?

Use Amazon S3 Glacier to store the audit logs and apply a Vault Lock policy.
Use Amazon EBS Volumes to store the audit logs and take automated EBS snapshots every month using Amazon Data Lifecycle Manager.
Use Amazon S3 to store the audit logs and enable Multi-Factor Authentication Delete (MFA Delete) for additional protection.
Use Amazon EFS to store the audit logs and enable Network File System version 4 (NFSv4) file-locking mechanism.
Show me the answer!
Question 3
For data privacy, a healthcare company has been asked to comply with the Health Insurance Portability and Accountability Act (HIPAA) in handling static user documents. They instructed their Security Engineer to ensure that all of the data being backed up or stored on Amazon S3 are durably stored and encrypted.

Which combination of actions should the Engineer implement to meet the above requirement? (Select TWO.)

Encrypt the data locally first using your own encryption keys before sending the data to Amazon S3. Send the data over HTTPS.
Instead of using an S3 bucket, move and store the data on Amazon EBS volumes in two AZs with encryption enabled.
Instead of using an S3 bucket, migrate and securely store the data in an encrypted RDS database.
Tutorials dojo strip
Enable Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) on the S3 bucket with AES-256 encryption.
Enable Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) on the S3 bucket with AES-128 encryption.
Show me the answer!
Question 4
A multinational company is developing a sophisticated web application that requires integration with multiple third-party APIs. The company’s unique keys for each API are hardcoded inside an AWS CloudFormation template.

The security team requires that the keys be passed into the template without exposing their values in plaintext. Moreover, the keys must be encrypted at rest and in transit.

Which of the following provides the HIGHEST level of security while meeting these requirements?

Use AWS Systems Manager Parameter Store to store the API keys. Then, reference them in the AWS CloudFormation templates using !GetAtt AppKey.Value
Use AWS Systems Manager Parameter Store to store the API keys as SecureString parameters. Then, reference them in the AWS CloudFormation templates using {{resolve:ssm:AppKey}}
Utilize AWS Secrets Manager to store the API keys. Then, reference them in the AWS CloudFormation templates using {{resolve:secretsmanager:AppKey:SecretString:password}}
Use an Amazon S3 bucket to store the API keys. Then, create a custom AWS Lambda function to read the keys from the S3 bucket. Reference the keys in the AWS CloudFormation templates using a custom resource that invokes the Lambda function.
Show me the answer!
Question 5
A company is looking to store its confidential financial files in AWS, which are accessed every week. A Security Engineer was instructed to set up the storage system, which uses envelope encryption and automates key rotation. It should also provide an audit trail that shows who used the encryption key and by whom for security purposes.

Which of the following should the Engineer implement to satisfy the requirement with the LEAST amount of cost? (Select TWO.)

Store the confidential financial files in Amazon S3.
Store the confidential financial files in the Amazon S3 Glacier Deep Archive.
Enable Server-Side Encryption with Customer-Provided Keys (SSE-C).
Enable Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3).
Enable Server-Side Encryption with AWS KMS Keys (SSE-KMS).
Show me the answer!
Question 6
A company is expanding its operations and setting up new teams in different regions around the world. The company is using AWS for its development environment. There’s a strict policy that only approved software can be used when launching EC2 instances.

In addition to enforcing the policy, the company also wants to ensure that the solution is cost-effective, does not significantly increase the launch time of the EC2 instances, and is easy to manage and maintain. The company also wants to ensure that the solution is scalable and can easily accommodate the addition of new software to the approved list or the removal of software from it.

Which of the following solutions would be the most effective considering all the requirements?

Use a portfolio in the AWS Service Catalog that includes EC2 products with the right AMIs, each containing only the approved software. Ensure that developers have access only to this Service Catalog portfolio when they need to launch a product in the software development account.
Set up an Amazon EventBridge rule that triggers whenever any EC2 RunInstances API event occurs in the software development account. Specify AWS Systems Manager Run Command as a target of the rule. Configure Run Command to run a script that installs all approved software onto the instances that the developers launch.
Use AWS Systems Manager State Manager to create an association that specifies the approved software. The association will automatically install the software when an EC2 instance is launched.
Use AWS Config to monitor the EC2 instances and send alerts when unapproved software is detected. The alerts can then be used to manually remove the software.
Show me the answer!
Question 7
A company migrated the DNS records of one of its domains to Amazon Route 53 and enabled logging for public DNS queries. After a week, log data was accumulating quickly, raising concerns about high storage costs over time. The company already uses AWS Cost Anomaly Detection to monitor unexpected spending patterns. To further reduce long-term storage expenses, logs older than one month must be automatically deleted.

Which action will resolve the problem most cost-effectively?

Configure a retention policy in an Amazon CloudWatch Logs to delete logs older than 1 month.
Free AWS Courses
Change the destination of the DNS query logs to Amazon S3 Glacier Deep Archive.
Configure Amazon CloudWatch Logs to export log data to an Amazon S3 bucket. Set an S3 lifecycle policy that deletes objects older than 1 month.
Create a scheduled job using an AWS Lambda function to export logs from Amazon CloudWatch Logs to an Amazon S3 bucket. Set an S3 lifecycle policy that deletes objects older than 1 month.
Show me the answer!
Question 8
A data security company is experimenting on various security features that they can implement on their Elastic Load Balancers such as Server Order Preference, Predefined Security Policy, Perfect Forward Secrecy, and many others. The company is planning to use the Perfect Forward Secrecy feature to provide additional safeguards to their architecture against the eavesdropping of encrypted data through the use of a unique random session key. This feature also prevents the decoding of captured data, even if the secret long-term key is compromised.

Which AWS services can offer SSL/TLS cipher suites for Perfect Forward Secrecy?

Amazon EC2 and Amazon S3
AWS CloudTrail and Amazon CloudWatch
Amazon CloudFront and Elastic Load Balancers
Amazon API Gateway and AWS Lambda
Show me the answer!
Question 9
A Cloud Security Engineer is validating network controls in an AWS VPC. From an authorized corporate laptop with a public IP address of 112.237.99.166, the engineer sends an ICMP ping to an Amazon EC2 instance with a private IP address of 172.31.17.140. The ping request is sent successfully, but the reply does not reach the laptop.

To investigate, the team reviews the VPC Flow Logs for the EC2 instance and observes the following entries:

2 123456789010 eni-1235b8ca 112.237.99.166 172.31.17.140 0 0 1 4 336 1432917027 1432917142
ACCEPT OK
2 123456789010 eni-1235b8ca 172.31.17.140 112.237.99.166 0 0 1 4 336 1432917094 1432917142
REJECT OK

What is the MOST likely root cause of this issue?

The security group has an inbound rule that allows ICMP traffic, but does not have an outbound rule to explicitly allow outgoing ICMP traffic.
The network ACL permits inbound ICMP traffic but blocks outbound ICMP traffic.
The security group’s inbound rules do not allow ICMP traffic.
The Network ACL does not permit inbound ICMP traffic.
Show me the answer!
Question 10
A newly hired Security Analyst is assigned to manage the existing CloudFormation templates of the company. The Analyst opened the templates and analyzed the configured IAM policy for an S3 bucket as shown below:

<pre>
{
  “Version”: “2012-10-17”,
  “Statement”: [
    {
      “Effect”: “Allow”,
      “Action”: [
        “s3:Get*”,
        “s3:List*”
     ],
     “Resource”: “*”
  },
  {
     “Effect”: “Allow”,
     “Action”: “s3:PutObject”,
     “Resource”: “arn:aws:s3:::team-palawan/*”
   }
 ] }
</pre>

What does the following IAM policy allow? (Select THREE.)

Allows reading objects from all S3 buckets owned by the account.
Allows writing objects into the team-palawan S3 bucket.
Allows changing access rights for the team-palawan S3 bucket.
Allows reading objects in the team-palawan S3 bucket but not allowed to list the objects in the bucket.
Allows reading objects from the team-palawan S3 bucket.
Allows reading and deleting objects from the team-palawan S3 bucket.
Show me the answer!
For more practice questions like these and to further prepare you for the actual AWS Certified Security Specialty SCS-C02 exam, we recommend that you take our top-notch AWS Certified Security Specialty Practice Exams, which have been regarded as the best in the market. 

Also, check out our AWS Certified Security Specialty SCS-C02 exam study guide here.
