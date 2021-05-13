#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3


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



def main():
    ce = CostExplorer(profile='dev', region='us-east-1')
    ce.get_cost_usage_data()

if __name__ == "__main__":
    main()
