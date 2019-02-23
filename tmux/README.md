# Tmux notes:


## Links:
[tmux plugin manager](https://github.com/tmux-plugins/tpm)
[session manager](https://github.com/tmux-python/tmuxp)



## To install plugins with tmux plugin manager:

```
# Add this line in your ~/.tmux.conf
set -g @plugin 'tmux-plugins/tmux-cpu'

# Then run:
Hit prefix + I to fetch the plugin and source it.

```

## Tmuxp session manager.
Can save sessions as yaml or json file format.

### Saving the session.
Save it under 
```
~/.tmuxp/

```

### Load a session from file.
For a session saved as: ```~/.tmuxp/4-pane-split.yaml```, you can load it as:

```
tmuxp load 4-pane-split
```

### To freeze a session to a file.
```
tmuxp freeze <session-name>
```
This will prompt you to save it to yaml/json format file.




* tmux new to start a new tmux session.
* to get out of tmux - one option is exitt
* prefix:
  * ctrl+b followed by : to get to tmux prompt.
  * ctrl+b d -> detach the session. Does not close the session. You can pickup from where you left off.
  * tmux ls --> to see active sessions.
  * tmux attach-session -t <no> --> to go the corresponding session.
  * tmux a # --> to attach to the last created ssession.
  * tmux new -s ilmtest --> create a session with a name
  * tmux a -t ilmtest --> attached to a session.
  * ctrl+b " --> split pane horizontally
  * ctrl+b % --> split pane vertically
  * Reloading tmux configuration. --> prefix + : (:source /Users/behzad.dastur/.tmux.conf)

