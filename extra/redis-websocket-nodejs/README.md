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

ajeetraina@Ajeets-MacBook-Pro notif-server % npm install ws redis

npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN notif-server@1.0.0 No description
npm WARN notif-server@1.0.0 No repository field.

+ ws@7.3.1
+ redis@3.0.2
added 6 packages from 8 contributors and audited 6 packages in 4.385s

1 package is looking for funding
  run `npm fund` for details

found 0 vulnerabilities

ajeetraina@Ajeets-MacBook-Pro notif-server %

npm install -g nodemon 
/usr/local/bin/nodemon -> /usr/local/lib/node_modules/nodemon/bin/nodemon.js

> nodemon@2.0.4 postinstall /usr/local/lib/node_modules/nodemon
> node bin/postinstall || exit 0

+ nodemon@2.0.4
added 121 packages from 58 contributors in 17.286s
ajeetraina@Ajeets-MacBook-Pro notif-server % nodemon                     
[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node index.js`
internal/modules/cjs/loader.js:1088
  throw err;
  ^

Error: Cannot find module '/Users/ajeetraina/notifications/notif-server/index.js'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:1085:15)
    at Function.Module._load (internal/modules/cjs/loader.js:928:27)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
    at internal/main/run_main_module.js:17:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
}
[nodemon] app crashed - waiting for file changes before starting...
^C%                                                                             ajeetraina@Ajeets-MacBook-Pro notif-server % nodemon server.js           

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node server.js`
WebSocket server started at ws://locahost:3000

npm install -g @vue/cli



> vue create webclient

> cd web-client

 cd notifications 
ajeetraina@Ajeets-MacBook-Pro notifications % s
zsh: command not found: s
ajeetraina@Ajeets-MacBook-Pro notifications % ls
notif-server
ajeetraina@Ajeets-MacBook-Pro notifications % npm install -g @vue/cli
npm WARN deprecated @hapi/joi@15.1.1: joi is leaving the @hapi organization and moving back to 'joi' (https://github.com/sideway/joi/issues/2411)
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm WARN deprecated @hapi/hoek@8.5.1: This version has been deprecated and is no longer supported or maintained
npm WARN deprecated @hapi/topo@3.1.6: This version has been deprecated and is no longer supported or maintained
npm WARN deprecated @hapi/bourne@1.3.2: This version has been deprecated and is no longer supported or maintained
npm WARN deprecated @hapi/address@2.1.4: This version has been deprecated and is no longer supported or maintained
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
npm WARN deprecated chokidar@2.1.8: Chokidar 2 will break on node v14+. Upgrade to chokidar 3 with 15x less dependencies.
npm WARN deprecated fsevents@1.2.13: fsevents 1 will break on node v14+ and could be using insecure binaries. Upgrade to fsevents 2.
/usr/local/bin/vue -> /usr/local/lib/node_modules/@vue/cli/bin/vue.js

> fsevents@1.2.13 install /usr/local/lib/node_modules/@vue/cli/node_modules/fsevents
> node install.js

  SOLINK_MODULE(target) Release/.node
  CXX(target) Release/obj.target/fse/fsevents.o
  SOLINK_MODULE(target) Release/fse.node

> core-js@3.6.5 postinstall /usr/local/lib/node_modules/@vue/cli/node_modules/core-js
> node -e "try{require('./postinstall')}catch(e){}"

Thank you for using core-js ( https://github.com/zloirock/core-js ) for polyfilling JavaScript standard library!

The project needs your help! Please consider supporting of core-js on Open Collective or Patreon: 
> https://opencollective.com/core-js 
> https://www.patreon.com/zloirock 

Also, the author of core-js ( https://github.com/zloirock ) is looking for a good job -)


> @apollo/protobufjs@1.0.4 postinstall /usr/local/lib/node_modules/@vue/cli/node_modules/@apollo/protobufjs
> node scripts/postinstall


> nodemon@1.19.4 postinstall /usr/local/lib/node_modules/@vue/cli/node_modules/nodemon
> node bin/postinstall || exit 0


> ejs@2.7.4 postinstall /usr/local/lib/node_modules/@vue/cli/node_modules/ejs
> node ./postinstall.js

Thank you for installing EJS: built with the Jake JavaScript build tool (https://jakejs.com/)

+ @vue/cli@4.4.6
added 1240 packages from 677 contributors in 433.65s
ajeetraina@Ajeets-MacBook-Pro notifications % vue create webclient


Vue CLI v4.4.6
? Please pick a preset: default (babel, eslint)


Vue CLI v4.4.6
✨  Creating project in /Users/ajeetraina/notifications/webclient.
🗃  Initializing git repository...
⚙️  Installing CLI plugins. This might take a while...


> fsevents@1.2.13 install /Users/ajeetraina/notifications/webclient/node_modules/watchpack-chokidar2/node_modules/fsevents
> node install.js

  SOLINK_MODULE(target) Release/.node
  CXX(target) Release/obj.target/fse/fsevents.o
  SOLINK_MODULE(target) Release/fse.node

> fsevents@1.2.13 install /Users/ajeetraina/notifications/webclient/node_modules/webpack-dev-server/node_modules/fsevents
> node install.js

  SOLINK_MODULE(target) Release/.node
  CXX(target) Release/obj.target/fse/fsevents.o
  SOLINK_MODULE(target) Release/fse.node

> yorkie@2.0.0 install /Users/ajeetraina/notifications/webclient/node_modules/yorkie
> node bin/install.js

setting up Git hooks
done


> core-js@3.6.5 postinstall /Users/ajeetraina/notifications/webclient/node_modules/core-js
> node -e "try{require('./postinstall')}catch(e){}"


> ejs@2.7.4 postinstall /Users/ajeetraina/notifications/webclient/node_modules/ejs
> node ./postinstall.js

added 1207 packages from 856 contributors and audited 1207 packages in 84.768s

46 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

🚀  Invoking generators...
📦  Installing additional dependencies...

added 53 packages from 36 contributors and audited 1260 packages in 10.99s

50 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

⚓  Running completion hooks...

📄  Generating README.md...

🎉  Successfully created project webclient.
👉  Get started with the following commands:

 $ cd webclient
 $ npm run serve
 
 DONE  Compiled successfully in 2585ms                                1:01:01 PM


  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://192.168.1.4:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.





Vue CLI v4.4.6
? Please pick a preset: (Use arrow keys)
❯ default (babel, eslint) 
  Manually select features 
  
  
</pre>
