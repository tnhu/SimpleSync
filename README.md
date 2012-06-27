## SimpleSync

Simple Sublime Text 2 plugin for SSH and local syncing.

### Before you start

- Currently support MacOS and Linux.
- SSH synchronization is done via scp, your system must have SSH public-key authentication enabled.

### Settings

When you finish installing SimpleSync, its settings can be found in Preferences > Package Settings > SimpleSync Settings

Sample settings:

``` javascript
{
  "sync": [{
    "type"     : "ssh",
    "host"     : "tnhu-ld",
    "username" : "tnhu",
    "local"    : "/Users/tnhu/workspace/trunk",
    "remote"   : "/home/tnhu/workspace/trunk"
  }, {
    "type"     : "local",
    "local"    : "/Users/tnhu/Library/Application Support/Sublime Text 2/Packages/SimpleSync",
    "remote"   : "/Users/tnhu/Dropbox/projects/SimpleSync"
  }]
}
```

Files are saved to remote server when you save them locally. In case of "local", they are copied to "remote" folder which is on the same machine.