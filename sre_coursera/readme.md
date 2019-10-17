SRE vs DevOps

# DevOps:
- Reduce organization silos
  - share ownership with developers

- Accept failure as normal
  - SLOs and Blameless PMs

- implement gradual change
  - Canary deployments

- leverage tooling and automation
  - Eleminate manual labor. Automate this years job away

- measure everything
  - Measure the amount of toil and reliability


*class SRE implements Devops*

- Devops and SRE arent two competing methods but rather close friends designed 
  to break down organizational barriers to deliver better software faster. 


# CRE (Customer Reliability Engineering):
- SRE everyone else
- Openly communicating with customers
- Customers interface with your APIs/systems
- Help customers that are implementing applications on your system on how to
  create good SLOs.
- Break down barriers between Platform/Cloudprovider and Customer.
- Think about how to make failure a normal accepted thing.
- SLOs and error budgets are defined so people dont panic when there is a 
  down time.
- Visibility into the system.
- How platform is perforrming and platform can see how customer service level
  objectives are fairing during an outage.

## CRE thrree reliability principles

- Our first principle is that the most important feature of any system is 
  its reliability.  
  - What's the point of having a system if your customers can't use the services
    you are providing.
  - That does not mean that the system should never fail it's users. This is
    costly and often unreachable target to set.
  - A more realistic goal is that the system should meet the expectations of
    it's users and strive to maintain their trust.
- Our monitoring does not decide our reliability, our users 
  - If your users perceive your service to be unreliable, then it is not 
    meeting their expectations, no matter what your logs and metrics say.
- well-engineered software can only get you to three nines.
  - Architecting a system carefuly and following best practices for
    reliability, like running in multiple globally distributed regions,
    means that the system has the potential to achieve three nines over a
    long time horizon.
  - To achieve 4 nines it's not enough to have talented deevelopers and well
    engineered software. You also need an operations team whose primary goal
    is to sustain system reliability reactive (like well trained incident
    response) and proactive engineering (like removing bottlenecks,
    automating processes, and isolating failure domains.)
  - Reaching levels of 5 mines reliability actually requires sacrificing many
    other aspects of the system, like flexibility and release velocity.
  - Every component must be automated such that changes are rolled out
    gradually and failures are detected quickly and rolled back without
    human involvement. 
  - Each additional nine makes your system 10 times more reliable than before,
    but as a rough rule of thumb, it also costs your business 10 times more.

  - What does 3 nines or 5 nines really mean when it comes to your system
    being down? It is helpful to think about these targets in termss of
    their inverse, how much down time is permissible over a given timespan?
  - This unreliability is your error budget.
  - A 3 nine reliability will give you window of about 40 minutes over 
    a four-week period. This is just about enough time for monitoring 
    systems to notice something wrong, and for a human to investigate and
    fix the root cause if lucky.
  - A 4 nine reliability means you can have only 4 minutes of complete down
    time in the same 4 week window. This is not enought time for human
    intervention. Your system has to be able to detect and self heal
    complete outages. You will have to architect your system so that changes
    propogate in waves, and no more than a certain fraction of the system is
    exposed to a change at once. This way humans still have time to react.



## SLOs:
- Reliability of a system is it's most important feature. Taking this to
  extremes is counterproductive. 
- Targeting a specific level of reliability is key to establishing a balance
  between reliability and pressure for new features to drive user acquisition.
  We call these targets 'Service Level Objectives' or SLOs.
- The main question SLOs can help product teams answer is if reliability is a
  feature, how do you prioritize it versus other features?
- Targeting a specific level of reliability is key to establishing that
  balance.
- Setting a target for system reliability and communicatting that target
  widely allows all parts of an organization to determinte independeltly
  whether or not the service is reliable enough. 
- Acknowledging that a specific quantity of unreliability is acceptable
  provides a budget for failure that can be spent on developing and launching
  new features.  


### How SLOs help to build features faster.

- The biggest cause on unreliability in a system is change. 
- The primary goal of most development organizations is to design and build
  product features, ideally as quickly as possible.
- There is often a strong negative correlation between development velocity
  and system reeliability. 
- A missed reliability target signals when too many things users care about
  have been broken by excessible development velocity. The main question SLOs
  can help development teams answer is, when moving fast and breaking things
  how fast is too fast? Or alternatively, how to balance the risk to 
  reliability from changing a system with the need to build new features 
  for that system.
- Measuring SLO performance gives a real time indication of the reliability
  cost of new features. 
- If SLO represents the point at which you are no longer meeting the expectations
  of your users, then broadly speaking, being well within SLO is a signal that
  you can move faster without causing user pain.
- Conversely burning most or in worst cases multiples of your error budget,
  means you have to lift your foot off the accelerator.
- This allows you to estimate risk and guage the potential amount of error
  budget that each risk might consume. If you can afford to pay the reliability
  cost of a specific risk from your budget, you don't have to spend 
  engineering effort mitigating or eliminating that risk.



## How SLOs help you balance operational and project work
- How do you balance operational work: firefighting, incident response,
  repetitive maintenance or upkeep tasks and balance actualy project work
  that is so vital to ensure the service doesn't catch fire in the first
  place.
- Getting caught in this viscious cycle leads to burn out, pager fatigue,
  and demoralization.
- SLOs help operations teams answer the question of what is the right level
  of reliability for the system you support?
- Cost of unreliability is not immediately obvious. Development organizations
  prioritize building new features over improving the reliability of past
  ones.
- Monitoring and alerting systems thatt trigger on operational response are
  only loosely connected to overall experience of users, leading to
  unnecessary operational work, or worse problems that go unnoticed until
  users complain.
- If your SLOs have executive backing and teams committed to meeting them,
  they turn drawn out arguments about prioritization into data-driven
  decisions. 
- An SLO can drive short-term operational response as well as long-term
  prioritization. If your system starts burning it's error budget at an
  elevated rate over a short time horizon, that is a strong signal users are
  having a bad time and someone should investigate. On the other hand if 
  there is no obvious harm to your users, then it may be that you can ignore
  a low rate of errors and other negative operational signals and get back
  to your project work.

- For SLOs to work, all parts of the business must agree that they are an
  accurate measure of user experience and to use them as the primary driver
  for decision-making.
- Being out of SLO must have concrete, well-documented consequences that
  redirect engineerin effort within the organization towards making
  reliability improvements. 
- Creating a sense of shared ownership where developers feel they have a 
  shared responsibility to make the service reliable and the operations team
  feel that they have a responsibility to help new features reach users as
  quickly as possible is crucial.

### Three principles we use to measure desired reliability of a service.
- First, figuring out what you want to promise and to whom.
- Second, figuring out the metrics you care about that make your service
  for reliability good.
- Finally, deciding how much reliability is good enough.



## SLOs vs SLAsi

- Service Level agreements or SLAs are you agreements that you make with your
  customers about the reliability of your services.
- An SLA has to have consequences if it's violated, otherwise there is no
  point in making one.
- If your customers are paying for something and you violate an SLA, there
  needs to be consequences, such as giving your customers partial refunds
  or extra service credits.
- Now if you are only alerted of issues after they have violated your SLA,
  that could be a very costly service to run.
- Therefor it is in your best interest to catch issues before they breach 
  your SLA so that you have time to fix it. These thresholds are your SLOs,
  Service Level Objectives.
- They should always be stronger than your SLAs because customers are usually
  impacted before the SLA is actually breached. And violating SLAs require
  costly compensation.

- So in summary an SLA is an external promise that comes with consequences,
  often monetary, while an SLO is effectively an internal promise to meet
  customer expectations.

- So what do we promise our customers? Deciding how reliable you want your
  service to be depends on what your customers expect. For eg you promise that
  every HTTP request on your service returns a response in 300 milliseconds
  or less. In general the minimum it takes for a customer to not be repelled
  by your service is a good starting point.
- In this case perhaps your SLOs should have 200 milliseconds as the response
  time.
- When you breach the SLO, it suddenly becomes really important to no longer
  have any more outages. That means slowing down the rate of change to the
  system and eliminating risks. Either by doing fewer pushes, devoting
  engineering and automation efforts to reduce and eliminate areas of risk etc.

## happiness test
- A good rule of thumb to help set SLO targets is what is called the
  'happiness test'. The test states that services need target SLOs that 
  capture the performance and availability levels that if barely met would keep
  a typical customer happy.
- Simply put, if your service is performing exactly at it's target SLOs, your
  average user would be happy with that performance. If it were any less
  reliable, you would no longer be meeting their expectations and they would
  be unhappy. 
- The challenge is quantifying and measuring happiness of your customers. It's
  bad if customers are unhappy despite the fact that you appear to be meeting
  all of your SLOs. 
- Make sure you arre thinking about all the groups of customers.


## How do we measure reliability

- How do we measure the metrics that we care about for a reliable service.
- What are some characteristics for a service when we consider the service
  working or good enough.
- We refer to any metrics that measure the level of service provided as
  Service Level Indicators or SLIs.
- SLIs like request latency are quantitative measurement or metric of user
  experience.

- When selecting which metrics to choose think about the tradeoffs between
  different ways of measuring a specific metrics.
- One note about SLIs is that they are best expressed as a proportion of all
  valid events that were good. For eg: the proportion of requests served
  successfully or proportion of requests served within x milliseconds.

- How do we set SLOs for our SLIs? An SLO is a target that you get to pick,
  once you have decided on that target you measure the performance of the SLIs
  against it over a period of time (such as 28 days, last quarter, etc). 
  Depending on what our target SLO is, our SLI will tell us whether or not
  a certain point in time was good or bad.



### Error Budgets
- If you SLO says 99.9% of requests should be successful in a given quarter,
  your error budgeet allows 0.1% of requests to fail. 
- This translates to:
```
0.1% x 28 x 24 x 60 = 40.32 minutes of downtime per month.
```
This is just about enough time for your monitoring systems to surface an
issue, and for a human to investigate and fix it.


















