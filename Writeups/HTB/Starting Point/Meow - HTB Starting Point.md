# Meow - HackTheBox Starting Point (Machine 1)
The tags available for this machine are *enumeration*, *telnet*, *external* and *penetration tester level 1*. It is a good machine to practice the core basics of the telnet service and how to break it. We start by connecting to our VPN to access the machines by using the `openvpn` command.

```shell
$ sudo openvpn ~/path/to/file/starting_point_<username>.ovpn
```

After we spawn our machine, we receive an IP address. Mine was assigned to be `10.129.212.7`, so I'll be using that. Note that your machine's IP will probably be different.

## Enumeration

We start by enumerating our target machine. We can use either `nmap` or `masscan`. Whichever one you use, just be sure to use the correct flags. In my case, I'll be using `nmap`, paired with the `-A` to enable OS detection, service version detection, script scanning and traceroute.

**Note: this `nmap` scan is not quiet, as it runs a lot of pings and requests to the target! To run a stealthy scan, please use AT LEAST the `-s` flag to spoof your IP, `-f` to evade firewall, and the `-sS` to run a SYN scan only. Consider using the `proxychain` utility as well.

```shell
$ nmap -A -T4 10.129.212.7
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-08 15:54 EDT  
Nmap scan report for 10.129.212.7  
Host is up (0.18s latency).  
Not shown: 999 closed tcp ports (conn-refused)  
PORT   STATE SERVICE VERSION  
23/tcp open  telnet  Linux telnetd  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  
  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .  
Nmap done: 1 IP address (1 host up) scanned in 40.66 seconds
```

Our `nmap` scan returns port 23 open, which is the default port for telnet (see [default port assignment](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)) so we know this machine is running service *telnet*, version *Linux telnetd*. The scan also tells us that this machine is running a *Linux OS*. Very useful! Now, let's turn to the questions on the HTB webpage.

## Tasks and Flag

>#task-1 **Task 1:  What does the acronym VM stand for?**
>*Hint: Described in the Setting Up section of the write-up, it is the alternative to using the dedicated, browser-based Pwnbox service.*
>Answer: virtual machine.

The hint very clearly points us in the direction of the answer, but the term *VM* is one you'll see a lot in the tech world, so be sure to remember it. You'll probably use VM's when setting up a personal lab, testing programs, analyzing files and other fun things!

>#task-2 **Task 2: What tool do we use to interact with the operating system in order to issue commands via the command line, such as the one to start our VPN connection? It's also known as a console or shell.**
>*Hint: One word. It's also the name of the location in any airport where passengers transfer between ground transportation and the facilities that allow them to board their flight.*
>Answer: terminal

This is one question I like a lot. On the surface, *terminal*, *console* and *shell* are explained to be synonyms. People will use these terms interchangeably, but in terms of specifics, they are different. Check [this link](https://www.geeksforgeeks.org/difference-between-terminal-console-shell-and-command-line/) and [this link](https://www.freecodecamp.org/news/command-line-for-beginners/#differencebetweenconsolecommandlinecliterminalandshell) to see the exact differences.

>#task-3 **Task 3: What service do we use to form our VPN connection into the HTB labs?**
>*Hint: It's an open source VPN service which comes preinstalled on most Linux-based Operating Systems.*
>Answer: openvpn

We already used `openvpn` to open and interpret the `starting_point_<username>.ovpn` file to connect, through a VPN tunnel, to the starting point lab. Read more about `openvpn` in [this link](https://community.openvpn.net/openvpn/wiki/OverviewOfOpenvpn).

>#task-4 **Task 4: What is the abbreviated name for a 'tunnel interface' in the output of your VPN boot-up sequence output?**
>*Hint: Short for tunnel. The tunnel interface is your connection between the target's network and your own VM.*
>Answer: tun

As we said before, VPN connections initiate a tunneled connection, direct between you and the target. The tunnel abbreviation most commonly used is `tun`, and you can see it for yourself in your own interface. Input the `ip address` command (you could also use `ifconfig`!), and your output should look like the code block below;

```shell
$ ip address
1: lo ... # this is your loopback address, or localhost, so to speak.
2: wlan0 or eth0 ... # this is your internet connection; WLAN is for wireless, and ETH is for ethernet, note that you might have both connected and, as such, both will appear.
3: tun0 ... # this is the VPN tunnel!
```

To read more about network interfaces, check [this link](https://codewithyury.com/demystifying-ifconfig-and-network-interfaces-in-linux/) to read more about network interfaces, and check [this video out](https://www.youtube.com/watch?v=SSLpvcIOPK0) for a more guided explanation. Let us continue!

>#task-5 **Task 5: What tool do we use to test our connection to the target with an ICMP echo request>**
>*Hint: It's also half of the name of a very popular sport, also known as table tennis.*
>Answer: ping

The hint already tells us enough, but what even is *ICMP*, and what is an *echo request*? Very short explanation, ICMP is short for **Internet Control Message Protocol** and it is what we use to "check" whether a host is alive or not. Think of the *echo request* as the type of message, akin to knocking on a door and asking "Hey, are you there?". If the host answers back "Yes, I'm here, alive and well", we know they're, pardon my redundancy, alive and well.

You can try this utility for yourself by pinging whatever you want. Let's say we `ping` google.com, for example. Be sure to exit the pinging by using **ctrl + c**. You'll see something similar to the code block below;

```shell
$ ping google.com
PING google.com (142.251.0.113) 56(84) bytes of data.  
64 bytes from cj-in-f113.1e100.net (142.251.0.113): icmp_seq=1 ttl=59 time=23.7 ms  
64 bytes from cj-in-f113.1e100.net (142.251.0.113): icmp_seq=2 ttl=59 time=24.7 ms  
64 bytes from cj-in-f113.1e100.net (142.251.0.113): icmp_seq=3 ttl=59 time=24.4 ms  
^C  
--- google.com ping statistics ---  
3 packets transmitted, 3 received, 0% packet loss, time 2001ms  
rtt min/avg/max/mdev = 23.733/24.274/24.722/0.409 ms
```

Success! We can see that out of 3 packets transmitted (or sent), 3 packets were received by google.com! Google lives and is alive and well. To see more in depth information about the [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) and the [ping command](https://en.wikipedia.org/wiki/Ping_(networking_utility)) check those links.

>#task-6 **Task 6: What is the name of the most common tool for finding open ports on a target?**
>*Hint: Short for Network Mapper, a popular network host scanning tool.*
>Answer: nmap

We already used this utility! Network Mapper, or `nmap` is usually the first step to any penetration test. We need to find the open ports, we need to enumerate our target to see what possible attack vectors are at our disposal. You can see more information [about nmap here](https://nmap.org/book/man.html#man-description) and a guided [video on how to use it](https://www.youtube.com/watch?v=4t4kBkMsDbQ) here. 

>#task-7 **Task 7: What service do we identify on port 23/tcp during our scans?**
>*Hint: This service runs on port 23/tcp by default, meaning we can research the port on Google and receive the correct result easily.*
>Answer: telnet

Let's remember we already did our enumeration on this machine right at the very start. Our `nmap` scan told us port 23/tcp is running `telnet`. To read a bit more in-depth about telnet, [check here](https://en.wikipedia.org/wiki/Telnet) for a description, and [a more advanced guide on pentesting telnet](https://book.hacktricks.xyz/network-services-pentesting/pentesting-telnet) service here.

>#task-8 **Task 8: What username is able to log into the target over telnet with a blank password?**
>*Hint: It is popularly known as the administrative account for any Linux-based Operating System, residing at the highest level of privilege on any such system.*
>Answer: root

First, to log in to anything, we need to connect to the machine. To do that, we know `telnet` is open, and the box is hinting towards it, so let's go and connect to it using the `telnet` protocol.

**Note: if unsure of how to use a command, always remember to check the manual pages by using `man` and then the command. Full syntax is `man <command>`.

```shell
$ telnet 10.129.212.7  
Trying 10.129.212.7...  
Connected to 10.129.212.7.  
Escape character is '^]'.  
  
 █  █         ▐▌     ▄█▄ █          ▄▄▄▄  
 █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀  
 █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█  
  
  
Meow login:
```

We are now presented with a login screen. If you paid attention to the hint, you'd know the highest privilege account in a Linux-based (actually UNIX-based, but you'll get to that) OS is *root*. To read about why [check this link](https://frameboxxindore.com/other/best-answer-what-is-the-difference-between-root-and-administrator.html), but very basically, Linux-based systems use a tree file-system. Everything inside the OS stems and branches off like a tree, and at the core of it, is the root. The *root user* is a superuser that has the capacity to read and write to anything in the file system.

Let us try using *root* as the possible login. The task also hints to it having no password, and password-cracking is a more advanced skill (check out the `hydra` command if you're interested), so we will not delve into that.

```shell
$ telnet 10.129.212.7  
Trying 10.129.212.7...  
Connected to 10.129.212.7.  
Escape character is '^]'.  
  
 █  █         ▐▌     ▄█▄ █          ▄▄▄▄  
 █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀  
 █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█  
  
  
Meow login: root

Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)  
  
* Documentation:  https://help.ubuntu.com  
* Management:     https://landscape.canonical.com  
* Support:        https://ubuntu.com/advantage  
  
 System information as of Sun 08 May 2022 08:55:57 PM UTC  
  
 System load:           0.0  
 Usage of /:            41.7% of 7.75GB  
 Memory usage:          4%  
 Swap usage:            0%  
 Processes:             137  
 Users logged in:       0  
 IPv4 address for eth0: 10.129.212.7  
 IPv6 address for eth0: dead:beef::250:56ff:feb9:ca40  
  
* Super-optimized for small spaces - read how we shrank the memory  
  footprint of MicroK8s to make it the smallest full K8s around.  
  
  https://ubuntu.com/blog/microk8s-memory-optimisation  
  
75 updates can be applied immediately.  
31 of these updates are standard security updates.  
To see these additional updates run: apt list --upgradable  
  
  
The list of available updates is more than a week old.  
To check for new updates run: sudo apt update  
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection  
or proxy settings  
  
  
Last login: Sun May  8 20:52:33 UTC 2022 on pts/0  
root@Meow:~#
```

We are now the *root user*! Let's use basic linux commands to navigate the filesystem using the command line. You can read about those [in this link](https://www.freecodecamp.org/news/command-line-for-beginners/#mostcommonandusefulcommandstouse). We will be using the `pwd` command to find out where we are and the `ls` command to list the files. We will find a *flag.txt* so we will use the `cat` command to check its contents.

```shell
root@meow:~# pwd
/root # This means we are in the root of the file system!
root@meow:~# ls
flag.txt  snap # Our flag is here
root@meow:~# cat flag.txt
b40abdfe23665f766f9c61ecba8a4c19
```

Another machine pwned! #flag == b40abdfe23665f766f9c61ecba8a4c19
