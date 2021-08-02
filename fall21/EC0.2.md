# Extra Credit (EC) 0.2 - ODU-CS Linux

Login to the [Linux system at ODU-CS](https://systems.cs.odu.edu/Unix_and_Linux_Services).  Note that if you're off-campus, you will first need to login to the [CS VPN](https://gp.cs.odu.edu) (download the [GlobalProtect VPN Client](https://www.odu.edu/ts/software-services/vpnclient)).

Create a directory for files for this course (name it whatever you wish, but something like `cs432` or `cs532` is probably a good idea). Change the permissions on this directory so that you are the only user who can read, write, or execute (view the contents) the directory (see ["Protection and Permission"](https://www.cs.odu.edu/~zeil/cs252/latest/Public/protection/index.html)).

In the directory that you just created, use the simple nano editor to create a file named text.txt (`nano test.txt`) with the following contents:

```text
CS 800
CS 432
CS 725
MATH 212
MATH 32
```

Execute each of the following commands and save its output. Explain in words what the command has done:

1. `wc -l test.txt`
1. `echo "CS 800" >> test.txt; cat test.txt`
1. `grep CS test.txt`
1. `grep -c CS test.txt`
1. `sort test.txt`
1. `sort -k2 test.txt`
1. `sort -k2 -n test.txt`
1. `sort test.txt | uniq -c`

For more information, see ["Redirection and Pipes"](https://www.cs.odu.edu/~zeil/cs252/latest/Public/redirection/index.html).  For information on the Unix commands, you can use the `man` command (ex: `man grep`) to display the manual page or do a web search for the command.