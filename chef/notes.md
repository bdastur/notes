# Setting up a Vagrant environment for Chef on local machine


```
   vagrant box add bento/centos-7 --provider=virtualbox
   vagrant init bento/centos-7
   vagrant up
   vagrant ssh

   # install chef development kit 4.13.3
   curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P chefdk -c stable -v 4.13.3

   # Check chef development kit is deployed successfully.
   chef --version


   # Other vagrant commands.
   vagrant ssh-config
```



# Chef Recepie

[Chef Resources](https://docs.chef.io/resources/)

## First chef recipe.

Create a new ruby file.

file: hello.rb >
```
file "/tmp/hello.txt" do
  content "Hello World!. Second version"
  owner "vagrant"
  group "vagrant"
  mode  0755
end
```
Save the file, and execute the chef client command as below:

```
   sudo chef-client --local-mode hello.rb
```

Check that a file is created `/tmp/hello.txt`, with group and owner as vagrant.
Try modifying the file content or change file ownership and rerun the chef-client command again.
Chef will bring the file back to it's original state.

## Another simple recepie:

Chef executes recepies in the order you specify top to bottom.
Actions are applied in the order left to right.

```
package 'tree' do
    action :install
end

package 'ntp'    <-- note simpliy specifying a package like this will use the default action
                     of installing the package.

file "/etc/motd" do
    content "This server is a property of Behzad Dastur.\n"
    owner 'root'
    group 'root'
end

service "ntpd" do
  action [:enable, :start]
end

```

run the chef-client again.
```
sudo chef-client --local-mode setup.rb

```

# Cookbooks [Chef Cookbooks - Docs](https://docs.chef.io/cookbooks/)

* A Chef cookbook is a fundamental unit of configuration and policy distribution.
* Cookbooks are a way for us to group our recipes into sets of configuration instructions
* Wenever are managing multiple nodes using a chef server we will use a cookbook


## Common components
- Readme
- metadata
- recipes
- testing directorie (spec + test)


## Running recepies in a cookbook

You can use chef-client to run recepies within a cookbook, using the --runlist option which takes
the form "cookbook::recipe" as below:

```
   sudo chef-client --local-mode --runlist "apache::server"
```

Running multiple recepies

```
   sudo chef-client --local-mode --runlist "workstation::setup,apache::server"
```
same behavior, a slightly different way to specify multiple recipes:

```
   sudo chef-client --local-mode --runlist "recipe[workstation::setup],recipe[apache::server]"
```

## Calling a recipe from another recipe.

```
   include_recipe method
```

Edit the worksation/recipes/default.rb and include the setup recipe.
```
> cat workstation/recipes/default.rb

include_recipe "workstation::setup"

```

Now, we can run the chef-client, notice how we dont specify any recipe and it picks up the
default recipe, which goes through the steps in the setup recipe as we have included it in our
defaults.rb recipe


```
   sudo chef-client --local-mode --runlist "recipe[workstation]"
```

can run multiple recipes in a similar way:

```
   sudo chef-client --local-mode --runlist "recipe[apache],recipe[workstation]"

```


# [Chef Ohai](https://docs.chef.io/ohai/)

* Tool that collects system configuration data.
* Ohai is run by Chef infra client at the beginning of every chef infra run to determine system
  state.
* It adds it to a node object. The node object is the representation of all the host specific
  details. We call the values on the node object, system attributes or node attributes.


Simply run:
```
   ohai
```

Will return all the node statistics in json format.

You can get specific data as well, like free swap memory, using syntax:

```
    ohai memory/swap/free
```

## Using the node object in the recipe:


```
   file "/etc/motd" do
    content "This server is a property of Behzad Dastur.
    Hostname: #{node['ipaddress']}
    Memory:   #{node['memory']['total']}
    "
    owner 'root'
    group 'root'
end
```


# Template resources

Instead of adding a file resource you can use a template.
A template allows you to define an erb template file that you can render and use in your chef recipes.

## Generating a template

```
    chef generate template workstation/ motd
```

The template file is a .erb file. You can specify ruby like syntax enclused in <% %> tags.
You can use <%= %> syntax to print any variable or expression.

An example
```
$ cat templates/motd.erb 
This server is a property of Behzad Dastur.
Hostname: <%= node['ipaddress'] %>
Memory:   <%= node['memory']['total'] %>
CPU :     <%= node['cpu']['0']['model_name'] %>
Name:     <%= @name %>

```
Here, we are referencing the node attributes as well as a name variable (last line), 
that is passed to the template.

Define a template resource:
```
  template "/etc/motd" do
  source "motd.erb"
  variables(
    :name => 'Behzad'
  )
  action :create
end

```

# Sending and receiving notifications
* Notification is a property common to all resources. 
* All resources have the ability to notify or subscribe to another resource if it's
  state changes in some way.

## Timers

*:before*
Action on the notified resource should be run before processing the resource block
in which the notification is located

*:delayed*
(Default) Specifies that a notification should be queued up, and then executed at
the very end of the chef-client run

*:immediately*
Specifies that the notification should be run immediately, per resource notified.

## Notifies
Syntax:
```
   notifies :action, "resource[name]", :timer
```

## Subscribes
Syntax:
```
   subscribes :action, "resource[name]", :timer
```

A simple example:
Here we notify the 'httpd' service to :restart, when the template resource runs. The action is
taken immediately as specified by the :timer.

```
template "/var/www/html/index.html" do
  source "index.html.erb"
  variables(
    :name => "Behzad Dastur"
  )
  action :create
  notifies :restart, 'service[httpd]', :immediately
end

service "httpd" do
  action [:enable, :start]
end

```

Alternatively, we will use subscribes for the same example to restart 'httpd' service, when the
template resource changes.

```
template "/var/www/html/index.html" do
  source "index.html.erb"
  variables(
    :name => "Behzad R. Dastur"
  )
  action :create
end

service "httpd" do
  action [:enable, :start]
  subscribes :restart, "template[/var/www/html/index.html]", :immediately
end

```

# Chef server

## Installation:

```
yum install -y rpm

wget https://packages.chef.io/files/stable/chef-server/14.3.14/el/7/chef-server-core-14.3.14-1.el7.x86_64.rpm?_ga=2.265831439.1409014844.1620690157-2090025871.1620085040
mv chef-server-core-14.3.14-1.el7.x86_64.rpm\?_ga\=2.265831439.1409014844.1620690157-2090025871.1620085040 chef-server-core-14.3.14-1.el7.x86_64.rpm
rpm -Uhv chef-server-core-14.3.14-1.el7.x86_64.rpm

sudo chef-server-ctl --help

```

## Configuration



# Installing Ruby on centos

```
sudo yum install -y git-core zlib zlib-devel gcc-c++ patch readline readline-devel \
                    libyaml-devel libffi-devel openssl-devel make bzip2 autoconf \
                    automake libtool bison curl sqlite-devel
git clone git://github.com/sstephenson/rbenv.git .rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
exec $SHELL
git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bash_profile
exec $SHELL
rbenv install -v 2.2.1
export PATH=$PATH:~/.rbenv/bin/
rbenv install -v 2.2.1
rbenv global 2.2.1
 ```





