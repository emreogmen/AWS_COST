Step-1: Configure AWS Access via CLI

AWS_COST % aws configure

AWS Access Key ID [****************KIXO]:
AWS Secret Access Key [****************p0WC]:
Default region name [None]:
Default output format [None]:

Step-2: Install the Required packages

pip install -r Requirements.txt

Step-3: Run the script

python3 nattest.py

AWS_COST % python3 nattest.py
             Date              UsageType Cost (USD) UsageQuantity
0      2024-09-01  USE2-NatGateway-Bytes   0.035585      0.883553
1      2024-09-01  USE2-NatGateway-Hours     0.4833          12.0
2      2024-10-01  USE2-NatGateway-Bytes   0.347563      8.629751
3      2024-10-01  USE2-NatGateway-Hours    3.78585          94.0
4      2024-11-01       NatGateway-Bytes        0.0      0.000008
5      2024-11-01       NatGateway-Hours    4.75245         118.0
6      2024-11-01  USE2-NatGateway-Bytes   0.048017      1.192239
7      2024-11-01  USE2-NatGateway-Hours    5.07465         126.0
8      2024-11-01  USW2-NatGateway-Bytes   0.000001      0.000013
9      2024-11-01  USW2-NatGateway-Hours    4.75245         118.0
10     2024-12-01       NatGateway-Bytes   0.000014      0.000354
11     2024-12-01       NatGateway-Hours   0.040275           1.0
Total       Total                   None   19.32016     479.70592

Step-4: Reach out to Aviatrix to start benefiting from Cost Savings as well as the Visibility and Security embedded in CSP!

