import boto3
import pandas as pd
from datetime import datetime, timedelta

# Initialize the AWS Cost Explorer client
ce_client = boto3.client('ce')

# Fetch NAT Gateway costs from AWS Cost Explorer
def fetch_nat_gateway_costs(start_date, end_date):
    response = ce_client.get_cost_and_usage(
        TimePeriod={'Start': start_date, 'End': end_date},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost', 'UsageQuantity'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'USAGE_TYPE'}],
    )
    data = [
        {
            'Date': result['TimePeriod']['Start'],
            'UsageType': group['Keys'][0],
            'Cost (USD)': float(group['Metrics']['UnblendedCost']['Amount']),
            'UsageQuantity': float(group['Metrics']['UsageQuantity']['Amount']),
        }
        for result in response['ResultsByTime']
        for group in result['Groups']
        if "NatGateway" in group['Keys'][0]
    ]
    return pd.DataFrame(data)

# Main script logic
if __name__ == "__main__":
    # Calculate start and end dates dynamically
    today = datetime.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=365)).strftime("%Y-%m-%d")

    # Fetch and process NAT Gateway costs
    df = fetch_nat_gateway_costs(start_date, end_date)
    if not df.empty:
        totals = df[['Cost (USD)', 'UsageQuantity']].sum(numeric_only=True)
        df.loc['Total'] = {
            'Date': 'Total',
            'UsageType': None,
            'Cost (USD)': f"{totals['Cost (USD)']:.5f}",
            'UsageQuantity': f"{totals['UsageQuantity']:.5f}",             
        }
    print(df)
    df.to_csv("nat_gateway_costs.csv", index=False)

print()
print("Reach out to Aviatrix to start benefiting from Nat Gateway Cost Savings as well as the enhanced visibility and security!") 
print()
print("www.aviatrix.com")
print()
