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









