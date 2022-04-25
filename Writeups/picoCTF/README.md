# Welcome!
This here is a copy of the writeups I've developed when tackling [picoCTF challenges](https://play.picoctf.org/practice). They, in no regard, represent an official way of solving each of these, and by all means I encourage you to find your own; practicing skills is necessary to get better, and reading the answer is by no means practicing. You are more than welcome to do so if you wanna compare answers for a problem, or simply parse through my thought process. Don't forget to check out the included [resources page](https://picoctf.org/resources) as it includes useful information and insight to solve the challenges ahead. </br>

## Navigating the Writeups
I've divided the picoCTF writeups by their included categories. To navigate this, I highly recommend using the [Table of Contents](#table-of-contents) I've included, as the list only grows the further I progress into the challenges.

# Table of Contents
1. [General Skills](#general-skills)
    - [Obedient Cat](#obedient-cat)
    - [Wave-a-Flag](#wave-a-flag)
    - [Python Wrangling](#python-wrangling)
    - [Nice Netcat](#nice-netcat)

# General Skills
Useful reading for this category: 
- [picoCTF General Skills PDF](https://picoctf.org/learning_guides/Book-1-General-Skills.pdf)

## Obedient Cat
**Author: Syreal**
> Description:
> This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag).

We first start to tackle this problem by downloading the file included with the challenge. We can either use our browser or use our command line utility ```wget``` plus the link to download the file to our computer. We can then use ```cat```, a command used to concatenate files and print on the standard output (if unsure what it does, read the manual page using ```man cat```). The flag, as stated by the challenge, is in the clear, meaning it is given to us without any type of encyption or other challenge.

```shell
$ wget https://mercury.picoctf.net/static/217686fc11d733b80be62dcfcfca6c75/flag 
 
flag                         100%[=============================================>]      34  --.-KB/s    in 0s         
  
2022-04-24 18:47:05 (6.83 MB/s) - ‘flag’ saved [34/34]

$ cat flag
picoCTF{s4n1ty_v3r1f13d_b5aeb3dd}
```

## Wave a Flag
**Author: Syreal**
>Description:
>Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...

First, this challenge needs the use of a program that is listed in the link given in the description. Let's go ahead and get it using ```wget```, and then use the command ```ls``` to list the file we just downloaded, so we're absolutely sure we got it.

```shell
$ wget https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm

warm                         100%[=============================================>]  10.68K  --.-KB/s    in 0s      

2022-04-24 18:53:39 (143 MB/s) - ‘warm’ saved [10936/10936]

$ ls
warm
```

From the challenge description we know that it is a tool or binary, meaning we're probably meant to execute it. We can check what type of file it is using the ```file``` command (it will confirm it is an executable, but for redundancy's sake, I did it anyway). To run a program, we can invoke it by using ```./``` and then the name of the program. Let's try all of this now.

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

Now it runs, and it is asking that we pass the ```-h``` option. This option in many other programs is used to symbolize 'help' (not all programs, inform yourself by reading the manual). Let's try it now.

```shell
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
```

## Python Wrangling
**Author: Syreal**
> Description:
> Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py) using [this password](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt) to get [the flag](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en)?

First things first, we need to download the files required for this challenge, either with the browser or the CLI utility ```wget```. Following true l33t h4xx0r fashion, I used the latter.

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

We've been given a password text file. It might include interesting data, let's ```cat``` it and copy its contents somewhere (or leave them in the history of the terminal). From the description of the challenge, we know we'll need this to access our flag. We also ```cat``` the 'flag.txt.en' file to see it contains a seemingly random string of symbols.

```shell
$ cat pw.txt
aa821c16aa821c16aa821c16aa821c16

$ cat flag.txt.en 
gAAAAABgUAIWjVP_Ne1VPrHlLZKpvfaifN7qlLoN7NEzOpAl55av7sPuV8wQZj9V-6oI_x4L10O8R-b9c19INaTFrlGbT6YxQeLXd2S3FQA8HmFxU9NILpJGEtVPsGpzPAmLSsRwezRX
```

We also got a python script named ```ende.py```. We know it is a python script from its file extension, '.py'. You could also run ```file``` on it and check the output, which I did for redundancy's sake. We run python scripts using ```python3```, as it is the latest version of python.

```shell
$ file ende.py  
ende.py: Python script, ASCII text executable

$ python3 ende.py
Usage: ende.py (-e/-d) [file]
```

After running the python script, we see it gives us 2 options, ```-e``` and ```-d```. Testing both on the file prompts us for the password. Using the ```-e``` option leaves us with the file as it was. As you could've probably guessed by now, this python script is encrypting or decrypting the file 'flag.txt.en', hence the options ```-e``` for 'encrypt' and ```-d``` for 'decrypt'. Using the ```-d``` option and inputting the password lets us get the flag.

```
$ python3 ende.py -d flag.txt.en 
Please enter the password:aa821c16aa821c16aa821c16aa821c16
picoCTF{4p0110_1n_7h3_h0us3_aa821c16}
```

## Nice Netcat
**Author: Syreal**
>Description:
>There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 43239`, but it doesn't speak English...
