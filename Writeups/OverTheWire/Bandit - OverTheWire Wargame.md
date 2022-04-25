# Level 0
For the zero level, we will go over how to connect to the wargame server through the *ssh* utility. It is indicated that this particular SSH server lives on port 2220. We will find similar instructions giving us the **Level Goal** on the webpage;

>*The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the Level 1 to find out how to beat Level 1.*
>
>*The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.*

We follow the instructions given by inputting our *ssh* connection command into our terminal and, once inside and connected, it displays a welcome message.

```shell
$ ssh -l bandit0 -p 2220 bandit.labs.overthewire.org

Linux bandit.otw.local 5.4.8 x86_64 GNU/Linux

      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to Steven or morla on
irc.overthewire.org.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ and /proc/ is disabled
  so that users can not snoop on eachother. Files and directories with
  easily guessable or short names will be periodically deleted!

  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few usefull tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /usr/local/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /usr/local/pwndbg/
    * peda (https://github.com/longld/peda.git) in /usr/local/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /usr/local/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)
    * checksec.sh (http://www.trapkit.de/tools/checksec.html) in /usr/local/bin/checksec.sh

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us through IRC on
  irc.overthewire.org #wargames.

  Enjoy your stay!
```

I printed the current working directory with *pwd* and then listed all files in the directory, including hidden ones with *ls -alt*. I found an interesting **readme** file, which I saw into with *cat* to get the next levels' password.

```shell
$ pwd
/home/bandit0
$ ls -alt
total 24
drwxr-xr-x 41 root    root    4096 May  7  2020 ..
drwxr-xr-x  2 root    root    4096 May  7  2020 .
-rw-r-----  1 bandit1 bandit0   33 May  7  2020 readme
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root     675 May 15  2017 .profile
$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

Since I cleared this level, next level credentials are **bandit1** instead of bandit0 when ssh-ing into the server.

> Level 1 password = boJ9jbbUNNfktd78OOpsqOltutMc3MY1
# Level 1
> *The password for the next level is stored in a file called **-** located in the home directory.*

Logged in, immediate *pwd* and *ls -alt*. I inmediately noticed this file named '-'.

```shell
$ pwd
/home/bandit1
$ ls -alt
total 24
drwxr-xr-x 41 root    root    4096 May  7  2020 ..
-rw-r-----  1 bandit2 bandit1   33 May  7  2020 -
drwxr-xr-x  2 root    root    4096 May  7  2020 .
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root     675 May 15  2017 .profile
```

I guessed "I'll just *cat* it", but boy, I was wrong. This file is named '-', which is a character the command *cat* understands as if we were to input an option to it. Instead, we need to redirect the file to the command cat using another character, such as '<', or instead specifying its relative path to this directory with './'.

```shell
$ cat -
(nothing really happened here so I had to close the process with CTRL+C)
$ cat < -
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
$ cat ~/- (it is the same as above)
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

> Level 2 Password = CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
# Level 2
>*The password for the next level is stored in a file called **spaces in this filename** located in the home directory.*

```shell
$ pwd
/home/bandit2
$ ls -alt
total 24  
drwxr-xr-x 41 root    root    4096 May  7  2020 ..  
drwxr-xr-x  2 root    root    4096 May  7  2020 .  
-rw-r-----  1 bandit3 bandit2   33 May  7  2020 spaces in this filename  
-rw-r--r--  1 root    root     220 May 15  2017 .bash_logout  
-rw-r--r--  1 root    root    3526 May 15  2017 .bashrc  
-rw-r--r--  1 root    root     675 May 15  2017 .profile
```

It seems the challenge in this level is, just as the file says, the spaces in that filename. Trying to *cat* the file just as is will just confuse the *cat* command, making it think each word is a different file or directory. The past game solution will not work either.

```shell
$ cat spaces in this filename
cat: spaces: No such file or directory  
cat: in: No such file or directory  
cat: this: No such file or directory  
cat: filname: No such file or directory
$ cat ./spaces in this filename
cat: ./spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
```

Instead, we will use *'* to indicate that it is a composite name, not separated arguments.

```shell
$ cat 'spaces in this filename'
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

>Level 3 Password:  UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
# Level 3
>*The password for the next level is stored in a hidden file in the **inhere** directory.*

```shell
$ pwd  
/home/bandit3  
$ ls -alt  
total 24  
drwxr-xr-x  2 root root 4096 May  7  2020 inhere  
drwxr-xr-x  3 root root 4096 May  7  2020 .  
drwxr-xr-x 41 root root 4096 May  7  2020 ..  
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout  
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc  
-rw-r--r--  1 root root  675 May 15  2017 .profile  
$ cd inhere
~/inhere$ ls
(It is empty)
```

Since we know (as per the scope of the challenge) that the flag must be somewhere in the 'inhere' directory, there must be something we are missing, so instead, let's use flags for our *ls* command to check for hidden files. Here (and usually) I use *-alt* as my flags, but a regular *-a* would have been sufficient.

```shell
$ ls -alt  
total 12  
drwxr-xr-x 2 root    root    4096 May  7  2020 .  
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden  
drwxr-xr-x 3 root    root    4096 May  7  2020 ..  
$ cat .hidden  
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

>Level 4 Password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB
# Level 4
>*The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.*

```shell
$ pwd
/home/bandit4
$ ls -alt
total 24
drwxr-xr-x  2 root root 4096 May  7  2020 inhere
drwxr-xr-x  3 root root 4096 May  7  2020 .
drwxr-xr-x 41 root root 4096 May  7  2020 ..
-rw-r--r--  1 root root  220 May 15  2017 .bash_logout
-rw-r--r--  1 root root 3526 May 15  2017 .bashrc
-rw-r--r--  1 root root  675 May 15  2017 .profile
$ cd inhere
~/inhere$ ls -alt
total 48
drwxr-xr-x 2 root    root    4096 May  7  2020 .
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file09
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file08
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file07
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file06
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file05
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file04
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file03
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file02
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file01
-rw-r----- 1 bandit5 bandit4   33 May  7  2020 -file00
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
$ cat ./-file00
�/`2ғ�%��rL~5�g��� �����
```

The apparent problem is that not all files in this challenge are encoded in a way that's human-readable. Some of these human-readable formats are namely **ASCII**, **UTF-8** and the lot. For this challenge, you could either bruteforce it by using *cat* on every single file, or we can go the intelligent way and use *file* to check the file type of each file.

We can see that ./-file07 is in a human-readable encoding, and as such, must be our flag.

```shell
$ file ./*
./-file00: data  
./-file01: data  
./-file02: data  
./-file03: data  
./-file04: data  
./-file05: data  
./-file06: data  
./-file07: ASCII text  
./-file08: data  
./-file09: data
$ cat ./-file07 
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

>Level 5 Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh
# Level 5
>*The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:
> - human-readable
> - 1033 bytes in size
> - not executable*

Ok. For this challenge things have changed a bit. We check that we're in the correct level by using *pwd* and then we *cd* into the inhere directory. We *ls -alt* all the files and boom; there is a ton of other directories, each with 9 files inside.

```shell
$ pwd
/home/bandit5
$ ls -alt
total 24  
drwxr-x--- 22 root bandit5 4096 May  7  2020 inhere  
drwxr-xr-x  3 root root    4096 May  7  2020 .  
drwxr-xr-x 41 root root    4096 May  7  2020 ..  
-rw-r--r--  1 root root     220 May 15  2017 .bash_logout  
-rw-r--r--  1 root root    3526 May 15  2017 .bashrc  
-rw-r--r--  1 root root     675 May 15  2017 .profile
$ cd inhere
~/inhere$ ls -alt
total 88
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere19
drwxr-x--- 22 root bandit5 4096 May  7  2020 .
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere15
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere16
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere17
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere18
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere10
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere11
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere12
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere13
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere14
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere06
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere07
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere08
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere09
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere02
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere03
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere04
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere05
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere00
drwxr-x---  2 root bandit5 4096 May  7  2020 maybehere01
drwxr-xr-x  3 root root    4096 May  7  2020 ..
```

We were given special hints that the file we are looking for has to have. It must be human-readable, 1033 bytes in size, and not an executable. For this challenge, we can use the *find* command, in combination with the *file* we used in the past challenge. The command *file* will allow us to find the attribute of human-readable, while *find* will get us the file size.

Note: We use the * (wildcard) to signify 'everything'; every single file inside every single directory. We then pipe the command using '|' to the *grep* command, which prints lines matching the pattern we specify, in this case 'ASCII'.

```shell
~/inhere$ file ./*/* | grep ASCII
```

We can see this yielded... not very good results. There are a lot of files which are readable, and way too many to bruteforce (I mean, you could always do it that way, but it'd be a pain in the neck).

```shell
~/inhere$ file ./*/* | grep ASCII  
./maybehere00/-file1:       ASCII text, with very long lines  
./maybehere00/-file2:       ASCII text, with very long lines  
./maybehere00/spaces file1: ASCII text, with very long lines  
./maybehere00/spaces file2: ASCII text, with very long lines  
./maybehere01/-file1:       ASCII text, with very long lines  
./maybehere01/-file2:       ASCII text  
./maybehere01/spaces file1: ASCII text, with very long lines
... (long etcetera)
```

I thought for a moment to compare the size of the flags we've gotten so far, product of my very classical CTF mindset. I encountered they were all 32 characters long, and thought "Is there a way to check how long a string is?", and for sure, there is. The wordcount, or *wc* utility let's us do just that by using the flag *-m*. It will then print how many characters it finds and what file it found them in. I used the same piping method and *grep*ped 32, as I'm looking for a 32-characters-long file.

```shell
~/inhere$ wc ./*/* -m | grep 32
  5532 ./maybehere04/spaces file1
```

Welp. That did not work. I'm assuming that *wc* counts spaces as characters too. What we will instead attempt, is checking what *find* will yield when we specify the size of the file we are looking. A quick look at the manual page for find (using *man find*) tells us that we can use the flag *-size*, and append *c* after the value we're looking for to specifically search for bytes. To our surprise, there is only one file which is a 1033 byte size. We can *cat* it and see what it yields.

```shell
~/inhere$ find -size 1033c  
./maybehere07/.file2
~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
```

And I was right! It is encoded with a bunch of spaces. We can see that *wc* does count spaces if we run it on this file and check how many characters it outputs.

```shell
~/inhere$ wc -m ./maybehere07/.file2  
1033 ./maybehere07/.file2
```

It was ALSO 1033! We have now learned that the ASCII encoding uses each space and/or character in one byte (8 bits!).

>Level 6 Password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7
# Level 6
>*The password for the next level is stored **somewhere on the server** and has all of the following properties:
> - owned by user bandit7
> - owned by group bandit6
> - 33 bytes in size*

Cool. Finally moving up in the world. Now, it isn't just a directory, it's *somewhere*, and detective Kedislav is on the case. We're finding this flag. One thing to note; the file cannot be the one in the etc folder, since that's where all the passwords are kept.  We use *pwd* to figure out where we are and if we are in the correct level.

```shell
$ pwd
/home/bandit6
```

To solve this challenge, we can use the *find* utility from last challenge. Reading through its manual page (or a quick google search), we can learn that using the *-user* and *-group* flags we can specify what user and what group the file is owned by. If we combine that with the flag we used in the past challenge, *-size*, we can search exactly the file we need!

Note: I used *find /* and not *find* with a wildcard since I want the *find* utility to search recursively through all of the file system. In UNIX systems, the file-system structure is like that of a tree, and as such, we start from the root of it all, the / (root) directory.

```shell
$ find / -type f -user bandit7 -group bandit6 -size 33c
find: ‘/root’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
...
/var/lib/dpkg/info/bandit7.password
$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

A ton of what was printed is files that we do not have permissions to access from this user, hence the 'Permission denied' comment. Besides the gibberish, we found one file we do have permission to access. We *cat* that file real quick and we have our flag!

>Level 7 Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
# Level 7
>*The password for the next level is stored in the file **data.txt** next to the word **millionth**.*

```shell
$ pwd
/home/bandit7
$ ls -alt
total 4108
-rw-r-----  1 bandit8 bandit7 4184396 May  7  2020 data.txt
drwxr-xr-x  2 root    root       4096 May  7  2020 .
drwxr-xr-x 41 root    root       4096 May  7  2020 ..
-rw-r--r--  1 root    root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root    root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root    root        675 May 15  2017 .profile
```

Immediately by looking at the 'total' from the *ls* output, I can guess there is a big file in here. If I *cat* the file data.txt, I get printed a big, long list of words and strings next to them.

Note: Using *cat* on this file will print a long list. Put a stop to it by using CTRL+C!

```shell
$ cat data.txt
binning WnfnFPqkuhl2nwHBohzn2C4L5W0gwcLq
abuts   v8PAwDdkGDdp5NsJ7ZFM5A7TJ5MkYDbm
fathead wBhCy0fqvbQdexz5kMKBtGoSWgXw7s0H
attacks 3GzwnGiZnBDdVuHivJk1pEfOOYu7uOTa
lopping H9hzviFp1QO4WF8EzcQNl5MDz5r1bzUC
tyrannosaurus   WxtYXVar4sgInHp7YUpTzOjdUw1Ww0x8
reservists QDidoX6BN1MDTi0QwA6Vt82L9Rb64cm3
```

We can kinda guess that this is a long list, similar to a dump of some kind of credentials. Very realistic, I like it. Since we have been using *grep* for a while now, let's try it now. Remember that *grep*'s utility shines because it prints lines matching the pattern we specify. We can pipe the *cat* command into *grep millionth* and check the output. Boom, we got our flag!

```shell
$ cat data.txt | grep millionth
millionth  cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

>Level 8 Password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV
# Level 8
>*The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.*

```shell
$ pwd
/home/bandit8
$ ls -alt
total 56  
drwxr-xr-x  2 root    root     4096 May  7  2020 .  
-rw-r-----  1 bandit9 bandit8 33033 May  7  2020 data.txt  
drwxr-xr-x 41 root    root     4096 May  7  2020 ..  
-rw-r--r--  1 root    root      220 May 15  2017 .bash_logout  
-rw-r--r--  1 root    root     3526 May 15  2017 .bashrc  
-rw-r--r--  1 root    root      675 May 15  2017 .profile
```

Ok, it seems the difficulty has gone up a bit. When we *cat* data.txt, we get a long list of random gibberish lines in disorder. Assuming from the level goal, most of these repeat at least once, yet there is only one that occurs once; our flag.

There are various ways to do it. A handy command to use is *sort*, which, well, sorts stuff. We can use it with the *-f* flag to ignore capitalization (considering all the files inside are random, capitalized or not, strings). We could sort it out like this and then scrutinize by eye to see which one pops out only once, but this is a rather brute and unintuitive way to do it.

Another handy command is *uniq*, as it reports or omits repeated lines. For this case use, we wanna omit them (as we want the unique one), so we will use the *-u* flag so it only prints the unique lines.

Combining both these commands with a pipe (|) comes in very handy, as we want to sort first (because *uniq* does not parse through the entire list, it just compares), and then point the only unique line. And voila! We got our flag!

```shell
$ sort -f data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

>Level 9 Password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
# Level 9
>*The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.*

We start by identifying what we're working with. We *pwd* to check where we are and if we're in the correct level, then *ls -alt* to list all files, and finally, *cat* data.txt to check what is inside the file.

```shell
$ pwd
/home/bandit9
$ ls -alt
total 40
drwxr-xr-x 41 root     root     4096 May  7  2020 ..
drwxr-xr-x  2 root     root     4096 May  7  2020 .
-rw-r-----  1 bandit10 bandit9 19379 May  7  2020 data.txt
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
-rw-r--r--  1 root     root      675 May 15  2017 .profile
$ cat data.txt
�L�lω;��ßOܛ��ǤX��NdT$��x7��@D@�o��+D��B��M֢�Z/,_���w���#�5���  
(a lot more like this gibberish)
$ file data.txt
data.txt: data
```

We found that data.txt isn't entirely human-readable. Actually, we ran *file* on data.txt to check what type of file it was, and sure as heck, it is data. From the level goal, we know it is in here. We could either *cat* the file and search manually for a bunch of ='s, or we could take the more optimized route of using a command to do it for us.

The command *strings* becomes relevant here; looking at its manual page with *man*, we see that it prints the strings of printable characters in files. Exactly what we need! Since we know that what we're looking for has to be human-readable, I used *-e s* to specify I'm looking for characters that are encoded in human-readable formats, such as ASCII, ISO 8859, etc, but it isn't necessary. We also know that the flag is preceded by a bunch of '=', so we can pipe (using |) the output of our *strings* command to *grep ==*. And there we have it, our flag pops up.

```shell
$ strings -e s data.txt | grep ==
========== the*2i"4  
========== password  
Z)========== is  
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

>Level 10 Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
# Level 10
>*The password for the next level is stored in the file **data.txt**, which contains base64 encoded data.*

```shell
$ pwd
/home/bandit10
$ ls -alt
total 24  
drwxr-xr-x 41 root     root     4096 May  7  2020 ..  
drwxr-xr-x  2 root     root     4096 May  7  2020 .  
-rw-r-----  1 bandit11 bandit10   69 May  7  2020 data.txt  
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout  
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc  
-rw-r--r--  1 root     root      675 May 15  2017 .profile
$ file data.txt
data.txt: ASCII text
$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
```

```shell
$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

>Level 11 Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
# Level 11
>*The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.*

```shell
$ pwd
/home/bandit11
$ ls -alt
total 24  
drwxr-xr-x 41 root     root     4096 May  7  2020 ..  
drwxr-xr-x  2 root     root     4096 May  7  2020 .  
-rw-r-----  1 bandit12 bandit11   49 May  7  2020 data.txt  
-rw-r--r--  1 root     root      220 May 15  2017 .bash_logout  
-rw-r--r--  1 root     root     3526 May 15  2017 .bashrc  
-rw-r--r--  1 root     root      675 May 15  2017 .profile
$ file data.txt
data.txt: ASCII text
$ cat data.txt
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
```

This is an encryption method known as ROT13, meaning we "rotate" or replace each letter from their respective position with the one 13 letters onward (taking 'A' as position 1). For decoding, we do the same operation, as the english alphabet is 26 letters long so direction does not matter. To apply this operation to a file or text, we can use the command *tr*, which function is to translate or delete characters. We want to translate the regular alphabet, A-Z, 13 letters onward, so A becomes N, and Z becomes M.

We know it also applies to the lowercase variants to, so we run a little test. We use *echo* do display the 'test' line and pass it to our test command using a pipe. If we count 13 from each letter, we see it successfully reads test. We can even reproduce the same operation on the encoded variant to check if we're right.

```shell
$ echo test | tr 'A-Za-z' 'N-ZA-Mn-za-m'  
grfg
$ echo grfg | tr 'A-Za-z' 'N-ZA-Mn-za-m'                  
test
```

Now, we can just pass the output of the *cat* data.txt command, through a pipe and into our custom *tr* command made to encode/decode ROT13... and voila! We got our flag.

```shell
$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'  
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

>Level 12 Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
# Level 12
>*The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)*
