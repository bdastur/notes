# Considerations/Best practices for managing reserved instances

Notes based on AWS docs.


## When to purchase RIs
The below two metrics can help you determine when to purchase RIs.

### Effective Rate
The actual rate you pay to run your EC2 instance.

formula:

```math
effective rate = upfront payment (full/partial) + recurring charges
```
Example:

|| Type || On-demand||No Upfront||Partial Upfront||All Upfront||
|Upfront payment to Amazon|	$0.00|	$0.00	$443.00	$751.00
|Recurring costs running at 100% for term|	$1226.40|	$876.00|	$324.12|	$0.00|
|Total effective cost (monthly)|	$1226.40|	$876.00|	$767.12|	$751.00
|Savings over on-demand|	n/a	|29%|	37%	|39%|


### PAYBACK PERIOD
Think of it as buying solar panels. How long before you break even on the
original cost.

So in this case the time/no of months that a RI must operate at 100% usage in order for it to be less expensive that an on-demand instance of the same instance type. In other words it is the point at which you can shut down a RI and still have benefited from the purchase of it.

The payback period is applicable to partial upfront and all upfront options. The payback period is not applicable to no upfront payment option as there is no initial investment.

Payback perioud varies by instance type, but on average it is 6 months for a 1-year term and 9 months for a 3-year term.


## Analyze Needs by Instance Group
**STEP 1: GROUP LIKE INSTANCES**
To simplify the decision of making RI purchase group instances by any of the common perspectives - functions, environments and applications.

Avoid grouping instances of different platforms (eg: Linux or Windows), as AWS prices
images of platforms differently.


**STEP 2: EVALUATE COST BY GROUP**
Start by asking the following questions:
1. What percentage of the group do you expect will be running 1 year, 3 years from now?
2. Will the instances stay within the current region?
3. How likely the instance type family for the instances in the group will change.


**STEP 3: MAKE RESERVATION DECISIONS BY GROUP**
Considering the above factors if you can with reasonable confidence know that the
instances in a group will be running in a given region, without chaning the instance
family for atleast 7 months (which is the average payback period for a RI), that group
is then a candidate for RI purchase.


**Note:**
- Be careful of making RI purchases for legacy instance types. They typically cost
  more and have less performance than newer instancee types. They would also be difficult to sell on the AWS marketplace.


**STEP 4: PICK HIGHEST VALUE TARGETS**
Start by picking the group that will give you the most cost savings in RI purchase.

