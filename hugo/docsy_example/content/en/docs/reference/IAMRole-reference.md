---
title: IAMRole Reference
description: >
    IAMRole Scenario Class, is a generic CDK handler class that can be used to deploy many scenarios specifically for **IAM Role** creation and management.
date: 2017-01-05
---

{{% pageinfo %}}
IAMRole Scenario Class Reference.
{{% /pageinfo %}}

## Solution Configuration.

**Configuration Details:**

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| scenario   | Name of the scenario.  | Any user provided string |
| description | A brief description for the scenario.     | Any user provided string |
| stacks      | A list of stacks. Here each stack is a seperate CDK stack, that can be deployed in same or different regions or accounts.  | A list of stack configurations |

IAM Role **'Stacks'** configuration:

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| stack_name | Name of the stack. | Any user defined string|
| scenario | This is the specific scenario name. In this case 'IAMRole'| IAMRole|
| description | A brief description for the specific scenario | Any user defined string |
| options | Configurtion options for the IAMRole scenario class| As specified in table below|
| deploy_options | Deploy configurations. | Configure deploy options |

IAM Role Stack **'options'**:

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| role_name         | A unique (per account) role name| A user defined role name|
| max_session_duration | [Maximum session duration](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in seconds | A user defined value in seconds|
| assume_roles | A list of trust relationship configurations| As specified in assume role |
| allow_access | Configuration for adding permissions to IAM Role | See table below |
| deny_access | Configuration for adding deny permissions to the role | See table below |

IAM Role **'assume_roles'** configuration:

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| principal_type | Principal type: Allowed values: aws_account|aws_service | Either aws_account or aws_service |
| principals | A list of principal ARNs | principal arns |
| externalId | Optional ExternalId | External ID. See [why you should use externalID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) |

IAM Role **'allow access'** configuration:

use the 'allow_access' configuration to setup Allow permissions for the IAM Role

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| service | Service name. Eg: s3, iam, ec2 | Service Name |
| access_type | Access type should be one of Read, Write or Full | Read/Write/Full |
| resource_arns | Resource ARNs | Resource ARNs |

IAM Role **'deny_access'** configuration:

use the 'deny_access' configuration to setup Deny permissions for the IAM Role

| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| service | Service name. Eg: s3, iam, ec2 | Service Name |
| access_type | Access type should be one of Read, Write or Full | Read/Write/Full |
| resource_arns | Resource ARNs | Resource ARNs |


**deploy_options** configuration:
| Field             |  Details           | Allowed values |
|-------------------|-------------------|-----------------|
| profile | User specified aws profile, as configured in ~/.aws/credentials | AWS Profile |
| region | AWS region. eg us-east-1 | AWS Region |


**Json Format**

```
{
    "scenario": "<Name of the Scenario>",
    "description": "<A brief description>",
    "stacks": [
        {
            "stack_name": "<Name of the stack>",
            "scenario": "IAMRole",
            "description": "<Description for the stack>",
            "options": {
                "role_name": "<Role name to create>",
                "max_session_duration": <Max session duration in seconds(900 - 43200)>,
                "assume_roles": [
                    {
                        "principal_type": "<Principal type: allowed values: aws_account|aws_service>",
                        "principals": [<List of Principal ARNs>],
                        "externalId": "<Optional: ExternalID for aws_account type>"
                    }
                ],
                "allow_access": [
                    {
                        "service": "<Service name. Eg: logs|lambda|s3>",
                        "access_type": "<Access type: Read|Write|Full>",
                        "resource_arns": [<resource ARN>,..]
                    }
                ],
                "deny_access": [
                    {
                        "service": "<Service name>",
                        "access_type": "<Access type: Read|Write|Full>",
                        "resource_arns": [<resource ARN>,..]
                    }
                ]
            },
            "deploy_options": {
                "profile": "<Profile name, as configured in ~/.aws/credentials>",
                "region": "<region name>"
            }
        }
    ]
}

```

Text can be **bold**, _italic_, or ~~strikethrough~~. [Links](https://gohugo.io) should be blue with no underlines (unless hovered over).

There should be whitespace between paragraphs. Vape migas chillwave sriracha poutine try-hard distillery. Tattooed shabby chic small batch, pabst art party heirloom letterpress air plant pop-up. Sustainable chia skateboard art party banjo cardigan normcore affogato vexillologist quinoa meggings man bun master cleanse shoreditch readymade. Yuccie prism four dollar toast tbh cardigan iPhone, tumblr listicle live-edge VHS. Pug lyft normcore hot chicken biodiesel, actually keffiyeh thundercats photo booth pour-over twee fam food truck microdosing banh mi. Vice activated charcoal raclette unicorn live-edge post-ironic. Heirloom vexillologist coloring book, beard deep v letterpress echo park humblebrag tilde.

90's four loko seitan photo booth gochujang freegan tumeric listicle fam ugh humblebrag. Bespoke leggings gastropub, biodiesel brunch pug fashion axe meh swag art party neutra deep v chia. Enamel pin fanny pack knausgaard tofu, artisan cronut hammock meditation occupy master cleanse chartreuse lumbersexual. Kombucha kogi viral truffaut synth distillery single-origin coffee ugh slow-carb marfa selfies. Pitchfork schlitz semiotics fanny pack, ugh artisan vegan vaporware hexagon. Polaroid fixie post-ironic venmo wolf ramps **kale chips**.

> There should be no margin above this first sentence.
>
> Blockquotes should be a lighter gray with a border along the left side in the secondary color.
>
> There should be no margin below this final sentence.

## First Header 2

This is a normal paragraph following a header. Knausgaard kale chips snackwave microdosing cronut copper mug swag synth bitters letterpress glossier **craft beer**. Mumblecore bushwick authentic gochujang vegan chambray meditation jean shorts irony. Viral farm-to-table kale chips, pork belly palo santo distillery activated charcoal aesthetic jianbing air plant woke lomo VHS organic. Tattooed locavore succulents heirloom, small batch sriracha echo park DIY af. Shaman you probably haven't heard of them copper mug, crucifix green juice vape *single-origin coffee* brunch actually. Mustache etsy vexillologist raclette authentic fam. Tousled beard humblebrag asymmetrical. I love turkey, I love my job, I love my friends, I love Chardonnay!

Deae legum paulatimque terra, non vos mutata tacet: dic. Vocant docuique me plumas fila quin afuerunt copia haec o neque.

On big screens, paragraphs and headings should not take up the full container width, but we want tables, code blocks and similar to take the full width.

Scenester tumeric pickled, authentic crucifix post-ironic fam freegan VHS pork belly 8-bit yuccie PBR&B. **I love this life we live in**.


## Second Header 2

> This is a blockquote following a header. Bacon ipsum dolor sit amet t-bone doner shank drumstick, pork belly porchetta chuck sausage brisket ham hock rump pig. Chuck kielbasa leberkas, pork bresaola ham hock filet mignon cow shoulder short ribs biltong.

### Header 3

```
This is a code block following a header.
```

Next level leggings before they sold out, PBR&B church-key shaman echo park. Kale chips occupy godard whatever pop-up freegan pork belly selfies. Gastropub Belinda subway tile woke post-ironic seitan. Shabby chic man bun semiotics vape, chia messenger bag plaid cardigan.

#### Header 4

* This is an unordered list following a header.
* This is an unordered list following a header.
* This is an unordered list following a header.

##### Header 5

1. This is an ordered list following a header.
2. This is an ordered list following a header.
3. This is an ordered list following a header.

###### Header 6

| What      | Follows         |
|-----------|-----------------|
| A table   | A header        |
| A table   | A header        |
| A table   | A header        |

----------------

There's a horizontal rule above and below this.

----------------

Here is an unordered list:

* Liverpool F.C.
* Chelsea F.C.
* Manchester United F.C.

And an ordered list:

1. Michael Brecker
2. Seamus Blake
3. Branford Marsalis

And an unordered task list:

- [x] Create a Hugo theme
- [x] Add task lists to it
- [ ] Take a vacation

And a "mixed" task list:

- [ ] Pack bags
- ?
- [ ] Travel!

And a nested list:

* Jackson 5
  * Michael
  * Tito
  * Jackie
  * Marlon
  * Jermaine
* TMNT
  * Leonardo
  * Michelangelo
  * Donatello
  * Raphael

Definition lists can be used with Markdown syntax. Definition headers are bold.

Name
: Godzilla

Born
: 1952

Birthplace
: Japan

Color
: Green


----------------

Tables should have bold headings and alternating shaded rows.

| Artist            | Album           | Year |
|-------------------|-----------------|------|
| Michael Jackson   | Thriller        | 1982 |
| Prince            | Purple Rain     | 1984 |
| Beastie Boys      | License to Ill  | 1986 |

If a table is too wide, it should scroll horizontally.

| Artist            | Album           | Year | Label       | Awards   | Songs     |
|-------------------|-----------------|------|-------------|----------|-----------|
| Michael Jackson   | Thriller        | 1982 | Epic Records | Grammy Award for Album of the Year, American Music Award for Favorite Pop/Rock Album, American Music Award for Favorite Soul/R&B Album, Brit Award for Best Selling Album, Grammy Award for Best Engineered Album, Non-Classical | Wanna Be Startin' Somethin', Baby Be Mine, The Girl Is Mine, Thriller, Beat It, Billie Jean, Human Nature, P.Y.T. (Pretty Young Thing), The Lady in My Life |
| Prince            | Purple Rain     | 1984 | Warner Brothers Records | Grammy Award for Best Score Soundtrack for Visual Media, American Music Award for Favorite Pop/Rock Album, American Music Award for Favorite Soul/R&B Album, Brit Award for Best Soundtrack/Cast Recording, Grammy Award for Best Rock Performance by a Duo or Group with Vocal | Let's Go Crazy, Take Me With U, The Beautiful Ones, Computer Blue, Darling Nikki, When Doves Cry, I Would Die 4 U, Baby I'm a Star, Purple Rain |
| Beastie Boys      | License to Ill  | 1986 | Mercury Records | noawardsbutthistablecelliswide | Rhymin & Stealin, The New Style, She's Crafty, Posse in Effect, Slow Ride, Girls, (You Gotta) Fight for Your Right, No Sleep Till Brooklyn, Paul Revere, Hold It Now, Hit It, Brass Monkey, Slow and Low, Time to Get Ill |

----------------

Code snippets like `var foo = "bar";` can be shown inline.

Also, `this should vertically align` ~~`with this`~~ ~~and this~~.

Code can also be shown in a block element.

```
foo := "bar";
bar := "foo";
```

Code can also use syntax highlighting.

```go
func main() {
  input := `var foo = "bar";`

  lexer := lexers.Get("javascript")
  iterator, _ := lexer.Tokenise(nil, input)
  style := styles.Get("github")
  formatter := html.New(html.WithLineNumbers())

  var buff bytes.Buffer
  formatter.Format(&buff, style, iterator)

  fmt.Println(buff.String())
}
```

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

Inline code inside table cells should still be distinguishable.

| Language    | Code               |
|-------------|--------------------|
| Javascript  | `var foo = "bar";` |
| Ruby        | `foo = "bar"{`      |

----------------

Small images should be shown at their actual size.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Picea_abies_shoot_with_buds%2C_Sogndal%2C_Norway.jpg/240px-Picea_abies_shoot_with_buds%2C_Sogndal%2C_Norway.jpg)

Large images should always scale down and fit in the content container.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Picea_abies_shoot_with_buds%2C_Sogndal%2C_Norway.jpg/1024px-Picea_abies_shoot_with_buds%2C_Sogndal%2C_Norway.jpg)

_The photo above of the Spruce Picea abies shoot with foliage buds: Bjørn Erik Pedersen, CC-BY-SA._


## Components

### Alerts

{{< alert >}}This is an alert.{{< /alert >}}
{{< alert title="Note" >}}This is an alert with a title.{{< /alert >}}
{{% alert title="Note" %}}This is an alert with a title and **Markdown**.{{% /alert %}}
{{< alert color="success" >}}This is a successful alert.{{< /alert >}}
{{< alert color="warning" >}}This is a warning.{{< /alert >}}
{{< alert color="warning" title="Warning" >}}This is a warning with a title.{{< /alert >}}


## Another Heading
