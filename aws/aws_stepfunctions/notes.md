# Step Functions

## Useful Links:
* [AWS Step Functions Developer guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
* [Amazon States Language specification](https://states-language.net/spec.html)
* [Error handling in Step functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
* [Step functions service quotas](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html)


## Service integration patterns:

* Request Response (default)
Call a service, and let step functions progress to the next state after it gets an 
HTTP response.

* Run a job (sync)
Call a service, and have step functions wait for a job to complete.

* Wait for a callback with a task token (.waitForTaskToken)
Call a service with a task token, and have step functions wait until the task token
returns with a callback.

## Concepts.

**Workflow**
A sequence of steps that often reflect a business process.

**States**
Individual steps in your state machine that can make decisions based on their input,
perform actions and pass output to other states.

**Workflow studio**
Visual workflow designer that helps you to prototype and build workflows faster.

**State machine**
A workflow designed using JSON text representing individual states or steps in
the workflow along with fields such as StartAt, TimeoutSeconds and Version.

**Amazon States Language**
A JSON based structured language used to define your state machines.

**Input and output configurations**
States in a workflow receive JSON data as input and usually pass JSON data as output
to the next state. Step functions provide filters to control the data flow
between states.

**Service Integration**
You can call AWS service API actions from your workflow.

**Service Integration type**
* AWS SDK Integration: Standard way to call any of over two hunder AWS services
  and over nine thousand API actions from your state machine.
* Optimized Integrations: Custom integrations that streamline calling and exchanging
  data with certain services.

**Service Integration pattern**
When calling an AWS service you can use one of the following service integration
patterns.
 * Request Response
 * Run a job (.sync)
 * Wait for a callback with a task token (.waitForTaskToken)


## Activities
Step function activities, can setup a a task in your state machine where the actual
work is performed by a worker running outside of the step functions. Eg, you could
have a worker program running on Amazon EC2 or ECS service or even mobile devices.







