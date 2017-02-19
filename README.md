# PDX Pixel

[pdxpixel.com](http://pdxpixel.com)

PDX Pixel web site and blog for sharing and collaborating ideas about programming, IT/operations, and web application development. 

Above site owned and operated by CISTech Consulting.  
[cistechconsulting.com](http://cistechconsulting.com)

## Set up

To run this web site and application, you must follow these steps:

1. Clone repository
1. Install requirements from base and local (if you want dev packages) or freeze for snapshot
1. Create postgres user/role and database with the following commands.

#### Dump database, create user, create database, import database. On remote server:

    pg_dump pdxpixel > pdxpixel.sql
    
On local development machine (assuming postgres is installed, to access postgres user use `sudo su - postgres`):
     
     psql  -U postgres
     CREATE USER pdxpixel WITH PASSWORD 'somepassword';
     CREATE DATABASE pdxpixel;
     GRANT ALL PRIVILEGES ON DATABASE pdxpixel to pdxpixel;
     
Import database from previously dumped data:

    psql pdxpixel < pdxpixel.sql