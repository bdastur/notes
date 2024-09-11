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



## Writing the ASL State machine file.
Amazon States Language is a JSON based structed language used to define your state
machine.

**Main Parts**

Comment (Optional): A human readable description

StartAt (Required): A string that matches (exactly) the name of one of the state
                    objects

TimeoutSeconds (Optional): Maximum number of seconds an execution of the state
                           machine can run. If it runs longer than this time, the
                           execution fails with States.Timeout Error.

Version (Optional): The versio of the Amazon States Language (Default: "1.0")

States (Required): Set of states, (comma delimited)

A sample structure of a state machine. (More details on "State" will be below)
```
{
  "Comment": "A simple comment",
  "StartAt": "FirstState",
  "TimeoutSeconds": 5,
  "States": {
    "FirstState": {
      "Type": "<Type>",
      "Next": "SecondState",
      :
    },
    "SecondState": {
      "Type": "<Type>",
      "End": true
    }
  }
}
```


### Anatomy of a State

**Fields:**

Type (Required)
The state's type.

Next
The name of the next state that is run when the current state finishes.

End
Designates the state as a terminal state if set to true. There can be any number
of terminal states per state machine.

Comment
Humna readable description (optional)

InputPath




=============================================
Input:
{
  "firstName": "Behzad",
  "lastName": "Dastur",
  "age": 46
}
-----------------------------

1. Simple.

State:
"FirstState": {
  "Type": "Pass",
  "End": true,
}
Transitions:

Enter:
{
  "input": {
    "firstName": "Behzad",
    "lastName": "Dastur",
    "age": 46
  },
  "inputDetails": {
    "truncated": false
  },
  "name": "FirstState"
}

Exit:
{
  "name": "FirstState",
  "output": {
    "firstName": "Behzad",
    "lastName": "Dastur",
    "age": 46
  },
  "outputDetails": {
    "truncated": false
  }
}

==============================================================================
2. State, this time with InputPath, filtering only for "firstName" field.:
(Use the InputPath filter to select a portion of the state input to use.)

State:
"FirstState": {
  "Type": "Pass",
  "End": true,
  "InputPath": "$.firstName" <- New config.
}

Transitions:

Enter:
{
  "input": {
    "firstName": "Behzad",
    "lastName": "Dastur"
  },
  "inputDetails": {
    "truncated": false
  },
  "name": "FirstState"
}

Exit:
{
  "name": "FirstState",
  "output": "\"Behzad\"",
  "outputDetails": {
    "truncated": false
  }
}


===============================================
3. State, this time with input path and result path defined.
(By default, a state sends its task result as output. With a ResultPath,
 you can pass the original input combined with Task result)

State:
"FirstState": {
  "Type": "Pass",
  "End": true,
  "InputPath": "$.firstName",        <-
  "ResultPath": "$.previousInput"    <- new config in addition to InputPath
}

Transitions:

Enter:
{
  "input": {
    "firstName": "Behzad",
    "lastName": "Dastur",
    "age": 46
  },
  "inputDetails": {
    "truncated": false
  },
  "name": "FirstState"
}

Exit:
{
  "name": "FirstState",
  "output": {
    "firstName": "Behzad",
    "lastName": "Dastur",
    "age": 46,
    "previousInput": "Behzad"
  },
  "outputDetails": {
    "truncated": false
  }
}
===============================================
4. Manipulating input with parameters as well as use of Intrinsic functions.
(Use the Parameters filter to build out a new JSON payload, using parts of the state input.)

State:
"FirstState": {
  "Type": "Pass",
  "End": true,
  "Parameters": { -> new config. Using Stats.Format to combine two fields from input into one.
    "fullName.$": "States.Format('{} {}', $.firstName, $.lastName)"
  }
}

Transitions:

Enter:
{
  "input": {
    "firstName": "Behzad",
    "lastName": "Dastur",
    "age": 46
  },
  "inputDetails": {
    "truncated": false
  },
  "name": "FirstState"
}

Exit:
{
  "name": "FirstState",
  "output": {
    "fullName": "Behzad Dastur"
  },
  "outputDetails": {
    "truncated": false
  }
}


===============================================


































