1. echo -n "Daniil"
2. touch ~/otchet/files/2.txt
   pwd > ~/otchet/files/2.txt
   whoami >> ~/otchet/files/2.txt 
3. touch ~/otchet/files/3.txt
   ls -li > ~/otchet/files/3.txt
4. touch ~/otchet/files/4.txt
   touch ~/otchet/files/4.md
   cat ~/otchet/files/4.txt > ~/otchet/files/4.md
5. chmod go-r ~/otchet/files/4.txt
6. chmod 775 ~/otchet/files/4.md
7. mv ~/otchet/4.txt ~/otchet/files/4.txt 
   mv ~/otchet/4.md ~/otchet/files/4.md 
8. sudo chown -c root ~/otchet/files/4.md 
9. sudo useradd -m test_user 
   sudo groupadd wheel
   sudo usermod -g wheel test_user
   sudo chsh -s /bin/zsh test_user 
10. sudo passwd test_user
11. already in group
12. cat /etc/passwd > ~/otchet/files/12.txt 
13. chmod a+w ~/otchet/files/12.txt
14. su -p test_user
15. whoami >> /home/matko_dd/otchet/files/12.txt
    pwd >> /home/matko_dd/otchet/files/12.txt
16. exit
17. sudo su 
18. whoami >> /home/matko_dd/otchet/files/12.txt
    pwd >> /home/matko_dd/otchet/files/12.txt
19. tail -n 2 ~/otchet/files/12.txt
20. sudo groupdel wheel
    sudo userdel -r test_user
21. find ~/ -maxdepth 2 -empty > ~/otchet/files/21.txt 
22. sudo find / -maxdepth 3 -user root -name 'dev*' > ~/otchet/files/22.txt 
23. mkdir ~/test_find
    mkdir ~/test_find/time
    mkdir ~/test_find/permissions
24. touch ~/test_find/time/one.txt
    touch ~/test_find/time/two.txt
    touch -a -t 202401010000 ~/test_find/time/one.txt 
    touch -m -t 202410140000 ~/test_find/time/two.txt
25. touch ~/test_find/cant_write
    touch ~/test_find/can_execute
    chmod a-w ~/test_find/cant_write
    chmod a+x ~/test_find/can_execute
26. find ~/test_find -type f -empty -atime -180 -delete
27. find ~/test_find -type f -perm 755 -exec chmod a-x {} +
28. man ls > ~/otchet/files/man_ls.txt
29. grep -n "^$" ~/otchet/files/man_ls.txt
30. grep -E "[0-9]+" ~/otchet/files/man_ls.txt
31. grep -i 'author' ~/otchet/files/man_ls.txt > ~/otchet/files/31.txt
32. wc -l man_ls.txt
    du -sh man_ls.txt
33. ps -u $USER > ~/otchet/files/33.txt
34. nano
35. pgrep nano
36. pkill nano
37. htop
