# albumSQLite
# Overview

This program stores CD information in a simple relational database. The menu prompts for user input and allows the user to add new artists or add albums to existing artists. Album information can be edited or deleted. There is also an option to view basic statistics of the database (number or albums per artist or genere)

I wrote this out of personal interest. I have a lot of physical CDs and I was curious about how much I have of different generes or artists.

[Software Demo Video](https://youtu.be/GYnakBp4NTI)

# Relational Database

Local database file. Contains an artist table and album table. 

Artist holds ID(primary key) and Name. 
Album holds ID(primary key), artist ID (foreign key), Name, Genre

# Development Environment

Code was written in VSCode using python and SQLite3

# Useful Websites

- [YouTube Python SQLite Tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA)
- [Official Python Documentation](https://docs.python.org/3/library/sqlite3.html)

# Future Work

- Expand tables to include more information (album release year, composer names, etc.)
- Impliment a graphical UI, potentially