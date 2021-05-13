#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import Filter
import boto3
import pprint

# Granularity: DAILY | MONTHLY | HOURLY
# Metrics: AmortizedCost , BlendedCost , NetAmortizedCost, NetUnblendedCost,
#          NormalizedUsageAmount , UnblendedCost , and UsageQuantity
#
# GroupBy: AZ , INSTANCE_TYPE , LEGAL_ENTITY_NAME , LINKED_ACCOUNT , OPERATION ,
#               PLATFORM , PURCHASE_TYPE , SERVICE , TAGS , TENANCY , RECORD_TYPE,
#               and USAGE_TYPE .
#
# Dimension: 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|
#            'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|
#            'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|
#            'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|
#            'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|
#            'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|
#            'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|
#            'PAYMENT_OPTION'|'AGREEMENT_END_DATE_TIME_AFTER'|
#            'AGREEMENT_END_DATE_TIME_BEFORE',


class CostExplorer():
    def __init__(self,
                 profile=None, region=None) -> None:

        self.session = boto3.Session(
            profile_name=profile, region_name=region)

        self.client = self.session.client('ce')


    def get_cost_usage_data(self):
        """
        Get Usage and Cost
        """
        data = self.client.get_cost_and_usage(
            TimePeriod={'Start': '2021-05-01', 'End': '2021-05-07'},
            Granularity='DAILY', Metrics=['AmortizedCost'])

        print(data)


    def get_cost_usage_data_2(self):
        timePeriod = {
            'Start': '2021-05-01',
            'End': '2021-05-08'
        }

        filter = {
            "And": [
                {
                    "Dimensions": {
                        "Key": "SERVICE",
                        "Values": ["Amazon Elastic Compute Cloud - Compute"]
                    }
                },
                {
                    "Dimensions": {
                        "Key": "AZ",
                        "Values": ["us-east-1a", "us-east-1b", "us-east-1c"]
                    }
                }
            ]
        }
        groupBy = [
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            },
            {
                'Type': 'DIMENSION',
                'Key': 'USAGE_TYPE'
            }
        ]
        data = self.client.get_cost_and_usage(
            TimePeriod=timePeriod,
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            Filter=filter,
            GroupBy=  groupBy
        )
        pp = pprint.PrettyPrinter()
        pp.pprint(data)





def main():
    ce = CostExplorer(profile='dev', region='us-east-1')
    ce.get_cost_usage_data()
    print("--------")
    ce.get_cost_usage_data_2()

if __name__ == "__main__":
    main()
