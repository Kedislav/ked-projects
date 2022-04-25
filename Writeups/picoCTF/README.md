# Welcome!
This here is a copy of the writeups I've developed when tackling [picoCTF challenges](https://play.picoctf.org/practice). They, in no regard, represent an official way of solving each of these, and by all means I encourage you to find your own; practicing skills is necessary to get better, and reading the answer is by no means practicing. You are more than welcome to do so if you wanna compare answers for a problem, or simply parse through my thought process. </br>

# Navigating


# General Skills

## Obedient Cat
**Author: Syreal**
> Description:
> This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag).

```shell
$ wget https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag 
 
flag                         100%[=============================================>]      34  --.-KB/s    in 0s         
  
2022-04-24 18:47:05 (6.83 MB/s) - ‘flag’ saved [34/34]

$ cat flag
picoCTF{s4n1ty_v3r1f13d_b5aeb3dd}
```

## Python Wrangling
**Author: Syreal**
> Description:
> Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py) using [this password](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt) to get [the flag](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en)?

```shell
$ wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en

ende.py                      100%[=============================================>]   1.30K  --.-KB/s    in 0.002s  

2022-04-24 18:45:44 (728 KB/s) - ‘ende.py’ saved [1328/1328]

pw.txt                       100%[=============================================>]      33  --.-KB/s    in 0s      

2022-04-24 18:45:45 (11.0 MB/s) - ‘pw.txt’ saved [33/33]

flag.txt.en                  100%[=============================================>]     140  --.-KB/s    in 0s      

2022-04-24 18:45:45 (25.5 MB/s) - ‘flag.txt.en’ saved [140/140]

FINISHED --2022-04-24 18:45:45--
Total wall clock time: 1.6s
Downloaded: 3 files, 1.5K in 0.002s (819 KB/s)
```

```shell
$ cat pw.txt
aa821c16aa821c16aa821c16aa821c16
```

```shell
$ python3 ende.py
Usage: ende.py (-e/-d) [file]

$ python3 ende.py -d flag.txt.en 
Please enter the password:aa821c16aa821c16aa821c16aa821c16
picoCTF{4p0110_1n_7h3_h0us3_aa821c16}
```

## Wave a Flag
**Author: Syreal**
>Description:
>Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...

First, this challenge needs the use of a program that is listed in the link given in the description. Let's go ahead and get it using ```wget```, and then use the command ```ls``` to list the file we just downloaded.

```shell
$ wget https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm

warm                         100%[=============================================>]  10.68K  --.-KB/s    in 0s      

2022-04-24 18:53:39 (143 MB/s) - ‘warm’ saved [10936/10936]

$ ls
warm
```

From the challenge description we know that it is a tool or binary, meaning we're probably meant to execute it. We can check what type of file it is using the ```file``` command (it will confirm it is an executable, but for redundancy's sake, I did it anyway). To run a program, we can invoke it by using ```./``` and then the name of the program. Let's try it now.

```shell
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-  
64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3181a501366281ab5eba1c41e54a1f40800e3966, with debug_info, not stripped

$ ./warm
zsh: permission denied: ./warm
```

As we can see, we do not have permissions to run the 'warm' file. We can change this by using the ```chmod``` command, with the ```+x``` option to add the permissions to e(x)ecute. After giving the appropriate permissions, let's try to run it again.

```shell
$ chmod +x warm

$ ./warm
Hello user! Pass me a -h to learn what I can do!
```

Now it runs, and it is asking that we pass the ```-h``` option. Let's try it now.

```shell
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
```

## Nice Netcat
**Author: Syreal**
>Description:
>There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 43239`, but it doesn't speak English...

picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}
