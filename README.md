# Task description
# Task 1 (task1)
Given a file containing a text string - indicating the path to the disk device in the Linux system. Read the file and display (stdout) the following disk device information:

Device type, for example: disk, part, lvm, rom;
The total amount in gigabytes;

In cases where it makes sense (for example, if the path is a disk partition), output also:
- The amount of free space in megabytes; 
- Type of file system, for example: ext4, swap; 
- Mount point.
On the Linux system where the code will be executed, coreutils and util-linux packages are installed.

# Task 3 (task2)
Given a file containing file names, a hash algorithm (one of MD5 / SHA1 / SHA256) and their corresponding hash sums, calculated by the corresponding algorithm and indicated in the file with a space. Write a program that reads this file and checks the integrity of the files using either the standard Python library or the md5sum / sha1sum / sha256sum program.

# Описание задачи
# Задача 1 (task1)
Дан файл, содержащий текстовую строку – указание пути к дисковому устройству в системе
Linux. Прочитайте файл и выведите на экран (stdout) следующую информацию о дисковом
устройстве:<br/>
- Тип устройства, например: disk, part, lvm, rom;
- Общий объем в гигабайтах;<br/>
<br/>
В тех случаях, когда имеет смысл (например, если путь – это раздел диска), выведите
также:<br/>
- Объём свободного пространства в мегабайтах;
- Тип файловой системы, например: ext4, swap;
- Точку монтирования.

На Linux-системе, где будет исполняться код, установлены пакеты coreutils и util-linux.

# Задача 3 (task2)
Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и
соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в
файле через пробел. Напишите программу, читающую данный файл и проверяющую
целостность файлов, используя либо стандартную библиотеку Python, либо программы
md5sum/sha1sum/sha256sum.
