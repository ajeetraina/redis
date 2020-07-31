<pre>
Last login: Fri Jul 31 11:25:36 on ttys000
ajeetraina@Ajeets-MacBook-Pro ~ % redis-cli 
127.0.0.1:6379> exit
ajeetraina@Ajeets-MacBook-Pro ~ % mkdir notifications


ajeetraina@Ajeets-MacBook-Pro ~ % cd notifications 
ajeetraina@Ajeets-MacBook-Pro notifications % mkdir notif-server

ajeetraina@Ajeets-MacBook-Pro notifications % cd notif-server 
ajeetraina@Ajeets-MacBook-Pro notif-server % npm init -y

zsh: command not found: npm
ajeetraina@Ajeets-MacBook-Pro notif-server % brew install npm
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).
==> Updated Formulae
Updated 24 formulae.

==> Downloading https://homebrew.bintray.com/bottles/icu4c-67.1.catalina.bottle.
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/2d1e91b5127f66e794179
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/node-14.7.0.catalina.bottle
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/9145dbfc69cfb951ca8f8
######################################################################## 100.0%
==> Installing dependencies for node: icu4c
==> Installing node dependency: icu4c
==> Pouring icu4c-67.1.catalina.bottle.tar.gz
==> Caveats
icu4c is keg-only, which means it was not symlinked into /usr/local,
because macOS provides libicucore.dylib (but nothing else).

If you need to have icu4c first in your PATH run:
  echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

For compilers to find icu4c you may need to set:
  export LDFLAGS="-L/usr/local/opt/icu4c/lib"
  export CPPFLAGS="-I/usr/local/opt/icu4c/include"

==> Summary
🍺  /usr/local/Cellar/icu4c/67.1: 258 files, 71.2MB
==> Installing node
==> Pouring node-14.7.0.catalina.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/node/14.7.0: 4,670 files, 61.8MB
==> Caveats
==> icu4c
icu4c is keg-only, which means it was not symlinked into /usr/local,
because macOS provides libicucore.dylib (but nothing else).

If you need to have icu4c first in your PATH run:
  echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

For compilers to find icu4c you may need to set:
  export LDFLAGS="-L/usr/local/opt/icu4c/lib"
  export CPPFLAGS="-I/usr/local/opt/icu4c/include"

==> node
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
ajeetraina@Ajeets-MacBook-Pro notif-server % npm init -y     

Wrote to /Users/ajeetraina/notifications/notif-server/package.json:

{
  "name": "notif-server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}


</pre>
