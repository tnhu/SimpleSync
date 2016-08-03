*This project has a new maintainer [hydralien](https://github.com/hydralien/SimpleSync). Issues and PRs, please go to [hydralien's repository](https://github.com/hydralien/SimpleSync)*

# SimpleSync

Simple Sublime Text 2/3 plugin for SSH and local syncing.

## Before you start

- Currently support MacOS and Linux.
- SSH synchronization is done via scp, your system must have SSH public-key authentication enabled.

## Installation

### Manually

* Sublime Text 2
Clone this project into your ST2 Packages folder, for example:

``` bash
cd "/Users/tnhu/Library/Application Support/Sublime Text 2/Packages"
git clone https://github.com/tnhu/SimpleSync.git
```

* Sublime Text 3

``` bash
cd "/Users/tnhu/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/tnhu/SimpleSync.git
```

### Using ST2/3 Package Control

Search for SimpleSync in ST2/3 Package Control and install it.

## Settings

When you finish installing SimpleSync, its settings can be found in Preferences > Package Settings > SimpleSync > Settings - Default.
And you should put your custom settings in Preferences > Package Settings > SimpleSync > Settings - User.

Sample settings:

``` javascript
{
  "sync": [{
    "type"     : "ssh",
    "host"     : "tnhu-ld",
    "port"     : "22",
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

Files are saved to remote server automatically when you save them locally. In case of "local" syncing, they are copied to "remote" folder which is on the same machine.

## Contributors

* [tnhu](https://github.com/tnhu)
* [gfreezy](https://github.com/gfreezy)

## License

Copyright (c) 2009-2012 Tan Nhu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
