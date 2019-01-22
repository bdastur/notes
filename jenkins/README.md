# Notes on Jenkins.
----

## Useful links:
[Jenkins plugins](https://plugins.jenkins.io/ansible)
[Official Jenkins Docker repo](https://github.com/jenkinsci/docker)


## Allowing your CI container to start other docker agents/containers.
* If you want your CI container, to be able to start containers, then a simple way is
  to expose /var/run/docker.sock to your CI container using -v flag.
  ``` --volume /var/run/docker.sock:/var/run/docker.sock```.
  You will also need to install the docker cli in your CI container.

* Now your CI container will be ablee to start containers. Except that instead of
  starting child containers, it will start sibling containers.


## To dump all credentials stored in jenkins, go to ```Script console``` under
   ```Manage Jenkins```, and execute this script:

```
import jenkins.model.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey
import org.jenkinsci.plugins.plaincredentials.StringCredentials

def showRow = { credentialType, secretId, username = null, password = null, description = null ->
  println("${credentialType} : ".padLeft(20) + secretId?.padRight(38)+" | " +username?.padRight(20)+" | " +password?.padRight(40) + " | " +description)
}

// set Credentials domain name (null means is it global)
domainName = null

credentialsStore = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0]?.getStore()
domain = new Domain(domainName, null, Collections.<DomainSpecification>emptyList())

credentialsStore?.getCredentials(domain).each{
  if(it instanceof UsernamePasswordCredentialsImpl)
    showRow("user/password", it.id, it.username, it.password?.getPlainText(),it.description)
  else if(it instanceof BasicSSHUserPrivateKey)
    showRow("ssh priv key", it.id, it.passphrase?.getPlainText(), it.privateKeySource?.getPrivateKey(), it.description )
  else if(it instanceof StringCredentials)
    showRow("secret text", it.id, it.secret?.getPlainText(), it.description, '' )
  else
    showRow("something else", it.id)
}

return
```

  
