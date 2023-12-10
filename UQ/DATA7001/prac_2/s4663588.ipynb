{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Prac 2 - Getting the Data I need"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1 - Assessing the Ethical Use of Data\n",
    "\n",
    "An important ethical consideration for releasing data is making sure that it is properly de-anonymised. In this part of the pratical, we will demonstrate how a dataset that at first seems  anonymised may potentially be de-anonymised. We will also walk through some potential steps to mitigate this risk.\n",
    "\n",
    "Let's say we have been given access to an *anonymised* dataset containing UQ student GPA information. Someone has attempted to anonymise this dataset by removing student names and IDs from the data. Download the dataset onto your lab machine:\n",
    "\n",
    "[student_data_anon.csv](./student_data_anon.csv)\n",
    "\n",
    "Let's also say we've managed to access a separate dataset that contains names, ages and postcodes from a UQ sporting club. Download the dataset onto your lab machine:\n",
    "\n",
    "[club_data.csv](./club_data.csv)\n",
    "\n",
    "Using the club dataset, can we possibly de-anonymise some of the students contained within the GPA dataset? Have a look at both datasets and their headers in Excel, can you think of any ways we can combine the two datasets to determine the names of the students in the anonymised student data?\n",
    "\n",
    "### Databases\n",
    "\n",
    "In the first prac we imported data from a single flat file using R. Data is commonly spread across multiple data sets or files, and often more insightful information can be gained by combining several datasets.\n",
    "\n",
    "One solution for exploring multiple datasets is to import the datasets into a *database*. In this practical, we will look at the relational database `MySQL`, which uses a standard format to interact, merge and answer questions with data called SQL (Structured Query Language).\n",
    "\n",
    "We will demonstrate the use of exploring multiple datasets by attempting to *de-anonymise* data after importing it into `MySQL`.\n",
    "\n",
    "### Importing into Phpmyadmin\n",
    "phpMyAdmin is a web tool designed to handle administrating MySQL databases. Your zone already has MySQL and phpMyAdmin configured, you can find it at `https://data7001-sXXXXXX.uqcloud.net/phpmyadmin/` (replacing sXXXXXX with your student number).\n",
    "\n",
    "The first thing we need to do is to import our CSV files into phpMyAdmin. If the CSV is in the correct format, MySQL will parse the CSV file, create the associated `table` and import the data into the table as rows. A MySQL table consists of rows and columns. Columns specify the *type* of data (e.g. whether it is text, a number, a 'True' or 'False' value etc) and the rows contain the actual data itself. Below is a visual representation of a MySQL table, as displayed by phpMyAdmin:\n",
    "\n",
    "![](img/mysql-table-in-phpmyadmin.png)\n",
    "\n",
    "Let's import the `student_data_anon.csv` file first. On the top menu of phpMyAdmin, select the `Import` option. Under the **File To Import** header, click the 'Choose File' button and browse to the location of `student_data_anon.csv` on the local system. Under the **Format** header, select `CSV` in the drop down menu, and enable the option \"The first line of the file contains the table column names\". Then press the \"Go\" button.\n",
    "\n",
    "This will create a database called \"CSV_DB\" and a table called \"TBL_NAME\" (both generic filler names) which is then filled in with the values from our CSV file. Let's rename the table name to something more meaningful - click on the `TBL_NAME` table on the left under `CSV_DB`. In this menu, click the **Operations** tab in the top menu and rename the database to `student_data_anon` under **Table Options** and press the 'Go' button.\n",
    "\n",
    "Let's import our second dataset now - `club_data.csv`. First click `CSV_DB` on the left hand menu so we are operating within the same database as our first dataset. Then press the \"Import\" tab on the top menu and follow the same steps previously outlined to import our second dataset. Rename the new table to `club_data`.\n",
    "\n",
    "### Exploring The Data\n",
    "\n",
    "Let's now have a look at how we can use SQL to ask some interesting questions about the data. Click on CSV_DB again in the left hand column and then click the 'SQL' tab on the top menu.\n",
    "\n",
    "This menu allows us to query the database using the SQL language. \n",
    "\n",
    "For example, we might ask something like - how many females are in our dataset? Try pasting in the following SQL query into the bottom input box under **SQL query on database CSV_DB:** and then press `Submit Query`.\n",
    "\n",
    "```\n",
    "SELECT COUNT( * ) \n",
    "FROM student_data_anon\n",
    "WHERE gender =  'F'\n",
    "```\n",
    "\n",
    "We can add as many filters as we want to start asking more specific questions - how many females in our dataset had a GPA less than 4?\n",
    "\n",
    "```\n",
    "SELECT COUNT( * ) \n",
    "FROM student_data_anon\n",
    "WHERE gender =  'F'\n",
    "AND GPA < 4.0\n",
    "```\n",
    "\n",
    "You can see from the above example queries that SQL statements follow a general format. We have a `SELECT <x>` query that specifies what specific results we want - in this case, the `COUNT(*)` function returns the number of rows that matches a specified criteria. We then have a `FROM` statement which specifies which **table** we want to pull our results from. We could easily run the first query against the `club_data` table (how many women are in the club_data dataset?) with the following syntax:\n",
    "\n",
    "```\n",
    "SELECT COUNT( * )\n",
    "FROM club_data\n",
    "WHERE gender = 'F'\n",
    "```\n",
    "\n",
    "The last `WHERE` clause specifies our filter, and the `AND` statement can be used to add more filters.\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "| Modify and execute the above query to determine how many **men** had a GPA **greater than** 4.0 in our `student_data_anon` table? Note: Provide SQL query AND the final answer. |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here ]\n",
    "SELECT COUNT( * ) FROM student_data_anon WHERE gender = 'M' AND GPA > 4.0;  # COUNT(*) 267"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Make sure your include your code for all questions requiring coding.**\n",
    "\n",
    "SQL supports many more functions. A tutorial on many of them are available at https://www.w3schools.com/sql/. The following task requires using the `AVG` and `MAX` functions.\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "| Write SQL queries to answer the following questions: (a) what is the average GPA of the students in the`student_data_anon` table? (b) What is the maximum GPA?|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here ]\n",
    "(a):SELECT AVG(GPA) FROM student_data_anon;\n",
    "(b):SELECT MAX(GPA) FROM student_data_anon;"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We are often interested in the groups within a collection of data, and the `group by` statement in SQL is useful for this. See https://www.w3schools.com/sql/ for an example. There are also some examples of using `group by` below, and you want may to answer the task below after you study them.\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "| Write a SQL query to generate a table of all unique postcodes and the corresponding average GPAs for students living in areas with the same postcode, with the postcodes ordered by increasing average GPAs. Which postcode has the highest average GPA?|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here ]\n",
    "SELECT postcode, AVG(GPA) FROM student_data_anon GROUP BY postcode ORDER BY 2;\n",
    "The postcode of the higest average GPA is 4069"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Combining Tables\n",
    "So we now know how to do some very basic queries across a single table. However, we want to be able to use *both tables* to see if we can use information from the club data to identify some of the users in the student dataset. This `club_data` dataset will be our *adversarial* dataset.\n",
    "\n",
    "As gender, age and postcode are available in both datasets, these three fields will be our *quasi-identifiers*. Quasi-identifiers are pieces of information that, alone, are not able to uniquely identifiy a record. However, they are correlated enough to potentially create a unique identifier.\n",
    "\n",
    "In our student data example, trying to identify a student based on gender, age or postcode alone would be difficult. However, the combination of all three may be sufficient to identify individuals.\n",
    "\n",
    "Our goal is to use our `club_data` dataset which contains these quasi identifiers to deanonymise this data. We can achieve this by using an *inner join* in MySQL. An inner join allows us to match rows in one table with rows in another table only if both tables meet the conditions specified.\n",
    "\n",
    "For example, let's say we have only 2 entries in club_data that looks like the following:\n",
    "\n",
    "| gender | age | postcode | firstname | surname  |\n",
    "|--------|-----|----------|-----------|----------|\n",
    "| F      | 23  | 4068     | Jane      | Anderson |\n",
    "| M      | 20  | 4044     | Thomas    | Hill     |\n",
    "\n",
    "We also have 3 entries in student_data_anon that looks like the following:\n",
    "\n",
    "| gender | age | postcode | GPA |\n",
    "|--------|-----|----------|-----|\n",
    "| M      | 31  | 4011     | 5.3 |\n",
    "| F      | 23  | 4068     | 5.5 |\n",
    "| F      | 20  | 4000     | 4.0 |\n",
    "\n",
    "Is there a combination of gender, age and postcode that appear in both tables?\n",
    "\n",
    "If we do an *inner-join* on the tables on these elements, we can combine the tables on these matching entries, and get a result that looks like the following:\n",
    "\n",
    "| gender | age | postcode | firstname | surname  | GPA |\n",
    "|--------|-----|----------|-----------|----------| --- |\n",
    "| F      | 23  | 4068     | Jane      | Anderson | 5.5 |\n",
    "\n",
    "You can see from this example that an *inner-join* is the act of selecting *matching entries* for specific *identifiers* from two different tables.\n",
    "\n",
    "![](img/inner-join.png)\n",
    "\n",
    "Let's do the same thing to our actual datasets and see if we can potentially match individuals to their GPA. Open the SQL editor again, and submit the following query:\n",
    "\n",
    "```\n",
    "SELECT c.* , s.GPA\n",
    "FROM club_data c\n",
    "INNER JOIN student_data_anon s ON ( s.gender = c.gender) AND (s.age = c.age) AND (s.postcode=c.postcode)\n",
    "```\n",
    "\n",
    "|<center>QUESTION</center>|\n",
    "| ---- |\n",
    "| Are there any *gender,age,postcode* combinations that have more than one  matching individual? If yes, how many such combinations are there? Note: Provide SQL query AND the final answer.|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "YES. 198 combinations. \n",
    "SELECT gender, age, postcode, COUNT( * ) AS counts FROM student_data_anon GROUP BY gender, age, postcode HAVING COUNT( * ) >= 2 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>QUESTION</center>|\n",
    "| ---- |\n",
    "| what is Debra Gibson' GPA? Note: Provide SQL query AND the final answer. |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "SELECT c.first_name, c.last_name, s.GPA FROM club_data c INNER JOIN student_data_anon s ON (s.gender = c.gender) AND (s.age = c.age) AND (s.postcode=c.postcode) WHERE c.first_name = 'Debra' and c.last_name = 'Gibson'; \n",
    "#Debra Gibson' GPA is 5.87"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### K-Anonymity\n",
    "The above examples demonstrate that student_data_anon, despite having the names removed, is still vulnerable to de-anonymisation with an adversarial dataset. One potential method of better anonymising the data is to make sure it satisfies the *k-anonymity* property for our quasi-identifiers of gender, age and postcode.\n",
    "\n",
    "So far we have only *read* data from MySQL, but for this part of the prac we want to modify the data in the database using the `UPDATE` command.\n",
    "\n",
    "Let's first copy our original database so we do not lose any accidental data! First click on the database name on the left column, `CSV_DB`. Then, one the top menu, click the 'Operations' tab. Under the 'Copy Database To' heading, give your database copy the name `CSV_DB_CP`, and make sure \"Structure and data\" and \"CREATE DATABASE before copying\" and \"Add AUTO_INCREMENT value\" is selected.\n",
    "\n",
    "We will now perform all our queries on our new copy of the database, click the 'CSV_DB_CP' database on the left and open the Query menu again.\n",
    "\n",
    "Recall from your lectures that k-anonymity property is satisfied for each individual if for each unique combination of quasi-identifiers, there are *at least k-1 individuals whose information also appear in the dataset*.\n",
    "\n",
    "We can use the following SQL statement to demonstrate how many individual rows match certain combinations of gender, age and postcode:\n",
    "\n",
    "```\n",
    "SELECT gender, age, postcode, COUNT( * ) AS counts\n",
    "FROM student_data_anon\n",
    "GROUP BY gender, age, postcode\n",
    "```\n",
    "\n",
    "Can we modify our anonymised student data such that there are at least two rows in every unique combination of gender, age and postcode (2-anonymity)?\n",
    "\n",
    "One solution may be to rounding the ages to the nearest decade. So a student who is 17 gets changed to 20, and a student who is 34 gets changed to 30.\n",
    "\n",
    "We can use the MySQL \"round()\" function to round values.\n",
    "\n",
    "Enter the following command to update the ages in the `student_data_anon` table to the nearest decade.\n",
    "\n",
    "```\n",
    "UPDATE student_data_anon SET age = ROUND(age, -1)\n",
    "```\n",
    "\n",
    "Make sure it worked by examining the table:\n",
    "\n",
    "```\n",
    "SELECT * \n",
    "FROM student_data_anon\n",
    "```\n",
    "\n",
    "Do we have less unique combinations now? Let's try our original combination count query but limit results to only those that have a count of \"1\":\n",
    "\n",
    "```\n",
    "SELECT gender, age, postcode, COUNT( * ) AS counts\n",
    "FROM student_data_anon\n",
    "GROUP BY gender, age, postcode\n",
    "HAVING COUNT( * ) = 1\n",
    "```\n",
    "\n",
    "Unfortunately it looks like there are still unique combinations. What if we round postcodes to the nearest decade, too?\n",
    "\n",
    "```\n",
    "UPDATE student_data_anon SET postcode = ROUND(postcode, -1)\n",
    "```\n",
    "\n",
    "It looks like we still have a few issues - many students over 40 are still uniquely identifiable, and it looks like students that had data entry issues without a gender specified are also still unique.\n",
    "\n",
    "One potential solution might be to remove any entries that have poor data, so our dataset only includes full entries. Lets submit another query where all entries that have an empty 'gender' column are removed:\n",
    "\n",
    "```\n",
    "DELETE FROM student_data_anon WHERE gender =  ''\n",
    "```\n",
    "\n",
    "Let's also update ages so that any entry with an age greater than 50 is set to 50:\n",
    "\n",
    "```\n",
    "UPDATE student_data_anon SET age = 50 WHERE age > 50\n",
    "```\n",
    "\n",
    "Let's have a look again to see if we still have any unique combinations:\n",
    "```\n",
    "SELECT gender, age, postcode, COUNT( * ) AS counts\n",
    "FROM student_data_anon\n",
    "GROUP BY gender, age, postcode\n",
    "HAVING COUNT( * ) = 1\n",
    "```\n",
    "\n",
    "It looks like we have successfully removed all unique identifying combinations of our *quasi-identifiers*, gender, age and postcode!\n",
    "\n",
    "We can use the following query to find the new minimum frequency of each combination of gender, age and postcode:\n",
    "\n",
    "```\n",
    "SELECT MIN( mycount ) \n",
    "FROM (\n",
    "SELECT COUNT( * ) mycount\n",
    "FROM student_data_anon\n",
    "GROUP BY gender, age, postcode\n",
    ") AS counts\n",
    "```\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "| What level of k-anonymity is our dataset now? Explain your answer. |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "The k-anonymity is level 2 ,\n",
    "SELECT MIN( mycount ) FROM (SELECT COUNT( * ) mycount FROM student_data_anon GROUP BY gender, age, postcode) AS counts; #MIN(mycount) 2. \n",
    "By searching unique combination of quasi-identifiers such as same gender, age, postcode, minimum two individuals' informeition will appear in the dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Part 2 - Hadoop Distributed Filesystem (HDFS)\n",
    "In the previous exercise we demonstrated ingesting data from a flat CSV file into a *database*, where we used SQL to explore the data. While databases like MySQL are effective at analysing small datasets, we begin to run into complex scalability issues when the size of the dataset exceeds what can be stored on a single machine. We can continue to add more disk space as the dataset grows, but then we begin to run into problems with processing speed - a single CPU can only process so much data off disk at a time.\n",
    "\n",
    "A potential solution is to scale the work *and the data* over *multiple machines*, so that processing occurs in parallel across several machines and several different hard disks. Scaling up this sort of infrastructure would just involve adding new machines, and is often referred to as *horizontal scaling*.\n",
    "\n",
    "One solution that uses horizontal scaling for storing large datasets for processing is the *Hadoop Distributed Filesystem (HDFS)*. A distributed file system is simply a file system where the data is stored on a server, not the local client machine. In HDFS, *where* the data is stored is abstracted away from the user. You can browse the data as if you were browsing on a local machine, however the dataset could potentially be stored across many different computers.\n",
    "\n",
    "In this part of the prac, we will gain some familiarity with the HDFS command line tools, and ingest some data into HDFS to be explored in future pracs.\n",
    "\n",
    "### Connect to the remote DATA7001 node\n",
    "Open the ‘Terminal’ program on the lab PC. Use SSH to connect to the DATA7001 Client Node, entering your UQ student password at the prompt.\n",
    "\n",
    "```\n",
    "ssh <username>@clientnode.zones.eait.uq.edu.au\n",
    "```\n",
    "\n",
    "NOTE: Your password won't appear on the screen as you type it in, this is to be expected – just type your password and hit the `return` key. If you are not inside a UQ network, you will need to first run `ssh <username>@remote.labs.eait.uq.edu.au`, and then run `ssh <username>@clientnode.zones.eait.uq.edu.au`.\n",
    "\n",
    "You should be presented with a screen that looks like this:\n",
    "\n",
    "```\n",
    "     ____________\n",
    "     |   \\XX/   |\n",
    "     | T. \\/ .T |      University of Queensland\n",
    "     | XX:  :XX |          Faculty of EAIT\n",
    "     T L' /\\ 'J T\n",
    "      \\  /XX\\  /\n",
    "   @\\_ '______' _/@\n",
    "   \\_X\\_ ____ _/X_/\n",
    "     \\=/\\----/\\=/\n",
    "\n",
    "-----------------------------------------------\n",
    "              DATA7001 Client Node\n",
    "-----------------------------------------------\n",
    "[sXXXXXX@data7001 ~]$\n",
    "```\n",
    "\n",
    "### Download the HR Analytics Dataset\n",
    "\n",
    "You can download the HR Analytics dataset onto the client node using the wget program. Like other unix programs, you can use the manual page to learn about how to use it. Try using the command `man wget` to read the manual for the wget program. The typing the letter `q` will exit the man page.\n",
    "\n",
    "Run the command \n",
    "\n",
    "```\n",
    "wget https://stluc.manta.uqcloud.net/mdatascience/public/datasets/HumanResourceAnalytics/HR_comma_sep.csv\n",
    "```\n",
    "\n",
    "to download the HR analytics dataset onto the data7001 node.\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|  Use `wget` to download the HR Analytics Dataset from the link specified at the beginning of the prac. |\n",
    "\n",
    "### Move data between the local filesystem and HDFS\n",
    "So far we have downloaded the HR Analytics Dataset to the local filesystem. To be able to use the Hadoop tools, we first have to push the file from our local filesystem into HDFS.\n",
    "\n",
    "As HDFS is modelled similarly to the Unix filesystem, many of the commands will seem similar to local filesystem commands. We will be using the `hadoop fs` set of commands, an overview can be found on the Hadoop file system shell documentation page:\n",
    "\n",
    "https://hadoop.apache.org/docs/r2.7.1/hadoop-project-dist/hadoop-common/FileSystemShell.html \n",
    "\n",
    "`$ hadoop fs -ls` for example is analogous to the ls command on the local filesystem.\n",
    "\n",
    "To push a local file into HDFS, we can use:\n",
    "\n",
    "`$ hadoop fs -put [local path] [hdfs path]`\n",
    "\n",
    "For example, I can push a file called “testfile” into the /tmp directory of HDFS with the following command:\n",
    "\n",
    "`$ hadoop fs -put testfile /tmp/testfile`\n",
    "\n",
    "To read a file from HDFS, we first need to copy it onto our local filesystem. To copy a file from HDFS to our local filesystem, we can use the following command:\n",
    "\n",
    "`$ hadoop fs -get [hdfs path] [local path]`\n",
    "\n",
    " For example, I can get the file we just pushed into `/tmp/testfile` on HDFS and rename it `testfile2` on my local system with the following command:\n",
    " \n",
    " `$ hadoop fs -get /tmp/testfile testfile2`\n",
    "\n",
    "To see what the file says, we can use the program cat (a command line program that can (among other things) output the contents of a file onto the terminal:\n",
    "\n",
    "```\n",
    "$ cat testfile\n",
    "hello world!\n",
    "```\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|  What does the file called `SECRET` within your home directory on HDFS contain? |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "OTXo0t5js4YXaA=="
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|  Use the hadoop fs tools to push the HR Analytics dataset you downloaded from the previous question into your home directory in HDFS. Note: Dont change the name of the file |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "hadoop fs -put HR_comma_sep.csv /tmp/HR_comma_sep.csv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|  Use the hadoop fs tools to make a copy of the file SECRET, called SECRET_copy in HDFS. |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "hadoop fs -put SECRET /tmp/SECRET_copy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 3 - Reasoning with sampling strategies\n",
    "\n",
    "\n",
    "### Simple Random Sampling\n",
    "\n",
    "As we saw in lectures, simple random sampling with replacement (SRSWR) can be accomplised as follows.  \n",
    "\n",
    "Suppose the rows of the n by d array \"data\" correspond to entries from which we wish to resample m times.\n",
    "\n",
    "The syntax of the R command is:\n",
    "\n",
    "`datasample<-data[sample(1:n,m,replace=TRUE),]`\n",
    "\n",
    "Let us try this now with the anonymised student data.  \n",
    "\n",
    "We will now load the data into R and display summary statistics.\n",
    "\n",
    "Note that, for simplicity, we will drop any rows with missing data, and only deal with complete cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Parsed with column specification:\n",
      "cols(\n",
      "  id = col_integer(),\n",
      "  gender = col_character(),\n",
      "  GPA = col_double(),\n",
      "  age = col_integer(),\n",
      "  postcode = col_integer(),\n",
      "  program = col_character()\n",
      ")\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "       id           gender               GPA             age       \n",
       " Min.   :  0.0   Length:835         Min.   :1.040   Min.   :18.00  \n",
       " 1st Qu.:223.5   Class :character   1st Qu.:3.505   1st Qu.:23.00  \n",
       " Median :450.0   Mode  :character   Median :4.720   Median :29.00  \n",
       " Mean   :447.8                      Mean   :4.539   Mean   :31.46  \n",
       " 3rd Qu.:673.5                      3rd Qu.:5.680   3rd Qu.:37.00  \n",
       " Max.   :897.0                      Max.   :6.990   Max.   :72.00  \n",
       "    postcode      program         \n",
       " Min.   :4000   Length:835        \n",
       " 1st Qu.:4067   Class :character  \n",
       " Median :4101   Mode  :character  \n",
       " Mean   :4088                     \n",
       " 3rd Qu.:4105                     \n",
       " Max.   :4169                     "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "31.4634730538922"
      ],
      "text/latex": [
       "31.4634730538922"
      ],
      "text/markdown": [
       "31.4634730538922"
      ],
      "text/plain": [
       "[1] 31.46347"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "library(readr)\n",
    "data <- read_csv(\"./student_data_anon.csv\")\n",
    "data <- data[complete.cases(data),]\n",
    "summary(data)\n",
    "mean(data$age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "We will now take a SRSWR of size 100 from the 835 case-complete rows, and compute the mean GPA of the sample."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "4.5542"
      ],
      "text/latex": [
       "4.5542"
      ],
      "text/markdown": [
       "4.5542"
      ],
      "text/plain": [
       "[1] 4.5542"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "datasample<-data[sample(1:nrow(data),100,replace=TRUE),]\n",
    "mean(datasample$GPA)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Suppose we are interested in calculating the mean GPA by gender, as well as the number of observations by gender.  \n",
    "\n",
    "We will now do so."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>gender</th><th scope=col>GPA</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>F       </td><td>4.443125</td></tr>\n",
       "\t<tr><td>M       </td><td>4.656731</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " gender & GPA\\\\\n",
       "\\hline\n",
       "\t F        & 4.443125\\\\\n",
       "\t M        & 4.656731\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "gender | GPA | \n",
       "|---|---|\n",
       "| F        | 4.443125 | \n",
       "| M        | 4.656731 | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "  gender GPA     \n",
       "1 F      4.443125\n",
       "2 M      4.656731"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>gender</th><th scope=col>GPA</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>F </td><td>48</td></tr>\n",
       "\t<tr><td>M </td><td>52</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " gender & GPA\\\\\n",
       "\\hline\n",
       "\t F  & 48\\\\\n",
       "\t M  & 52\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "gender | GPA | \n",
       "|---|---|\n",
       "| F  | 48 | \n",
       "| M  | 52 | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "  gender GPA\n",
       "1 F      48 \n",
       "2 M      52 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "aggregate(GPA~gender, datasample, mean)\n",
    "aggregate(GPA~gender, datasample, length)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have taken a single SRSWR from our overall dataset and computed the mean GPA by gender.  \n",
    "\n",
    "Repeated resampling is the basis of **bootstrapping**, wherein one constructs a set of statistics of the repeated samples.\n",
    "\n",
    "For more information on Bootstrapping, see pp 189 to 190 of the following text: http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf\n",
    "\n",
    "These then give one an empirical understanding of the distribution of those statistics as they relate to the population of interest.\n",
    "\n",
    "We will now compute and store the mean by gender for a SRSWR of size 100 repeatedly (1000 times), compute summary statistics of the mean by gender, and display a histogram of the mean by gender."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "     sample            FGPA            MGPA      \n",
       " Min.   :   1.0   Min.   :3.977   Min.   :3.811  \n",
       " 1st Qu.: 250.8   1st Qu.:4.471   1st Qu.:4.328  \n",
       " Median : 500.5   Median :4.601   Median :4.462  \n",
       " Mean   : 500.5   Mean   :4.604   Mean   :4.460  \n",
       " 3rd Qu.: 750.2   3rd Qu.:4.740   3rd Qu.:4.591  \n",
       " Max.   :1000.0   Max.   :5.227   Max.   :5.069  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "meanGPAbygender<-data.frame(sample=integer(),FGPA=double(),MGPA=double())\n",
    "for (i in 1:1000){\n",
    "    datasample<-data[sample(1:nrow(data),100,replace=TRUE),]\n",
    "    temp<-as.data.frame(aggregate(GPA~gender, datasample, mean))\n",
    "    temp$gender<-NULL\n",
    "    meanGPAbygender[i,]<-c(i,t(temp))\n",
    "}\n",
    "\n",
    "summary(meanGPAbygender)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let us plot the histograms.\n",
    "\n",
    "A histogram is a simple and widely used graphical representation of the distribution of numerical data.  \n",
    "\n",
    "The range of data is partitioned into bins, and the number of data entries in each bin (the frequencies) are counted.  The histogram is then constructed as a collection of rectangles whose base is the bin and whose height is the corresponding bin's frequency.  See also https://en.wikipedia.org/wiki/Histogram "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzdeUBU9f7/8TMDCLgNiCvgikDlEqCSpaYCmpW5lSWaaZmhpi0ut+VGuV26\nWZQ3syi1FE0hswxEKkWvZiIuoFgq5A1JsFxQEBGRZX5/zO97PA0wG8ycmePz8dfwOZ9z5j1n\n4zVnzqLSarUCAAAAHJ9a7gIAAADQOAh2AAAACkGwAwAAUAiCHQAAgEIQ7AAAABSCYAcAAKAQ\nBDsAAACFINgBAAAoBMEOAABAIQh2AAAACkGwAwAAUAiCHQAAgEIQ7AAAABSCYAcAAKAQBDsA\nAACFINgBAAAoBMEOAABAIQh2AAAACkGwAwAAUAiCHQAAgEIQ7AAAABSCYAcAAKAQBDsAAACF\nINgBAAAoBMEOAABAIQh2AAAACkGwAwAAUAiCHQAAgEIQ7AAAABSCYAcAAKAQBDsAAACFINgB\nAAAoBMEOAABAIQh2AAAACkGwAwAAUAiCHQAAgEIQ7AAAABSCYAcAAKAQBDvAKq5du6aS+OWX\nX6z6ds7OzuJ7HThwwKrvhdqqqqr+85//9O/f38PDQ61W6xbEhAkT5K4Ldo3N1lw23q86KGe5\nC1Cmvn37HjlyRK+xSZMmzZs379KlS79+/SZOnHj//ffbuKpt27YdPnxYrHDkyJH2MCmIpKvN\nAw888P333+t1mDp16rp163SvfXx8CgoKGvHdWaYNMWHChC1btshdRR17nhMnTtx555163Xbs\n2DF8+HBpy6OPPvr1119bvT4rS09P/+abb37++ef8/PyioiJBEDQajZ+fX1BQ0PDhwx988EFX\nV1dp/zp31IIgNG/e3Nvbu1+/fpMmTXrwwQfrfK9Zs2Z98skn0pY6Z7VDMHe+wd5pYQV9+vQx\nOueffvrpmpoaW1YVFRUlvntUVJSdTEqpSktLpYv7+PHjRkeRrjYPPPBA7Q5TpkwRO/j4+EgH\nOTk5iYPS09MtKJhlajExEOu4ubl16tSpc+fOs2fPtnEltfc8c+bMqd1t9OjRet0effRRG5fa\nuE6ePDlw4EDDu1wvL68jR45IxzJlR/3ggw+Wlpbqvd3Nmze9vLz0er722mvmlt3wzbaBLJtv\nMrJgv3ob4oidbL744ouBAwc+88wzchcCJXjxxRerq6t1rzt06CBvMbcbabDr2LHjiRMnmjdv\nLmM9UvHx8W+//XazZs3ElrNnz27btk3Gkhpdamrq+PHjy8rKDHcrKiq6cOGCBROfNGnSd999\np9eoO7IltXHjxn/9618qlcrct5CLVecbZESws7p77733ww8/FATh+vXrP/7447/+9S9x0MaN\nGwl2aBSxsbFyl3D7unbtmvg6ICDAflKdIAglJSVffvnlc889J7Z8+umn4ncABcjOztZLJ+7u\n7g8//HBQUJBGoyktLT19+vSBAwdOnDhheDp33XXXnDlzBEG4fv36oUOHvvrqq5qaGt2gpKSk\ngwcPhoaGip03bNhQewr5+fk//fST7c+xsUxjzTfYI7kPGSqTgd/Uhg0bJg7y8/OrPW5mZmZU\nVNRdd93VsmVLFxeXdu3aDR8+/KOPPrp+/Xqd72VK/9q/vEh5eXnpulVUVMTFxQ0bNszb29vV\n1dXNzc3X17dv377PPvtsXFxcUVGR6ZPS+4nh4sWLc+bM6dKli7Oz8+DBg3V9kpKS5s+fHx4e\n7u/v7+Xl5ezs3KJFC39//wkTJiQlJdX+pHrTPHfu3KxZszp37uzq6urr6ztjxow///yz4aPo\nHD9+fPbs2T179tRoNE2aNOnQocOoUaM2b95c56/nZWVl0dHRAQEBrq6uHTp0ePLJJ3Nzc+3k\np9hGXKY6Zq2fZWVlb775pm7OtG/ffuLEiSdOnDAwZ6yx2kjfKz09/fTp05MmTWrbtm2zZs36\n9++/ZcsWXbdr165FR0f7+fnp1o2ZM2deuHDB6CKbN2+egVm3efNmC+abKTOhPtJVSDx0FBQU\nJHaoqKho166dXgehnp9iTd8KGrgtFxUVzZ8/v1u3brr1ZPLkyWfOnDH8SUWDBw+WzvMHH3zw\n/Pnztbvl5OS8+OKLe/furW926W1xK1askE52yZIl4qCSkhI3Nzdx0MMPPyy+nj59uoll1zkf\nLly4oFvWde6gFi5caGB55ebmikNdXV2vXLli+K0bMt90TF89LFvclu1XLa7KrA3NzhHsrMLA\n/kJ6znKfPn2kgyorK2fPni3Uo1OnTocPH7asvyn/ucvLy/v372+g244dO0yclPbv28xXX33V\nsWNH8U9xm7n77rsNTGrMmDE3b96Ufl7pND/77LPa57i0adPml19+aeAo1dXV//jHP+r7PSUs\nLEwXhkQXL17s1auXXrfmzZsnJydLW2QJdo27TM1dPy9dutS7d2+9bm5ubl999VV9c8Yaq410\n6IcfftiiRQu9Ud57772LFy/27NlTr93f37+kpMTwIjMl2Jk730yZCfWRrkIRERHi6/379+s6\nbNy4UdeiUqmkHfSCgrlbQUO25TVr1tQ+eaB9+/Znz541/GG1Wu3BgwelY/Xp06eiosLoWHXO\nLr0trrCwUDrlWbNmiYPWrFkjfUfp1ayenp43btwwvQDpfFi/fn3t+SDdQRUWFjo7//8f2Zo0\naXLx4kXppGJiYsSxHn/8ccPv28D5Zu7qYcHitmC/2pCqzN3Q7BzBziqk+4t777330KFDhw4d\n2rt3b3R0tHS1e+ONN6RjzZw5s841UtSqVavTp09b0N+U/9zvv/++tNHNzU33zVtssTjYtWnT\nRtrn/vvv1/UR/xm4uLh4eXlJTwPSWbhwoXT+SKfZpEmTOgvw9/eXHgKxYBS9f9VqtVrvl7VB\ngwZVVlaK/R966KE6J6s3lrnBrkuXLvNq6dGjh9jBlGDXuMvU3PWzvjmjd4VdfcGusVYb6SAX\nF5fa9TRp0qS++Pv6668bXmSmBDtz55spM8GUVWjJkiXiCvPkk0/qOohnyo8YMUJ6uYxesDN3\nK2jItlznQhEE4amnnjL8YbVa7aJFi6SjbNu2zego9c0uvWC3f/9+6ZQXLFggDho6dKjY/t57\n72m12m7duokt4jFgU0jnQ+2ZpiPdQT366KNi+wcffFDfZ0lJSTH8vg2cb+auHhYsbgv2qw2p\nytwNzc4R7KzClIut+vfvL73YSu8rVL9+/VJTU7Oyst5++23pf+LRo0db0P/8+fN5eXkTJ04U\n2ydOnJj3f/744w+tVjtq1Chx6DfffKM7cF1VVfXrr7+uXLlyyJAhaWlpJk5K+/dtRhAEJyen\nMWPGLFiwYPLkyWPGjNH1iYqKWrVq1enTp6urq3Ut58+fnzt3rjiWl5eX9Pi53jTHjBnz/fff\nf//999LKBUH48MMPLR4lKytLTN4qlerdd98tLy/XarUZGRmdOnUS+3/22We6/nv27JFOp0+f\nPt9+++2ePXt0J+tImRvsjDIl2DXiMjV3/dSbM8HBwd99992+fftqH7uqL9gJjbTa6L3dyJEj\nExMTX331Vb1v9q1bt/7Pf/6zbt06Pz8/sbF79+6GF9nly5fz8vJef/11cZQBAwaIs66srMzc\n+WbiTDBlFVqyZMnKlSt1r11dXS9evJidnS0OTUpKqi/YmbsVWLBQ9D5jnz59vvjii48//tjb\n21tsbNasWVVVleHPO27cOLG/i4uLrk6dqqqqk7Xk5ubWN7vEYHf9+vW9e/dKv0QJgrBx40bd\n0LNnz6rVanHm6I4zvfbaa2LPsWPHGq5ZytwdVFpamtjYu3dvcTp5eXlie/v27a063yxYPcxd\n3BbsVxtelVkbmp0j2FmF0f/QHTp0yMzMlI4yffp0cWirVq2kmU96vYVKpdKdCWFuf62x+1k8\n8MADukFqtdroCS5Gb40h3WacnJzqPEWjTpWVle7u7uK4J06cqHOa99xzj/h/orq6WjrD+/fv\nb/EoM2bMEBsnT54sLUx6unRoaGjt/p6enlevXhX7P/3009IlLkuwa8Rlau76Jp0zHh4e0t80\nJ0+eXN+cscZqI32v3r17i/88BgwYIB2Umpqqa09KSpK213duq9S7774r9g8PD2/IfGvITNDW\nCnZXr14Vf3r+97//LS6ULl26VFdX1xfszN0K6mPituzr63vt2jVd+65du6Qz/7fffjP8FoMG\nDRI7e3t7Swf9+eefQi0ajaa+2WVAhw4dxAX3zjvviO3icR1pYjbl/LY654OJ+7Q77rhDbBd/\nxJdeOzVv3jyj79uQ+WbB6mHu4rZgv9rAqszd0OwcT56Qx59//tm3b99NmzaJLfv27RNfP/74\n49JjyNOmTRNfa7Xan3/+2YL+RonfUGtqagIDAwcNGjR9+vT3339/9+7dN27cMP2j1TZx4kTp\nfkRUU1Pz1VdfPf7444GBgS1atHByclKpVLqvj2Kfc+fO1TnNZ555Rvx+plarpVt7ZmZmnRf9\nmTLKTz/9JDYePXp0pIT0ZqRHjhyprKwUBOHQoUNi4/jx46Xnb0mXglwacZmau75J58xjjz3W\nsmVL8U9p1jHAGqvN008/Le7NAwMDxXZfX18xBOud2VNSUmJKtfVp4HZa30wwUYsWLcQY/fHH\nH4v/4aKiosTDTrWZuxUIDVsoM2fOFH+F1EtaxcXFpn9YK91nxM3NbcOGDeKCk6aEyMhI3Yte\nvXrdddddutcVFRV6Z5GayMR9mjTBfP7557oX0ptjS8/ENYW5882C1UPKlMVtwX61gVU1cEOz\nN9zuxOrERwjcvHnz1KlTc+fO1R1Or6mpmTZtWkREhO7X/b/++kscpWvXrtIptGvXzt3dXdxF\n6r5RmdvfqOeff37NmjW6f2MVFRX79u0T/ye1aNEiKipq6dKllt1/XO8e9zplZWUPP/yw3iH3\n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\nb9++Xbt2dXV1FUIUFhZmZmaePHlyxYoVO3fu3L9/f7NmzdQOa2XKygqNxptbt05SO0i1goJf\nhBCKUNQOAgCANbGaYhcREfHjjz8GBwe///77np6etV69fPnym2++uWnTpoiIiLfffluVhNbr\n9u08R6XctyBL7SDVLhXnXhHCUHlH7SAAAFgTqyl2mzdvDggI+Pzzz7Xa+zx7z8vLa+PGjRkZ\nGVu2bKHYNYCLEEv8xqmdotp3Oclpt66onQIAACujURTr+GmXo6Pja6+9FhUVVcecRYsWrV27\ntqysrP67zc7OHjRoUGVlXd8JraysvHXrVnl5uYODQ/33/CBz5sxZv/4Li/ryRHn5LcVY6SQs\n6NsnBqGUC+EkhMaSUpUKRSeEnSVFKhOKnRAOlhSpXCiKEI6WFKlSKBVCOFtSJCFEqVAchdBa\nUqpSoTgIYW9Jke4IRSOEzpIiVQil0sLeTkah3BGCt9PvKhOKVoiWTk7m2mHI6NEfbd9urr2Z\ni9VcsdPr9dnZ2XXPyc7ONt14V3/e3t7/+c9/6i52iqJcu3bNLK1OCBEeHj5lyhSz7Mpcbt68\nefjw4Xbt2qkd5C4nTpzo27ev2inucurUKT8/P51Op3aQajk5Oc2bN2/Tpo3aQaoVFhbm5+c/\n9thjagepZjQaT5065e/vr3aQu6Snp/v7+1vU1/l/+eWXtm3b6vUW9B35vLy827dve3t7qx2k\nWnl5eWZmZq9evdQOcpe0tLQ+ffqoneIuZ8+e7dSpk0Xd9X7r1q0OHTp06dLFXDv08vIy167M\nyGqu2E2bNm3Lli2xsbEzZsy474T169e//PLLU6dO/fLLL5s4GwAAgCWwmmJ3/vz5gICAoqKi\nvn37jhkzplu3bqaPlUVFRRkZGbt3705LS3N1dT1+/LgZyzgAAIAVsZpiJ4Q4derU7Nmzjx49\net9XBw4c+Nlnn1na5XEAAIAmY03FziQ1NTUpKSkjI6OoqEgIodfru3Xr9vTTT/fr10/taAAA\nAGqyvmIHAACA+7rPM+EAAABgjSh2AAAAkqDYAQAASIJiBwAAIAmKHQAAgCQodgAAAJKg2AEA\nAEiCYgcAACAJih0AAIAkKHYAAACSoNgBAABIgmIHAAAgCYodAACAJCh2AAAAkqDYAQAASIJi\nBwAAIAl7tQPYnCFDhhw5ckTtFAAANK7Q0NDw8HC1U9gcil1T8/X1bdu27apVq9QOYtGysrIm\n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",
      "text/plain": [
       "Plot with title “Bootstrapped Histogram for Mean GPA by Gender”"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "hist(meanGPAbygender$MGPA, col=rgb(0,0,1,0.5),main=\"Bootstrapped Histogram for Mean GPA by Gender\", xlab=\"Mean GPA\")\n",
    "hist(meanGPAbygender$FGPA, col=rgb(1,0,0,0.5),add=TRUE)\n",
    "legend(\"topright\", c(\"Male\",\"Female\"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>Task<center>|\n",
    "| ------- |\n",
    "|<center>From the histograms and summary statistics above, what can you say about the comparative *location* or *central tendency* of the mean GPA between the two groups? How about the comparative *spread* or *variability* of the mean GPA? <center>|"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### [Place your Answer here]\n",
    "As shown by the histogram, the central tendency of the male mean GPA is between 4.4 and 4.5 while the female mean GPA is between 4.5 and 4.6. \n",
    "The values for male group mostly fall between 4.0 and 4.9 while for female group the range 4.1 and 5.1."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Weighted Random Sampling\n",
    "\n",
    "For SRSWR, each observation is equally likely to appear in the sample.  Sometimes, we wish to select each observation with a probability proportional to a specified weight.  As an illustrative example, we may have demographic data from the ABS which tells us the actual proportions of males and females by age-group enrolled at university, and we wish to correct for *sampling bias*.\n",
    "\n",
    "For the purposes of this practical, we will create a non-negative weight without any special meaning for each of the n rows in our data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate some random weights which are non-negative and sum to 1\n",
    "data$weights<-runif(nrow(data))\n",
    "data$weights<-data$weights/sum(data$weights)\n",
    "\n",
    "weighteddatasample<-data[sample(1:nrow(data),100,replace=TRUE,data$weights),]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>Task</center>|\n",
    "| ---- |\n",
    "| Using this sampling approach, repeat the steps we carried out for SRSWR to create a Weighted Sample Bootstrapped Histogram for Mean GPA by Gender. |"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzdeUAU9f/H8WEBAS8gvDg8kgDz5FCyjK8KaJSGYVnelmZ4fru06yvlwZe+\nWZZlh2UWkimklkpIqWAqiXjhUSp8TSTB8kBBQESO/f2xv+84LbAX7A47PR9/LZ/57Mx759oX\ns3PYqNVqAQAAANZPJXcBAAAAaBoEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIId\nAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACA\nQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDs\nAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAA\nFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdYBZlZWU2Er/88otZ\nJ2dnZydOa//+/WadFuqqrq5+//33Bw4c6OLiolKpNAti7NixcteFZo3N1lgW3q9aKTu5C1Cm\n/v37Hz58WKuxRYsWrVu37tat24ABA8aPH/+Pf/zDwlV9//33hw4dEiscOXJkcxgVRNLV5oEH\nHvjhhx+0Ojz55JNr1qzRvPb09CwoKGjCqbNMG2Ps2LGbNm2Su4p69jwnT568++67tbrt2LFj\n+PDh0pZHH31048aNZq/PzDIzM7/99tuff/45Pz+/qKhIEARnZ2dvb29/f//hw4c/+OCDDg4O\n0v717qgFQWjdurWHh8eAAQMmTJjw4IMP1jutWbNmffLJJ9KWeme1VTB2vqG5U8MMgoKC9M75\np556qra21pJVRUdHi1OPjo5uJqNSqtLSUuniPnHihN63SFebBx54oG6HKVOmiB08PT2lg2xt\nbcVBmZmZJhTMMjWZGIg1HB0du3Tp0rVr1zlz5li4krp7nrlz59btNmrUKK1ujz76qIVLbVqn\nTp26//77de9y3dzcDh8+LH2XITvqBx98sLS0VGtyt27dcnNz0+r56quvGlt24zfbRjJtvsnI\nhP3q3xBH7GTz5Zdf3n///VOnTpW7ECjBs88+W1NTo3nt7u4ubzF/N9Jg17lz55MnT7Zu3VrG\neqQSEhLefPPNVq1aiS3nz5///vvvZSypyaWmpo4ZM6a8vFx3t6KiokuXLpkw8gkTJmzZskWr\nUXNkS2rdunX//ve/bWxsjJ2EXMw63yAjgp3Z3XvvvR988IEgCDdu3Ni+ffu///1vcdC6desI\ndmgSy5Ytk7uEv6+ysjLxta+vb/NJdYIglJSUfP31188884zY8umnn4r/AyjA8ePHtdKJk5PT\niBEj/P39nZ2dS0tLz5w5s3///pMnT+oeT8+ePefOnSsIwo0bNw4ePPjNN9/U1tZqBm3duvXA\ngQPBwcFi57Vr19YdQ35+/t69ey1/jo1pmmq+oTmS+5ChMun4TW3YsGHiIG9v77rvPXLkSHR0\ndM+ePdu2bWtvb9+xY8fhw4d/+OGHN27cqHdahvSv+8uLlJubm6ZbZWXlypUrhw0b5uHh4eDg\n4Ojo6OXl1b9//6effnrlypVFRUWGj0rrJ4bLly/PnTu3W7dudnZ2gwcP1vTZunXrvHnzwsLC\nfHx83Nzc7Ozs2rRp4+PjM3bs2K1bt9b9pFrjvHDhwqxZs7p27erg4ODl5TVjxow//vij8W/R\nOHHixJw5c3r37u3s7NyiRQt3d/fIyMgNGzbU++t5eXl5TEyMr6+vg4ODu7v7xIkTc3Nzm8lP\nsU24TDWMWj/Ly8tff/11zZzp1KnT+PHjT548qWPOmGO1kU4rMzPzzJkzEyZM6NChQ6tWrQYO\nHLhp0yZNt7KyspiYGG9vb826MXPmzEuXLuldZC+++KKOWbdhwwYT5pshM6Eh0lVIPHTk7+8v\ndqisrOzYsaNWB6GBn2IN3woauS0XFRXNmzeve/fumvVk0qRJ586d0/1JRYMHD5bO8wcffPDi\nxYt1u+Xk5Dz77LN79uxpaHZpbXErVqyQjnbJkiXioJKSEkdHR3HQiBEjxNfTp083sOx658Ol\nS5c0y7reHdTChQt1LK/c3FxxqIODw7Vr13RPujHzTcPw1cO0xW3aftXkqoza0Jo5gp1Z6Nhf\nSM9ZDgoKkg6qqqqaM2eO0IAuXbocOnTItP6GfHNXVFQMHDhQR7cdO3YYOCr1X7eZb775pnPn\nzuKf4jbTr18/HaN65JFHbt26Jf280nF+9tlndc9xad++/S+//NLIt9TU1Lz00ksN/Z4SGhqq\nCUOiy5cv9+nTR6tb69atk5OTpS2yBLumXabGrp9Xrlzp27evVjdHR8dvvvmmoTljjtVGOvSD\n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\npDeSkNL6yNJzXG7dulVcXFz3OglD3iL97jlx4sSJEyfqnXpNTc2VK1fc3d0vXrwoNnbr1q2h\n8ZtA75MnDNGEy9TY9U06Z7RmhfS3Th3Msdr4+vqKr6WnNPn6+opfb9ILHgVBqK6uNqTahjRy\nO613Jhhl1qxZH3/8sSAIv//+u6bFwcFB938dxm4FjVwo0iStdZ6Z3pkvPTXq0qVLlZWVTfiM\nBFtb24iIiKVLl4qh7fjx4+LcsLOze+yxx8TO48aNi4mJ0bxeu3at9P4yBjJwn/bkk0++9tpr\nN27cEARh/fr1y5Ytu3r1amZmpqZnQEBA3WsO6mrMfDN29dBqN2Rxm7BfbWRVjd/QmhWO2FlO\nixYt+vbtKz1KV1FRkZSUJGNJUt27d8/MzBw9enTdLby0tPSdd9559tlnTRuz9GojUVxcnPSb\noG/fvpMmTYqOjo6OjpZ+s6rrnCNVb7t4xykdTHiLDpWVlXXH2YTjbxLmW6aNoWOmSZljtbnj\njjvE19JDVtLvuUYmuaZV70wwSq9evbRubDFmzBitU8VNptkKGrlQpMVonfakl/Sy66qqql27\ndol/durUSfOzlHSXq0PPnj0/+eSTTz75ZOXKlV999dXOnTsvX778/fffi6lO+Ovhuurq6vbt\n24sPLRVTnSAIGRkZ+fn5Rn0QweAdlLOzs3g67LVr1zZv3vzdd9+J7zXwcF0TzjcdNKuHFkMW\nt1n3q/VW1fgNrVkh2Fla+/btpT/H/Pbbb5oXnTp1EhulZ8IKgnDx4kXpLxqa/zaM7W+Iu+++\ne9OmTdeuXfv555+/+OKLV199NSAgQBwaHx9v2m+y9f4vKH0w5dy5c48dO5aQkLBy5coPP/zQ\nkE337Nmz0j+lc6BFixYuLi6mvUU6V7UuOtOi+T9SvCWYUGcpaP0pl6Zapsaub9I5c+7cOWl/\ncZ3XzRyrjeU1cjttkuNPs2bN0vFnXcZuBTIuFK0HuS5evNjkXN65c+cZM2bMmDEjOjp64sSJ\nYWFhrq6u0g61tbUGZh21Wv31118bW4Dh+zTpEvziiy/E32Ht7e2ll0Dp0Jj5ZuzqYQIT9quN\nrEphD8Ml2FnayZMnpT9JiP+ySB/Y980330j7SG+bZGNjoznp29j+wl+vM5d+o2iIG7aTk9N9\n99331FNPxcXFHTx4UNxgKisrxV+LdI/KENIfnkJDQ8XX27dvv3Xrlt63f/HFF+J3Rm1t7Zdf\n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\n3kxPTx86dKhpk7t586aTk1O9g9avXz927FjTRgvTWE2wi4qK2rhx4/r162fMmFF36HvvvVde\nXr5q1SrLFwYAQLNSU1Njr1JdffllA/vbL1lSU1PTyIna29uPHz9eq/HOO+9s5GhhLKsJdg8/\n/PB7771X9zQ70cqVK318fIqKiixZFQAAEAShZcuW8fHxclcB6wl2bdq0ee6553R0UKlU8+fP\nt1g9AKxFUVGuIAjt27eXu5C/UKlU27dvDwgIkLsQwEIyMzPfeeedjIyMa9eutWvXLjQ0dMGC\nBT169NAMPXr0aEBAwJQpUxYsWPDSSy/99NNP1dXV999///Lly319ff/4449XX301NTX1+vXr\nQUFBy5cv79+/vzhmzZ1ujx079ueffzo4OPTr12/OnDljxoxpZElWymqCHQCY5tKlE4Ig3FPl\nJNjYyF3L/6jVqaWF+/btI9jhb2LVqlUzZsxwc3MbOXJkhw4d8vLyNmzYsHnz5rS0tHvuuUfs\n9vvvv99777133XXX+PHjT58+nZqaevTo0T179gwdOrRdu3aPPvro77//npKSMnz48LNnz4qP\nJ4iOjg4ODh46dGjHjh0vXbr0/fffP/7442+99dZLL73U+JKsDsEOwN/CvICpKpvmcoOnWnVt\n6p4lclcBNKUbN248+eST0pY+ffq8+OKLgiCcOnVq9uzZw4YN++6778TLLI4fPz5o0KBnnnnm\n2LFj4lt27dq1aNGi119/XfPn9OnTP//88+Dg4MmTJ7/33ns2NjaCIMTExMTGxn766acv/+8k\nwvz8/M6dO0srGTx48MKFC6dPn97Q7TIML8nqNJfdHAAAsF5VVVVr/mrHjh2aQR9//HFVVdVr\nr71WXl5+5X88PDzCwsKOHz+en58vjqRr167/+te/xD/FpPjmm2/a/O+Iu6bx6NGjYjdNqlOr\n1SUlJRcvXrx+/XpUVFRFRcXevXsbqtbwkqwOR+wAAEBjOTs7FxcX1zsoMzNTEITBgwfXO/TC\nhQtdu3bVvA4ICJDeuczT01MQhF69eklvp6JplN7aNjs7e+HChbt27SotLZWOubCwsKFqDS/J\n6hDsAACAGWluWLF169Z6b3fXs2dP8bXWrWrt7OwaahRvv3zkyJH777/f0dFx5syZ/fr1c3Z2\ntrW13blz57JlyyorKxtfktUh2AEAADPSJLNOnToNGDCgyUf+7rvvVlRUbN26NTw8XGw8fPiw\njCXJi3PsAACAGQ0cOFAQhMTERHOM/Ny5c+IkROnp6TKWJC+CHQAAMKM5c+bY2dmtWLFCK2+V\nlZUlJSU1cuTdu3cXBEG8UEMQhHXr1ukNdmYtSV78FAsAgNLUqtVv/fyz4Z3NWkzv3r0//fTT\n6Ojo8PDw4cOHBwQE1NTUnD59Oj09vVu3bk888URjRj5nzpx169aNGzfuiSee6Nq1a3Z2dmpq\n6pgxYzZs2CBXSfIi2AEAoCg+Pj7hw4fvNPjxr8OGD/fx8TFrSVOnTg0MDHz33Xd/+umnXbt2\ntWrVysPDY9KkSY2PUMHBwTt37nz99dc3b94sCEL//v23b99+4cIF3cHOrCXJi2AHAICidOvW\n7YcffrDY5BwdHdUGHPPz9/dPSEjQMbTuSLy8vOo22tnZaTUOGTJkz549Wt0mTpyoezx6S7JS\nnGMHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBCEOwAAAAUgmAH\nAACgEAQ7AAAAheCRYgCaWG1tzc2b1+Su4rbq6kq5SwAACyHYAWhKBw4cuHDhwFtv3SF3IXXp\nf5YlAFg7gh2ApnTjxg13lf1C/6fkLuS25Lwd31/Lk7sKALAEgh2AJuZgY+Pbxl3uKm67w9ZJ\n7hIAwEK4eAIAAEAhCHYAAAAKwU+xAAA0UxUVFTt37pS7CmirqqqSu4QGEewAAGiOOnbsePny\n5WHDhsldCOrRokULNzc3uauoB8EOAIDm6MEHH6ypqZG7ClgZzrEDAABQCIIdAACAQhDsAAAA\nFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJg\nBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAA\noBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAE\nOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAA\nAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg\n2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEA\nACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgE\nwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4A\nAEAhCHYAAAAKQbADAABQCDu5CzCaWq3Ozc3Nzc0tLi4WBMHFxcXX19fX19fGxkbu0gAAAORk\nTcGuoqJi2bJlK1euLCws1Brk5eUVHR394osvOjk5yVIbAACA7Kwm2JWXl4eFhWVlZalUqoCA\nAB8fHxcXF0EQiouLc3Nzjx8/HhMTk5KSkpaW1rJlS7mLBQAAkIHVBLu4uLisrKwJEyYsXbrU\nw8NDa2hhYeH8+fPXr18fFxcXGxsrS4UAAADysppgl5iYGBQUlJCQoFLVc8GHp6fn2rVrc3Jy\nkpKSCHYAmjm1IAiCsHDhwnfffVfmUv5q6dKljz76qNxVADCd1QS7goKCyMjIelOdhkqlCgkJ\nWblypSWrAgCTqAVBGO3qGu7vL3clty1IT8/NzZW7CgCNYjXBztnZOS8vT3efvLw8zYl3AND8\nBbm5jenZU+4qbnsvM1PuEgA0ltXcxy48PDw5OTkhIaGhDvHx8cnJyWFhYZasCgAAoPmwmiN2\nS5Ys2bZt25QpU5YvXx4REeHn5+fs7CwIQklJSU5OTmpq6tGjR11cXBYvXix3pQAAAPKwmmDn\n7e2dkZExbdq0AwcOZGdn1+0QHBy8evVqb29vy9cGAADQHFhNsBMEoXfv3llZWUeOHElPT8/J\nySkpKREEwdnZ2c/PLzQ0NDAwUO4CAQAA5GRNwU4jMDCQDAcAAFCX1Vw8AQAAAN0IdgAAAAph\nxcFu7969Dz30ULt27dq0aePv779s2bLq6mq5iwIAAJCN1Zxj16lTpyeeeOL999/X/Ll+/fqJ\nEyfW1tZq/jx27NixY8f27t373Xff2djYyFcmABjq999/37lzp9xV3FZSUnLp0iW5qwDQKFYT\n7C5evKi5DFYQhKKiomeeeUYQhAULFkydOtXFxeWnn36aPXv2li1b1q1bN2HCBFkrBQA91Gq1\nIAiXL5eerPhD7lpuKy0rP3XqlNxVAGgUqwl2Uhs3biwrK3vuueeWLFmiaYmKinJ3d7/33nvX\nrFlDsANgFVxcvPv2HCV3FbfZZrypSZwArJdVBrvjx48LgjB9+nRp48CBA/39/Y8ePWrUqC5d\nuvTss8/W1NTo6FNUVGRCkQAAABZmlcGuoqJCEIQ777xTq7179+6//vqrUaNycnLy9vbWfdWF\ng4ODsRUCAABYnlUGu7vuuksQhOvXrzs5OUnbr127pnmArOHatGkTGxuru8++ffvWrl1rbJEA\nAAAWZk3B7quvvkpMTBQEQXMx7C+//NKxY0dph7Nnz3bu3Fme4gAAAORmNcHOz89Pq+XAgQNh\nYWHin0eOHMnPz3/wwQctWxcAAEBzYTXB7vTp07o71NTUvP3229KoBwAA8LdiNcFOrwEDBgwY\nMEDuKgAAAGRjxY8UAwAAgBTBDgAAQCEUFezmzZvXrVs3uasAAACQh6KC3ZUrV/Lz8+WuAgAA\nQB6KCnYAAAB/Z1ZzVezYsWP19snKyrJAJQAAAM2T1QS7pKQkuUsAAABo1qwm2LVq1crT03PZ\nsmU6+ixfvjwtLc1iJQEAADQrVhPs+vbt++uvv44YMcLGxqahPhs3brRkSQAAAM2K1Vw8ERgY\neP369bNnz8pdCAAAQDNlNUfsQkND9+/fX1BQ4O3t3VCfyMhILy8vS1YFAADQfFhNsBs9evTo\n0aMb3wcAAECprOanWAAAAOhGsAMAAFAIgh0AAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAA\nKATBDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATB\nDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBCEOwAAAAUgmAHAACgEHZyFwDAdHPnzv3666/lruIv\nysrK3GvVclcBAH9TBDvAip07d87dPTwo6Bm5C7lty5Yn1aUX5a4CAP6mCHaAdXNx6dq9e7jc\nVdxmZ9dS7hIA4O+Lc+wAAAAUgmAHAACgEPwUCwAQBEGoFtRFRUU7d+6Uu5C/8PX17dKli9xV\nAFaDYAcAEARBuFJbfenIkccffljuQm6rqK6OGDnyu+++k7sQwGoQ7AAAgiAIakF4xNU1ae5c\nuQu5bf6OHaerq+WuArAmnGMHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAI\ngh0AAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0A\nAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBC\nEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBCEOwA\nAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0AAIBCEOwAAAAU\nQn+wu3btmgXqAAAAQCPpD3aenp5PPvlkZmamBaoBAACAyfQHOy8vrzVr1tx33339+vX7+OOP\nr1+/boGyAAAAYCz9wS4nJ2fnzp2PP/746dOnZ8+e7eHh8fTTTx86dMgCxQEAAMBw+oOdjY1N\nWFhYUlLS+fPn//Of/3Tq1Gn16tUDBgwICgr67LPPysrKLFAlAAAA9DLiqtgOHTq8/PLL//3v\nf7dv3/7oo4+eOHEiOjraw8Nj5syZv/zyi/lKBAAAgCGMvt2JjY2Nr6/v3Xff7erqKghCaWnp\nypUr+/btO27cuJKSEjNUCAAAAIMYEexqamq2bt06YsSI7t27x8bGOjg4LF68uKCgYNu2bYMH\nD05MTJw9e7b5CgUAAIBudoZ0On/+/OrVqz///PPCwkIbG5vw8PBZs2Y9/PDDtra2giB4enpG\nRESMGjVq27ZtZq4WAAAADdIf7B5++OHU1NSampo77rjjhRdemDlz5l133aXVx8bGZuDAgcnJ\nyeYpEgAAAPrpD3bff//9gAEDZs2aNXbsWEdHx4a6RUREtG3btklrAwAAgBH0B7tDhw4FBQXp\n7RYYGBgYGNgUJQEAAMAU+i+eMCTVAQAAQHb6g90333wzdOjQwsJCrfaCgoIhQ4Zs2rTJPIUB\nAADAOPqD3apVq0pLSz09PbXavby8iouLV61aZZ7CAAAAYBz9we7EiRP9+/evd1D//v1PnDjR\n1CUBAADAFPqD3dWrV93c3Ood1KFDhytXrjR1SQAAADCF/mDn5ub23//+t95BZ86ccXFxaeqS\nAAAAYAr9we7+++/funXr6dOntdpPnTq1devWQYMGmacwAAAAGEd/sHvhhReqqqoGDRq0YsWK\nM2fOVFRUnDlzZsWKFffff39VVdW8efMsUCUAAAD00n+D4nvvvfejjz6aM2fOP//5T2m7ra3t\nRx99dN9995mtNgAAABhBf7ATBGHGjBn33Xffxx9/nJWVVVxc7OLiMnDgwFmzZvXp08fc9QEA\nAMBABgU7QRD69u27cuVKs5YCAACAxtB/jh0AAACsAsEOAABAIQwKdrt3746MjOzUqZODg4Nd\nHeYuEQAAAIbQH8uSk5MfeeSR2tpaZ2dnHx8fkhwAAEDzpD+lLVq0yMbG5uuvvx43bpyNjY0F\nagIAAIAJ9Ae7X375JSoqavz48RaoBgAAACbTf45dq1atOnToYIFSAAAA0Bj6g114ePiBAwcs\nUAoAAAAaQ3+wW7p06fnz5xctWlRTU2OBggAAAGAa/efYvfHGG7169Vq4cOGXX37p7+/v4uKi\n1SE+Pt4spQEAAMAY+oPdmjVrNC/y8/Pz8/PrdiDYAQAANAf6g112drYF6gAAAEAj6Q92/v7+\nFqgDAAAAjWTEYyTy8/MvXLjQs2dPZ2dn8xWkl1qtzs3Nzc3NLS4uFgTBxcXF19fX19eXmycD\nAIC/OYOeFbt///5+/fp169btvvvuO3jwoKYxMTGxd+/eu3fvNmd5f1FRUREbG9u5c+cePXpE\nRkZOnjx58uTJkZGRPXr06NKlS2xsbEVFhcWKAQAAaG70H7E7depUeHi4jY3NqFGjtmzZIraP\nHDly2rRpGzZsGDx4sDkr/H/l5eVhYWFZWVkqlSogIMDHx0dzfW5xcXFubu7x48djYmJSUlLS\n0tJatmxpgXoAAACaG/3BLjY2tqqq6tChQ+7u7tJg17p169DQ0IyMDHOWd1tcXFxWVtaECROW\nLl3q4eGhNbSwsHD+/Pnr16+Pi4uLjY21TEkAAADNiv6fYtPS0qKiovr06VN3UI8ePQoKCsxQ\nVT0SExODgoISEhLqpjpBEDw9PdeuXRsYGJiUlGSZegAAAJob/cGuqKioW7du9Q6ytbUtLS1t\n4ooaUFBQEBISolI1WLBKpQoJCTl//rxl6gEAAGhu9Ac7V1fXy5cv1zsoOzvb3d29qUuqn7Oz\nc15enu4+eXl5dR+MAQAA8DehP9gNGjQoJSWlsrJSqz09PX3Hjh1DhgwxS111hIeHJycnJyQk\nNNQhPj4+OTk5LCzMMvUAAAA0N/ovnpg3b94//vGPqKioV155RRCEioqKgwcPrl+//sMPP7Sz\ns3vhhRfMX6QgCMKSJUu2bds2ZcqU5cuXR0RE+Pn5aW6nV1JSkpOTk5qaevToURcXl8WLF1um\nHgAAgOZGf7AbNGjQRx99NHfu3NTUVEEQIiMjNe329vaff/553759zVvg/3h7e2dkZEybNu3A\ngQP1PuUsODh49erV3t7elqkHAACguTHoyRMzZswICQlZuXJlZmZmUVGRs7PzwIED586d26tX\nL3PXJ9W7d++srKwjR46kp6fn5OSUlJQIguDs7Ozn5xcaGhoYGGjJYgAAAJobQx8p1qtXrxUr\nVpi1FAMFBgaS4QAAAOoy6JFiAAAAaP4MPWLXfKjV6tzc3Nzc3OLiYkEQXFxcfH19fX19bWxs\n5C4NAABATvqD3V133aW7w5kzZ5qoGD0qKiqWLVu2cuXKwsJCrUFeXl7R0dEvvviik5OTZYoB\nAABobvQHuytXrmi1lJeXV1dXC4LQtm1bix0nKy8vDwsLy8rKUqlUAQEBPj4+mnsRFxcX5+bm\nHj9+PCYmJiUlJS0trWXLlpYpCQAAoFnRH+w0v3hKVVVVZWdnP/fcc+3atdu0aZN5CtMWFxeX\nlZU1YcKEpUuX1n1cbGFh4fz589evXx8XFxcbG2uZkgAAAJoVUy6esLe3Dw4OTklJOXToUFxc\nXJPXVK/ExMSgoKCEhIS6qU4QBE9Pz7Vr1wYGBiYlJVmmHgAAgObG9IsnXF1dw8PD16xZ88Yb\nbzRhQQ0pKCiIjIxUqRpMoiqVSnOzPaNGe+HChTFjxtR9YJpUWVmZIAhqtdqoMUN5Jk6cePr0\nabmr+IszZ8506tRe7ioAAM1Fo66KdXBwqHsdg5k4Ozvn5eXp7pOXl6c58c5wrq6ujz322K1b\nt3T0yc/Pz8nJ4apbbNu2rXPnkR06WPS+3LpVVMSWlpbJXQUAoLkwPdj9+eefycnJnp6eTViN\nDuHh4UlJSQkJCZMnT663Q3x8fHJy8rhx44warZOT0/PPP6+7z759+z755BOjRguluvvuqB49\nouSu4rbMzPfkLgEA0IzoD3YLFy7Uaqmurj5//vzmzZuvX7++ePFis9RVx5IlS7Zt2zZlypTl\ny5dHRET4+fk5OzsLglBSUpKTk5Oamnr06FEXFxeL1QMAANDc6A92ixYtqrfdyclp3rx5//rX\nv5q6pPp5e3tnZGRMmzbtwIED2dnZdTsEBwevXr3a29vbMvUAAAA0N/qDXXJyslaLSqVydXXt\n06dP69atzVNV/Xr37p2VlXXkyJH09PScnJySkhJBEJydnf38/EJDQ3mALAA0Uk1t7bVr1+Su\n4rabN2/W1tbKXQVgTfQHu5EjR1qgDsMFBgaS4QCg6anVxcXFH3zwgdx13HZEEM7Vd4srAA2x\nvmfFAgDMQS0Idnat7wmaKncht+37JammpkbuKgBrQrADrJhaXVNZefHs2Z1yF3JbdfUNgZs+\nWi0bG5Wjo6vcVdxmo7IVBIIdYAT9wa5bt26Gj+7cuXMml9J48+bN27hxo7w1AJZUWVl648ae\nr74aJnchf+EscNNHAJCH/mBXVlZWU1MjPjG2VatW5eXlmtcuLi62trZmrM5IV65cyc/Pl7sK\nwKKGtHB74945cldx28x9S8urbspdBQD8Tel/Vuy5c+d69+4dGBiYkpJSWlpaVlZWWlqakpIS\nEBDQu3fvc+fOXZGwQMUAAACol/4jdjExMRcuXDhx4kTLli01La1bt37ooYeGDBnSp0+fmJiY\n996zxL3vx44dq7dPVlaWBSoBAABonvQHuw0bNowbN05MdaKWLVuOHj06MTHRMsEuKSnJAlMB\nAACwXvqD3eXLl9UNXOOmVqsvX77c1CXVr1WrVp6ensuWLdPRZ/ny5WlpaZapBwAAoLkx6KrY\nTZs2LVq0qFWrVtL28vLyTZs23XnnnWar7S/69u3766+/jhgxwsamwQvuNm7caJliAAAAmiH9\nF0/MmDHj3LlzgwYN2rx589WrVwVBuHr16ubNmwcNGnTu3Lno6GjzFykIghAYGHj9+vWzZ89a\nZnIAAABWR/8Ru2efffbUqVOrVq2KiooSBMHOzq66uloz6JlnnvnnP/9p3gL/JzQ0dP/+/QUF\nBd7e3g31iYyM9PLyskw9AAAAzY3+YKdSqT777LNx48atWbMmOzu7pKTE2dk5ICDgySefHDJk\niPkr/H+jR48ePXp04/sAAAAolaGPFBs6dOjQoUPNWgoAAAAaQ/85dqL8/PzMzMySkhLzVQMA\nAACTGRTs9u/f369fv27dut13330HDx7UNCYmJvbu3Xv37t3mLA8AAACG0h/sTp06FR4efvbs\n2VGjRknbR44cmZeXt2HDBrPVBgAAACPoP8cuNja2qqrq0KFD7u7uW7ZsEdtbt24dGhqakZFh\nzvIAAABgKP1H7NLS0qKiovr06VN3UI8ePQoKCsxQFQAAAIymP9gVFRV169at3kG2tralpaVN\nXBEAAABMoj/Yubq6NvRA2OzsbHd396YuCQAAAKbQH+wGDRqUkpJSWVmp1Z6enr5jxw5L3qMY\nAAAAOugPdvPmzbt8+XJUVNTJkycFQaioqDh48OALL7wQERFhZ2f3wgsvunTLsgAAIABJREFU\nmL9IAAAA6Kf/qthBgwZ99NFHc+fOTU1NFQQhMjJS025vb//555/37dvXvAUCAADAMAY9UmzG\njBkhISErV67MzMwsKipydnYeOHDg3Llze/XqZe76AAAAYCD9wW7//v2Ojo7+/v4rVqywQEEA\nAAAwjf5z7O67777Y2FgLlAIAAIDG0B/s3NzcWrZsaYFSAAAA0Bj6g92QIUMOHDhQU1NjgWoA\nAABgMv3BLi4u7sqVK88999yNGzcsUBAAAABMo//iiX//+999+/b98MMPExMT/f39PTw8bGxs\npB3i4+PNVR0AAAAMpj/YrVmzRvPiypUrO3furNuBYAcAANAc6A922dnZFqgDAAAAjaQ/2Pn7\n+1ugDgAAADRSgxdPJCYmZmVlWbIUAAAANEaDwW7cuHGffPKJ+OeyZcsiIiIsUhIAAABMof92\nJxonTpz48ccfzVoKAAAAGsPQYAcAAIBmjmAHAACgEAQ7AAAAhSDYAQAAKISu+9itW7du8+bN\nmteaB8W6uLjU7VZcXGyOygAAAGAUXcGuqqqqpKRE2qL1JwAAAJqPBoNdRUWFJesAAABAIzUY\n7BwdHS1ZBwAAABqJiycAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMA\nAFAIgh0AAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAI\ngh0AAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKATBDgAAQCEIdgAAAApBsAMAAFAIgh0A\nAIBCEOwAAAAUgmAHAACgEAQ7AAAAhSDYAQAAKISd3AUAAFC/W+ramzdvbtiwQe5C/qJLly73\n3HOP3FUA9SPYAQCaqXO3yspulUVPnix3IbdV1dY6tm17+fJluQsB6kewAwA0U2pB8LW1Pfny\ny3IXctt3p09P275d7iqABhHsAEPdunXr1Knviopy5S7kNrW6Rq2ukbsKAEBzQbADDHXjxo2L\np7+7mbdT7kIkaqtrbSrlLgIA0FwQ7AAjTO7Y76Hu4XJXcdvDuxfLXQIAoBnhdicAAAAKQbAD\nAABQCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQ\nCIIdAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIId\nAACAQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACA\nQhDsAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDs\nAAAAFIJgBwAAoBAEOwAAAIUg2AEAACgEwQ4AAEAhCHYAAAAKQbADAABQCIIdAACAQhDsAAAA\nFIJgBwAAoBAEOwAAAIWwk7sAo6nV6tzc3Nzc3OLiYkEQXFxcfH19fX19bWxs5C4NAABATtYU\n7CoqKpYtW7Zy5crCwkKtQV5eXtHR0S+++KKTk5MstQEAAMjOaoJdeXl5WFhYVlaWSqUKCAjw\n8fFxcXERBKG4uDg3N/f48eMxMTEpKSlpaWktW7aUu1gAAAAZWE2wi4uLy8rKmjBhwtKlSz08\nPLSGFhYWzp8/f/369XFxcbGxsbJUCAAAIC+ruXgiMTExKCgoISGhbqoTBMHT03Pt2rWBgYFJ\nSUmWrw0AAKA5sJpgV1BQEBISolI1WLBKpQoJCTl//rwlqwIAAGg+rCbYOTs75+Xl6e6Tl5en\nOfEOAADgb8hqgl14eHhycnJCQkJDHeLj45OTk8PCwixZFQAAQPNhNRdPLFmyZNu2bVOmTFm+\nfHlERISfn5+zs7MgCCUlJTk5OampqUePHnVxcVm8eLHclQIAAMjDaoKdt7d3RkbGtGnTDhw4\nkJ2dXbdDcHDw6tWrvb29LV8bAABAc2A1wU4QhN69e2dlZR05ciQ9PT0nJ6ekpEQQBGdnZz8/\nv9DQ0MDAQLkLBAAAkJM1BTuNwMDAJsxwv//++/Dhw6uqqnT0uXnzpiAIarW6qSYKAABgDtYX\n7JqWu7v7a6+9poluDfntt9+WLl3Ks2gBAEAz93cPdvb29pMnT9bdZ9++fUuXLrVMPQAAACaz\nmtud1LV3796HHnqoXbt2bdq08ff3X7ZsWXV1tdxFAQAAyMZqgl2nTp2effZZ8c/169cPGTIk\nNTW1qKiorKzs2LFj8+bNe+yxxzgTDgAA/G1ZTbC7ePGi5jJYQRCKioqeeeYZQRAWLFhw9uzZ\nq1evfvvtt+7u7lu2bFm3bp2sZQIA/q+9e4+Kqlz8P/7McBMlIS+BCCKSYKIeAW+VrVTw0ldJ\nq2OppGLosjpWlqvV8oLFyahTh+isTv4UNTILNUsIyyui5VILA8HMAEPwmigiGDe5zP79MesA\ngiL3Z+bh/forn3n28NlP4/Yzm71nAEhjNsWutq+//rqoqOjll19+++233d3d77333ieeeGL7\n9u1CiI0bN8pOBwAAIIdZFrsTJ04IIRYsWFB7cNSoUUOHDk1NTZUUCgAAQDKzLHalpaVCCHd3\n9zrj/fr1KygokJEIAABAPrMsdvfff78Q4saNG3XGr1+/bvwCWQAAgA7InD7HbtOmTVu2bBFC\nGAwGIcTJkycdHR1rTzhz5oyrq6uccAAAALKZTbHz8vKqM5KUlOTv71/9x5SUlLNnzz722GPt\nmwsAAMBUmE2xS09Pb3hCVVXVBx98ULvqAQAAdChmU+zuavjw4cOHD5edAgAAQBqzvHkCAAAA\n9VHsAAAAFEGxAwAAUATFDgAAQBEUOwAAAEVQ7AAAABRBsQMAAFAExQ4AAEARFDsAAABFUOwA\nAAAUQbEDAABQhDrfFQsAUI2maZp26tQp2TlqnL94sbKyUnYK4I4odgAAE1VlKDcYDLGxO2QH\nqfGbobJIq5KdArgjih0AwJTpH374DdkZahSeSRAXjshOAdwR19gBAAAogmIHAACgCIodAACA\nIrjGDqaoqKjopZdeKi4ulh3kFpqmVVbdlJ0CAIA7otjBFJ07d+6zzz6bPWSIrZWV7Cy3KC8v\nkh0BAIA7otjBdP17woT7unSRnaLGuuRk2REAAGgIxQ6mqKCgQAixadOme/SmdRloVSWfXwUA\nMF0UO5iia9euCSGsrPrZWpvQGTsh/qwyUOwAAKaLYgfT1auXT8/OPWWnqOVMguwEAAA0xLR+\nzwUAAIBmo9gBAAAogmIHAACgCIodAACAIih2AAAAiqDYAQAAKIJiBwAAoAiKHQAAgCIodgAA\nAIqg2AEAACiCYgcAAKAIih0AAIAiKHYAAACKoNgBAAAogmIHAACgCIodAACAIih2AAAAiqDY\nAQAAKIJiBwAAoAiKHQAAgCIodgAAAIqg2AEAACiCYgcAAKAIih0AAIAiKHYAAACKoNgBAAAo\ngmIHAACgCIodAACAIih2AAAAiqDYAQAAKIJiBwAAoAhL2QEAADAb+ZWlmqaNHz9edpBb2NjY\nfPHFFw4ODrKDQD6KHQAAjXWtosRKiADZMWorKi9flZBw6dIlih0ExQ4AgCaxFOKNhx+WnaLG\nleLiVT/+KDsFTAXX2AEAACiCYgcAAKAIih0AAIAiKHYAAACKoNgBAAAogmIHAACgCIodAACA\nIih2AAAAiqDYAQAAKIJiBwAAoAiKHQAAgCL4rliI7OzstWvXyk5xiz/++EMIoWmycwAAYFYo\ndhD79++PjPzk/vsfkx2kRn7+GSFEZWWF7CAAAJgTih2Epml2dr2mT/9KdpAax46t3rnzH7JT\nAABgZrjGDgAAQBEUOwAAAEVQ7AAAABRBsQMAAFAExQ4AAEARFDsAAABFUOwAAAAUQbEDAABQ\nBMUOAABAERQ7AAAARVDsAAAAFEGxAwAAUATFDgAAQBEUOwAAAEVQ7AAAABRBsQMAAFAExQ4A\nAEARFDsAAABFUOwAAAAUQbEDAABQBMUOAABAERQ7AAAARVDsAAAAFEGxAwDAjBVXVAghvL29\ndaZEr9d/++23stemI7KUHQAAADRfaUWFECJy7NhBLi6ys9QIjou7cuWK7BQdEcUOAACzN8zJ\naXS/frJT1OhsZSU7QgfFr2IBAAAUQbEDAABQBL+KhSgrKysvLzp1apvsIDX+/DNFdgQAAMwP\nxQ4iOTm5uOjP3bFzZAepUWGoFEJUVd2UHQQAAHNCsYMwGAzddRbbHn5DdpAae3IOvHf2R03T\nZAcBAMCccI0dAACAIih2AAAAiqDYAQAAKIJr7NpbbGzs5s2bZae4RVJSkia4mg0A7q7KUCGE\n2LbNhD5G4MLNm0KIyooK2UFgEih27S0+Pj4xMa1v3zGyg9TIyyvtxG0KANAIlZVlQojr121l\nB6lRUF4phCgpKZEdBCaBYieBq+tDU6aslZ2iRm7uidLiq7JTAIDZ8PScIjtCDX3hOXEtU3YK\nmAqusQMAAFAExQ4AAEARFDsAAABFUOwAAAAUQbEDAABQBMUOAABAERQ7AAAARVDsAAAAFEGx\nAwAAUATFDgAAQBEUOwAAAEXwXbEAAJi9rKysw+XlslPUyC8ujouLy8/Plx3kFgEBAX5+frJT\ntC2KHQAAZqyy8qYQIjv7UvnFG7Kz1Ci4efNYQkLu8eOyg9TIKShIT0+Pjo6WHaRtUewAADBr\nmhCiV6+Rfn0flp2klh/C/n7ffatDQmTnqDHv229lR2gPFLvG+sc//qHXt8IliUeOHKmsdG35\n8wAAANRhfsVO07TMzMzMzMyCggIhhIODg6enp6enp06na7sf6iOELiVFtMaPKDp7tqyLoeXP\nAwAAUIc5FbvS0tKIiIg1a9ZcvHixzkMuLi4LFy5csmSJra1tW/xoFyH+3//9n4WFRcufyj87\nO7XlzwIAAFCP2RS74uJif3//n3/+Wa/X+/j49O/f38HBQQhRUFCQmZl54sSJ0NDQ77//fv/+\n/Z07d5YdtiGXbt68cfN8VNQw2UFq5OWld5WdAQCgmCu5uVFRUbJT1MgsKBCm3RBahdkUu/Dw\n8J9//jkoKOj99993dnau8+jFixdff/31zZs3h4eHr1q1SkrCRiqsrHQ0VE22vVd2kBq7NUOx\n0GSnAAAoRdNsbG29ZaeoUZF3+PqVK7JTtDmzKXZbtmzx8/P7/PPPb3sHQ+/evb/44ouMjIyt\nW7eaeLETQvTSWcx0NaF7l9IuJf9RWSo7BQBAKZaWnV1N6R87yz9TZEdoDzpNM49TNTY2Ni++\n+GJkZGQDcxYvXrxmzZqysrLGP212dvbIkSMrKysbmFNZWdnzr7+ud+rU+KdtQGFZmU4Ia9GG\nt3o0VbnQDEJ0MqVIVUIrF6KTEDpTSlUqNGshLEwpUpnQLISwMqVI5ULThLAxpUiVQqsQwtaU\nIgkhSoVmI4TelFKVCs1KCEtTinRTaKZ2wKwQWqWJvZwMQrspBC+nuyoXmoenZ0ZGhuwgbcts\nztjZ29tnZ2c3PCc7O9t44V3jubm5ffXVVw0XO03TUlNTfXx8mvTMd5KVlXXhwoV77rmnVZ6t\nVZSUlJw7d27AgAGyg9zi+PHjrbXmreXkyZOenp7W1tayg9TIycmxs7Pr0aOH7CA1CgoK8vLy\n7r//ftlBahgMhpMnTw4ZMkR2kFukpaUNGTKkTW/nb6o//vijZ8+e9vb2soPUuHr1aklJiZub\nm+wgNcrLyzMzMwcNGiQ7yC1SU1OHDh0qO8Ut0tPT+/TpY2pXvU+YMEF2hDZnNmfsZs2atXXr\n1ujo6Dlz5tx2wmefffbcc8/NnDnzyy+/bOdsAAAApsBsil1WVpafn19hYaGPj8+kSZO8vLyM\nbysLCwszMjJ27dqVmprq4ODwyy+/eHh4yA4LAAAggdkUOyHEyZMnQ0JCkpKSbvvoiBEjNmzY\nYGqnxwEAANqNORU7o5SUlMTExIyMjMLCQiGEvb29l5fXuHHjfH19ZUcDAACQyfyKHQAAAG6r\nFb7VHgAAAKaAYgcAAKAIih0AAIAiKHYAAACKoNgBAAAogmIHAACgCIodAACAIih2AAAAiqDY\nAQAAKIJiBwAAoAiKHQAAgCIodgAAAIqg2AEAACiCYgcAAKAIih0AAIAiKHYAAACKsJQdAPKF\nhoauWrVKdgoAANrWqFGjjh49KjtF26LYQfTu3btPnz7bt2+XHcTUjRs3LjQ0dOzYsbKDmLTo\n6OhDhw59+umnsoOYNIPBMGLEiKioKF9fX9lZTNp//vOfnJycyMhI2UFMWn5+/oQJE7766qt+\n/frJzmLSwsLC7rnnHtkp2hzFDsLCwsLGxsbPz092EFNnYWHh4eHBQjVs7969Xbp0YZUaZjAY\nhBBeXl4sVMMcHR2vX7/OKjXsypUrQghvb++BAwfKzmLSunfvLjtCe+AaOwAAAEVQ7AAAABRB\nsQMAAFAExQ4AAEARFDsAAABFUOwAAAAUQbEDAABQBMUOAABAERQ7AAAARfDNExDW1tbW1tay\nU5gBFqoxWKXG0Ol0VlZWLNRd8XJqDCsrK51Ox0LdVQdZIp2mabIzQLKKiorLly+7urrKDmLq\nzp496+LiYmFhITuISSstLS0oKOjVq5fsIKYuOzu7b9++Op1OdhCT9tdff5WVlfXs2VN2EFN3\n5swZvij2rq5fvy6EuPfee2UHaVsUOwAAAEVwjR0AAIAiKHYAAACKoNgBAAAogmIHAACgCIod\nAACAIih2AAAAiqDYAQAAKIJiBwAAoAiKHQAAgCIodgAAAIqg2AEAACiCYgcAAKAIih0AAIAi\nKHYAAACKoNgBAAAogmLXUezYsUOn0+l0uhUrVjRmflZWVlBQkJOTU6dOnfr3779ixYqSkpK2\nDmkKGr9QRUVFW7dunTFjhpubm7W1tb29/ejRo9evX28wGNonqkRNfTm1fEMz1Yz93b9//7Rp\n0xwdHW1sbFxdXadOnXrw4MG2zChfk1ZJ07TY2Fh/f38XFxdbW9t+/fpNnz796NGj7ZBTigED\nBujqcXJyasy2Hecw3rxVUvUYbik7ANrD1atXFyxYYGdnV1RU1Jj5J0+efOSRRwoLCwMDA93d\n3Q8dOvTOO+/s378/MTHR1ta2rdNK1KSFWr9+/auvvmptbe3r6zty5Mjc3NwjR44cPnx4x44d\nsbGxer2y75qa+nJq+YZmqhn7u3Tp0vfee8/GxmbUqFGOjo5Xr149fPjw4MGDx4wZ05ZJZWrq\nKi1atGj16tX29vaBgYHdu3fPzMzcvn37N998Ex0dPXfu3LZOK4Ver589e3btEXt7+7tu1dEO\n481YJWWP4Ro6gGnTpvXq1Ss0NFQIsXz58rvOHzFihBAiOjra+MeqqqqZM2cKId5+++22DSpb\nkxbq66+/Xr16dUFBQfXIb7/9dt999wkhYmJi2jipTE19ObV8QzPV1P399NNPhRAPPvjghQsX\nqgerqqry8vLaMqZkTVqlrKwsIUSPHj0uXrxYPRgXFyeEcHV1beOkcnh5ednY2DRjww51GG/e\nKql6DDfbQopGi46OjouLW7duXbdu3RozPyUlJSkpaejQocHBwcYRvV7/wQcf6PX6tWvXaprW\nhlmlaupCPfXUUy+88ELtN4UDBw589dVXhRA//PBDW6WUramr1PINzVRT97e8vHzZsmVdunSJ\njY3t3bt39bher+/evXubxZSsqauUnZ0thBgxYoSzs3P1YGBgoKWlZV5eXlulNEMd9jDeJKoe\nwyl2isvJyXnllVfmzZs3efLkRm6SmJgohHjsscdqD/bu3XvIkCEXLlzIzMxs/ZQmoBkLdVvG\nY4SNjU0r5TItzV6l1lpec9G8v3eXL1+eNm2avb391q1bQ0NDw8PD9+/fr/C/wc1YpQEDBlhY\nWBw7duzy5cvVgzt37qysrJw4cWLbxJTPYDCEh4eHhIQsWrQoKioqPz//rpt0wMN4M1bpthQ4\nhnONncoMBsPcuXMdHBwiIyMbv1VGRoYQwsvLq864p6dnampqZmZm/YfMXfMWqj5N0z7//HMh\nRGBgYCtFMyHNXqXWWl5z0bz9PXbsmBCie/fuQ4YMOX36dPX4gw8+GBsb6+jo2PpBpWreKvXu\n3TssLGzFihUPPPCA8Rq706dP79mzZ/LkyevWrWu7tHJVVFQsX768+o9LliyJiooy/l71Tjrg\nYbwZq1SfGsdwztipLCIi4scff9ywYUNjrrStVlhYKG532amDg4MQoqCgoBUTmojmLVR9YWFh\nP/3005NPPhkQENBa2UxHs1eptZbXXDRvf69cuSKE+OSTT/R6/YEDB/76668TJ06MHz/+6NGj\nM2bMaLOw0jT7VbF8+fKYmBiDwbBp06aPPvro+++/9/DwCAoK6tGjRxtFlWvu3Ln79u37888/\nS0pKTp48uWjRopKSktmzZx86dKiBrTraYbx5q1SfGsdwip2yfv3119DQ0Oeff378+PGys5i0\n1lqo//73v2FhYb6+vtHR0a2VzXQ0e5U62uuw2ftr/IQFnU4XFxc3ZswYOzu7wYMHx8bGOjs7\nHzx48JdffmmbvHK05FURFhYWFBT0/PPPZ2dnFxcXJycnu7m5zZo1a9myZW0RVbqlS5cGBAQ4\nOTnZ2tp6e3t//PHHS5curaqqevfdd2VHMyGtskrKHMMpdmrSNG327NnOzs4ffPBBU7c1vskz\nvuGrzfgmz/iGTxktWajaIiIiXnrpJT8/v4SEhK5du7ZWPBPR7FVqreU1Fy3ZX+PfrAEDBgwY\nMKB6sEuXLsbqo1Kxa8kq7d2796233poxY8a//vWvvn37du7c2dfXNy4uztXV9f333z979mxb\nBDY1ISEhQoikpKQG5nSow/htNWaValPqGC7pbly0rYqKiob/v4eEhNxpW+PRdunSpXXGfXx8\nhBDp6eltnL1dtWShqr355ptCiAcffLD2bfMqafYqtcrympGW7O/GjRuFEKNHj64z/sorrwgh\nIiMj2zh7+2nJKr388stCiKioqDrj06dPF0LExcW1cXaTYLwtwM7OroE5HeowfluNWaVqih3D\nuXlCTXq93vh+pbbffvvtp59+Gjp0qJ+f3yOPPHKnbceNGyeE2L17d3h4ePXgpUuX0tLSXFxc\nPD092yizFC1ZKKPXXnstMjJyzJgxO3bssLOza7OkMjV7lVq+vOalhX/vdDpdenp6RUWFlZVV\n9fivv/4qhHB3d2+jzO2vJatUXl4u/nc9Ym25ubnCzO9kbDzjJ3F4eHg0MKdDHcZvqzGrZKTg\nMVx2s0T7Md59Vv8jQKOjoyMjI3Nzc6tHjJ9suXHjRuMfq6qqgoKChKKfbFlfIxeqqqpqwYIF\nQoiJEyeWlJS0e0zJGv9yauSGqmr8Qj355JNCiDfffLN6JD4+XgjRo0ePoqKi9kkrSyNX6csv\nvxRCODk5nT9/vnpOfHy8Tqfr3Lnz9evX2y9xu0hKSkpLS6s9cuzYMeNn+P373/+uPd6RD+PN\nXiVVj+GcsYNYtWpVVlbW6NGjjZ+4LYTYsGHD6NGj582bt337duN30SQnJ48cOXLJkiVyo8pV\nZ6EiIiLWrVun1+u7dev2wgsv1J45ePDgDrtW9V9OuK36C/Xxxx+npKSEhYXt3bvX19c3Jydn\n165dVlZW69ev79Kli9y0stRZpWeeeWb9+vUHDhwYMGDAlClTHB0df//993379gkhIiIi1Lt0\n7Icffnj99dc9PDzc3d27du2anZ2dmpqqadrjjz9u/K10tY58GG/2Kql6DKfY4TYGDRqUnJwc\nGhqakJCwa9cuFxeXZcuWLVu2TMlvGGy2a9euCSEMBsPmzZvrPDRx4kTzPShAFmdn52PHjv3z\nn/+Mj4//5ZdfunbtOnXq1GXLlg0bNkx2NFNhYWGxe/fuTz75ZMuWLd9//31paWm3bt0CAwMX\nL15s/OWjYvz9/RcsWPDTTz+lpKTcuHHDwcEhICBgzpw5QUFBOp2u4W07zmG82auk6jFcp6n7\nseYAAAAdCh93AgAAoAiKHQAAgCIodgAAAIqg2AEAACiCYgcAAKAIih0AAIAiKHYAAACKoNgB\nAAAogmIHAACgCIodAACAIih2AAAAiqDYAQAAKIJiBwAAoAiKHQAAgCIodgAAAIqg2AEAACiC\nYgcAAKAIih0AAIAiKHYAAACKoNgBAAAogmIHAACgCIodAACAIih2AAAAiqDYAQAAKIJiBwAA\noAiKHQAAgCIodgAAAIqg2AEAACiCYgcAAKAIih0AAIAiKHYAAACKoNgBAAAogmIHAACgCIod\nANNVVlam0+l0Op2FhcWFCxfqT/D29jZO+O6779o/XsMyMjJeffVVHx+fbt26WVlZde/e/aGH\nHlq+fHlmZmbtadX7WL2nPXr08Pf3j4mJqf+c77zzjnFaRkZGe+0HAHNCsQNg6iwtLQ0GQ3R0\ndJ3xw4cPnzp1ytLSUkqqBmiaFhYWNnDgwI8++qigoGDcuHFz58719/fPz88PDw9/4IEHPv/8\n8zqbWFtbL1y4cOHChcHBwd7e3omJiUFBQa+99lqdp12/fr1OpxNCrFu3rv32B4D50GmaJjsD\nANxeWVmZra2tm5ubg4NDYWHhmTNnjLXGaN68eV9++eX48eN37ty5Y8eOKVOmSIxaW1hY2Ftv\nveXs7Lxhw4ZJkybVfuj06dMRERFubm5Lly41jhj30d7evqCgoHra7t27J0+erGnamTNn+vbt\naxzcs2fPpEmTgoODd+/eXVlZefHiRWtr6/baJwDmgTN2AMzA/Pnzc3JyEhISqkdu3Lixbdu2\nxx9/vGfPnvXnHz169KmnnnJ0dLS2tnZ2dn722WfT09NrT1i3bt20adPc3d1tbW0dHBweffTR\nbdu21Z6Qmpqq0+mCg4PPnz8/a9asHj162NraDh8+fOfOnQ1HPXPmzKpVqzp16rR37946rU4I\n0b9//zVr1tQ5FVffpEmTfH19NU07duxY7cxCiAULFgQFBeXl5cV4v+4mAAAGU0lEQVTGxjb8\nJAA6IIodADPw7LPPdurUaf369dUjMTExxcXF8+fPrz953bp1o0ePPnTo0OTJk1977bVHHnlk\n27Ztw4YN+/nnn6vnLFy48PLly2PHjl28ePFTTz2Vnp7+9NNPv//++3We6vz588OHD8/IyHj6\n6acnT558/PjxwMDAQ4cONRA1Ojq6srJy1qxZ3t7ed5pjY2Nz1102/jql+gxlbm5ufHy8p6fn\nQw89FBwcLISIioq665MA6HA0ADBVpaWlQgg3NzdN05599llra+u8vDzjQ35+fn369Kmqqpo7\nd64QYseOHcbxU6dOWVlZTZw4saSkpPp50tLS7OzshgwZUj1y7ty52j+ouLh42LBhtra2+fn5\nxpHjx48bD5KhoaEGg8E4uGnTJiFEYGBgA5nHjh0rhNi8eXOT9tHe3r724M6dO/V6vU6ny8nJ\nMY68++67Qojw8PDq3dfpdKdPn27kTwHQQXDGDoB5mD9/fnl5ufG2g9TU1OTk5Hnz5un1dQ9i\nq1evrqioWLZsWXFxcd7/ODs7+/v7nzhx4uzZs8Zprq6uQghN0woLC3Nzc2/cuPHEE0+UlpbW\nORvXp0+flStXVp82CwoKsre3T0pKaiDn5cuXhRAuLi61B9PS0p6vZeXKlXW2Ki0tNT4UEhLy\n6KOPTp482WAwLF682M3NTfzvtgm9Xj9nzhzj/ODgYE3TuIUCQF2SiyUA3FntM3aapvXv39/b\n21vTtBdffFGv1589e1bTtDpn7Pz8/Bo44h05csQ4LSUl5fHHH7/nnnvqTFi9erVxgvGM3dSp\nU+tE8vb2tra2biDzAw88IIQ4dOhQ7cE618N5eHjU2cdqer2+W7duY8eO/eKLL6rnGC8unDhx\nYvXItWvXrK2t77vvvvLy8savJwDlmdzHBADAncyfP/+NN944cOBATEzM+PHj+/TpU3/OtWvX\nhBDx8fG2trb1Hx04cKAQIiUlZfTo0Z06dXrhhRf+9re/2dvbW1hYJCQkRERE3Lx5s/Z8BweH\nOs9gaWlZVVXVQEgnJ6fff/+9zqfuTZs2TdM0IcTly5d79epVf6s6d8XWYbycznhpnVG3bt0C\nAwO/+eabb7/99u9//3sDeQB0KBQ7AGZj7ty5K1asmDNnTkFBQUhIyG3n2NvbCyGcnJyGDx9+\np+f58MMPS0tL4+PjAwICqgeTk5NbJeTDDz984MCBffv2zZgxo1We8OrVq3FxcUKImTNnzpw5\ns86jUVFRFDsA1Sh2AMyGo6PjlClTYmNje/bsOXXq1NvOGTVqVFpa2pYtWxoodjk5OcaZtQcT\nExNbJWRwcPB7770XExOzZMkS4wnCFtq4cWN5ebmfn9/QoUPrPBQfH5+QkJCdne3u7t7yHwRA\nAdw8AcCcRERExMbGfvfdd3f6bN5FixZZWlp+/PHHdYpaUVHR1q1bjf/dr18/IcS+ffuqH42J\niWmtYufh4bFixYqysrLx48fv2bOnzqPVd280nvEOidWrV6+vZ+HChZqm1f4UGAAdHGfsAJgT\nd3f3hs9ODRo0aO3atQsXLgwICJgwYYKPj09VVVV6enpiYmLfvn2feeYZIcSiRYtiYmJmzpz5\nzDPPuLm5HT9+fNeuXdOnT6/zGcXNtnLlSk3T3n777UmTJrm7u/v5+dnb2+fn52dlZZ04cUKv\n19/pdGN9Bw8ezMzMHDx48IgRI+o/GhIS8s4770RHR4eFhZngV6sBaH8cCACo5rnnnvP19f3w\nww8PHjx44MCBLl26ODs7z54929jqhBAjRoxISEhYuXKl8dq1YcOG7d2799KlS61V7HQ63Vtv\nvTVz5sw1a9YYr7crLi7u2rWrl5fX0qVLg4ODPT09G/lUxtN1t/0cZiFE3759AwIC9u3bt2PH\njieeeKJVwgMwa3xXLAAAgCK4xg4AAEARFDsAAABFUOwAAAAUQbEDAABQBMUOAABAERQ7AAAA\nRVDsAAAAFEGxAwAAUATFDgAAQBEUOwAAAEVQ7AAAABRBsQMAAFAExQ4AAEARFDsAAABFUOwA\nAAAUQbEDAABQBMUOAABAERQ7AAAARVDsAAAAFEGxAwAAUATFDgAAQBEUOwAAAEVQ7AAAABRB\nsQMAAFAExQ4AAEARFDsAAABFUOwAAAAUQbEDAABQBMUOAABAERQ7AAAARfx/0ARN3coD/6YA\nAAAASUVORK5CYII=",
      "text/plain": [
       "Plot with title “Bootstrapped Histogram for Mean GPA by Gender”"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# [Place your Answer here]\n",
    "data$weights<-runif(nrow(data))\n",
    "data$weights<-data$weights/sum(data$weights)\n",
    "meanGPAbygender<-data.frame(sample=integer(),FGPA=double(),MGPA=double())\n",
    "for (i in 1:1000){\n",
    "    weighteddatasample<-data[sample(1:nrow(data),100,replace=TRUE,data$weights),]\n",
    "    temp<-as.data.frame(aggregate(GPA~gender, weighteddatasample, mean))\n",
    "    temp$gender<-NULL\n",
    "    meanGPAbygender[i,]<-c(i,t(temp))\n",
    "}\n",
    "hist(meanGPAbygender$MGPA, col=rgb(0,0,1,0.5),main=\"Bootstrapped Histogram for Mean GPA by Gender\", xlab=\"Mean GPA\")\n",
    "hist(meanGPAbygender$FGPA, col=rgb(1,0,0,0.5),add=TRUE)\n",
    "legend(\"topright\", c(\"Male\",\"Female\"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Stratified Sampling\n",
    "\n",
    "For Stratifed Sampling on s strata, we generate a SRSWR of size k for each and then combine to obtain a sample of size m=sk.  In the combined sample, each of the s strata has exactly k samples represented.\n",
    "\n",
    "One way to achieve this in R is illustrated below.  \n",
    "\n",
    "First we generate some random data with two strata."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "sv<-data.frame(variable=double(),strata=integer())\n",
    "sv[1:10,1]<-rnorm(10)\n",
    "sv[1:10,2]<-as.numeric(sv[,1]>0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Second, we split the data into two subsets, one for each stratum."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "sv0<-sv[sv$strata==0,]$variable\n",
    "sv1<-sv[sv$strata==1,]$variable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Third, we perform SRSWR to sample three times from each subset and then combine."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "sv0sample<-sv0[sample(1:length(sv0),3,replace=TRUE)]\n",
    "sv1sample<-sv1[sample(1:length(sv1),3,replace=TRUE)]\n",
    "svsample<-rbind(sv0sample,sv1sample)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can achieve the same effect as steps 2 and 3 using the following code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "sv0sample<-sv[sample(1:nrow(sv), 3, replace=TRUE,prob=(sv$strata==0)), 'variable']\n",
    "sv1sample<-sv[sample(1:nrow(sv), 3, replace=TRUE,prob=(sv$strata==1)), 'variable']\n",
    "svsample<-rbind(sv0sample,sv1sample)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|<center> Apply stratified sampling with strata `gender`, with 50 samples in each stratum. Using this sampling approach, repeat the steps we carried out for SRSWR to create a Stratified Sample Bootstrapped Histogram for Mean GPA by Gender. <center>|"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzdaUBUdf///8MAAi4NhCvgikDlBqikEamAZmkaVuaapimubWrbJeV2UVmU\npRlpGpKJpJaKSKlgKoXggqKpkIkmaC4oKIjIMv8b8/+e37kGmA1mhjk+H7eGcz5zPu85G685\ncxYblUolAAAAwPopLF0AAAAA6gfBDgAAQCYIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAH\nAAAgEwQ7AAAAmSDYAQAAyATBDgAAQCYIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAHAAAg\nEwQ7AAAAmSDYAQAAyATBDgAAQCYIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAHAAAgEwQ7\nAAAAmSDYAQAAyATBDgAAQCYIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAHAAAgEwQ7AAAA\nmSDYAQAAyATBDgAAQCYIdgAAADJBsAMAAJAJgh0AAIBMEOwAAABkgmAHmERxcbGNxMmTJ03a\nnZ2dndjXwYMHTdoXqquoqPjiiy/69Onj7OysUCjUC2LUqFGWrgsNGputocy8X7VSdpYuQJ56\n9ep15MgRjYGNGjVq2rRphw4devfuPWbMmCeeeMLMVe3YsePw4cNihUOHDm0Ik4JIuto8+eST\nv/zyi0aDiRMnrlu3Tv3a3d09Ly+vHntnmdbFqFGjtmzZYukqatjznDp16uGHH9Zotnv37kGD\nBkmHPPfcc5s3bzZ5fSaWlpb2008//f777xcuXCgoKBAEQalUenp6+vr6Dho06KmnnnJwcJC2\nr3FHLQhC06ZN3dzcevfuPXbs2KeeeqrGvmbMmPH1119Lh9Q4q62CofMNDZ0KJtCzZ0+dc/7l\nl1+uqqoyZ1Xh4eFi7+Hh4Q1kUnJ1+/Zt6eI+ceKEzrdIV5snn3yyeoMJEyaIDdzd3aWjbG1t\nxVFpaWlGFMwyNZoYiNUcHR3btWvXvn37WbNmmbmS6nue2bNnV282fPhwjWbPPfecmUutX6dP\nn3788ce173JdXV2PHDkifZc+O+qnnnrq9u3bGt3du3fP1dVVo+W7775raNl132zryLj5ZkFG\n7FfvQxyxs5jvvvvu8ccfnzRpkqULgRy89tprlZWV6tdt2rSxbDH3G2mwa9u27alTp5o2bWrB\neqRiY2M//PDDJk2aiEMuXry4Y8cOC5ZU75KSkl544YWSkhLtzQoKCq5evWrExMeOHbtt2zaN\ngeojW1IbNmz473//a2NjY2gXlmLS+QYLItiZXN++fb/88ktBEO7cubNr167//ve/4qgNGzYQ\n7FAvoqKiLF3C/au4uFh87e3t3XBSnSAIRUVFP/zww9SpU8Uh33zzjfgdQAaysrI00omTk9OQ\nIUN8fX2VSuXt27fPnj178ODBU6dOaZ/OI488Mnv2bEEQ7ty5c+jQoR9//LGqqko9avv27RkZ\nGQEBAWLj9evXV5/ChQsXDhw4YP5zbIxTX/MNDZGlDxnKk5bf1AYOHCiO8vT0rP7eo0ePhoeH\nP/LIIw888IC9vX2rVq0GDRq0YsWKO3fu1NiXPu2r//Ii5erqqm5WVlYWHR09cOBANzc3BwcH\nR0dHDw+PXr16vfLKK9HR0QUFBfpPSuMnhmvXrs2ePbtDhw52dnb9+vVTt9m+ffvcuXNDQkK8\nvLxcXV3t7OyaNWvm5eU1atSo7du3V/+kGtO8dOnSjBkz2rdv7+Dg4OHhMW3atMuXL9f9LWon\nTpyYNWtW165dlUplo0aN2rRpM2zYsE2bNtX463lJSUlERIS3t7eDg0ObNm3GjRuXk5PTQH6K\nrcdlqmbQ+llSUvL++++r50zr1q3HjBlz6tQpLXPGFKuNtK+0tLSzZ8+OHTu2ZcuWTZo06dOn\nz5YtW9TNiouLIyIiPD091evG9OnTr169qnORzZkzR8us27RpkxHzTZ+ZUBvpKiQeOvL19RUb\nlJWVtWrVSqOBUMtPsfpvBXXclgsKCubOndupUyf1ejJ+/Pjz589r/6Sifv36Sef5U089deXK\nlerNsrOzX3vttf3799c2uzS2uOXLl0snu3jxYnFUUVGRo6OjOGrIkCHi6ylTpuhZdo3z4erV\nq+plXeMOasGCBVqWV05OjjjWwcHh5s2b2ruuy3xT03/1MG5xG7dfNboqgza0Bo5gZxJa9hfS\nc5Z79uwpHVVeXj5r1iyhFu3atTt8+LBx7fX5z11aWtqnTx8tzXbv3q3npFT/u838+OOPbdu2\nFf8Ut5kePXpomdSzzz5779496eeVTnPVqlXVz3Fp0aLFyZMn6/iWysrKt956q7bfU4KDg9Vh\nSHTt2rVu3bppNGvatGlCQoJ0iEWCXf0uU0PXz+vXr3fv3l2jmaOj448//ljbnDHFaiMd++WX\nXzZr1kzjLZ9++um1a9e6du2qMdzLy6uoqEj7ItMn2Bk63/SZCbWRrkKhoaHi6z/++EPdYMOG\nDeohNjY20gYaQcHQraAu2/KaNWuqnzzQunXrixcvav+wKpUqIyND+q6ePXuWlZXpfFeNs0tj\ni8vPz5dOecaMGeKoNWvWSHuUXs3q4uJy9+5d/QuQzofvv/+++nyQ7qDy8/Pt7P7/H9kaNWp0\n7do16aQiIyPFd40cOVJ7v3Wcb4auHkYsbiP2q3WpytANrYEj2JmEdH/Rt2/fQ4cOHTp0aP/+\n/REREdLVbv78+dJ3TZ8+vcY1UvTggw+ePXvWiPb6/Of+7LPPpAMdHR3V37zFIUYHuxYtWkjb\nPPHEE+o24j8De3t7V1dX6WlAagsWLJDOH+k0GzVqVGMBXl5e0kMgRrxF41+1QqHQ+GUtKCio\nvLxcbP/000/XOFmNdxka7Dp06DCnmi5duogN9Al29btMDV0/a5szGlfY1Rbs6mu1kY6yt7ev\nXk+jRo1qi7/vvfee9kWmT7AzdL7pMxP0WYUWL14srjDjxo1TNxDPlB88eLD0chmNYGfoVlCX\nbbnGhSIIwksvvaT9w6pUqoULF0rfsmPHDp1vqW12aQS7P/74QzrlefPmiaMGDBggDv/0009V\nKlWnTp3EIeIxYH1I50P1maYm3UE999xz4vDPP/+8ts+SmJiovd86zjdDVw8jFrcR+9W6VGXo\nhtbAEexMQp+Lrfr06SO92ErjK1Tv3r2TkpIyMzM//PBD6X/i4cOHG9H+ypUrubm5Y8aMEYeP\nGTMm9//8888/KpVq2LBh4tiffvpJfeC6oqLizz///Oqrr/r375+cnKznpFT/u80IgmBra/vs\ns8/Omzdv/Pjxzz77rLpNeHj46tWrz549W1lZqR5y5cqVN998U3yXq6ur9Pi5xjSfffbZX375\n5ZdffpFWLgjCl19+afRbMjMzxeRtY2PzySeflJaWqlSq9PT0du3aie1XrVqlbr9v3z7pdHr2\n7Pnzzz/v27dPfbKOlKHBTid9gl09LlND10+NOePn57dt27bU1NTqx65qC3ZCPa02Gt0NHTo0\nPj7+nXfe0fhm37x58y+++GLdunWenp7iwM6dO2tfZDdu3MjNzX3vvffEtwQGBoqzrqSkxND5\npudM0GcVWrx48VdffaV+7eDgcO3ataysLHHs9u3bawt2hm4FRiwUjc/Ys2fP7777buXKlW5u\n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\nS2CdHPu+z+nh9Srb5db2AiDLfP7553fcccfxxx//9ddfH8r+q1atuuSSS8rKynr16tWqVatF\nixaNHj36tddeW7hwYcOGDY/2askWh3teRVGUk5PTt2/f6lsKCgqOwtLISkd2eni9CkEMHI5r\nr722efPmI0aMiKLovvvu+879O3fuHEXRtGnT0n+sqKjo3bt3FEUPPPDA0V0oWeVwz6t27drV\nr18/gYWRjY749PB6FQA/ioXDMG3atNmzZ0+ZMqVJkyaHsv+yZcsWL1583nnnlZSUpLfk5OSM\nHTs2Jyfnsccei+P4KK6V7HG45xUcDV6vwiDs4FBt2rTp17/+df/+/Xv27HmIX7Jw4cIoiq68\n8srqG0899dRzzz33448/Li0tzfwqyTZHcF6lVVZWjhkzZsCAAYMHD548efLWrVuP0grJRkdw\neni9CoN77OCQVFZW9uvXr7CwcMKECYf+VWvXro2iqF27djW2t23bdvny5aWlpfs/RJ1yZOdV\n2jfffHPfffdV/XHo0KGTJ09O/+AMjuD08HoVBlfs4JCMGzfur3/969SpUw/r/vSysrLoQPcs\nFxYWRlG0ffv2DK6QbHRk51UURf369Zs/f/6nn366a9euVatWDR48eNeuXX379l20aNFRWipZ\n5MhOD69XYXDFDr7b+++/P2LEiF/84hfdu3ev7bUQju9zXg0bNqzqn9u3b//oo48WFBSMHj36\noYceuuSSSzK6TLKP06Muc8UOvkMcx3379i0qKho7duzhfm36777pvwdXl/67b/rvwdRN3+e8\nOqABAwZEUbR48eKMHI3AHMrp4fUqDMIOvkNFRcWKFSs2btzYuHHjqo/6vOuuu6IoGj16dCqV\nGjhw4Ld9bfqWlPSdK9WtW7cuiqK2bdsezYVzTPs+59UBpb/v7t2796gslyx3KKeH16sw+FEs\nfIecnJz0X3ar++c///nOO++cd955xcXFB/nRxuWXXx5F0csvvzxmzJiqjZ988smKFStatGjh\nhbIu+z7n1QG9+eabURS1bt06Y0skIIdyeni9CkTtfoweZKn0exj3/yDZadOmTZgw4bPPPqva\nkv7AzyeeeCL9x4qKij59+kQ+8JMDOcTzavHixStWrKi+w5IlS4qKiqIo+t3vfpfQWjlWHfrp\n4fUqSK7YQSY9+OCD69ev79Kly8knn5zeMnXq1C5duvTv3//Pf/5z+lf0LF269IILLhg6dGjt\nLpUsUuO8evPNN++5557WrVu3atXqhBNO2Lhx4/Lly+M4vvrqq3/1q1/V9mKpZYd+eni9CpJ7\n7ODoOuecc5YuXXrTTTe99dZbEydO3LZt27333vvaa6/5xYscsa5du95xxx2NGjVatmzZnDlz\nPvroo27duj311FOzZ8/Oy8ur7dVRy77P6eH1KgCp2C8JAQAIgit2AACBEHYAAIEQdgAAgRB2\nAACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQ\ndgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACB\nEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2wLFrz549qVQqlUrV\nq1fv448/3n+H9u3bp3d48cUXk1/ewa1du/auu+7q0KFDkyZN8vLyTjzxxIsuuui+++4rLS2t\nvlvVc6x6pieddFLXrl2nT5++/zFHjx6d3m3t2rVJPQ8gmwg74FiXm5tbWVk5bdq0Gtv//ve/\nr169Ojc3t1ZWdRBxHI8aNerss8/+/e9/v3379ssvv7xfv35du3bdunXrmDFjzjrrrCeffLLG\nl+Tn5w8aNGjQoEElJSXt27dfuHBhnz597r777hqHffzxx1OpVBRFU6ZMSe75ANkjFcdxba8B\n4MD27NnTsGHDli1bFhYWlpWVbdiwIZ01af3793/mmWe6d+8+b968uXPnXnXVVbW41OpGjRp1\n//33FxUVTZ06tUePHtUfWrdu3bhx41q2bDls2LD0lvRzLCgo2L59e9VuL7/8cs+ePeM43rBh\nwxlnnJHe+Morr/To0aOkpOTll1/et2/f5s2b8/Pzk3pOQHZwxQ7IAgMHDty0adOCBQuqtuzY\nsWPmzJlXX31106ZN99//7bffvv7660855ZT8/PyioqJbb711zZo11XeYMmXKtdde26pVq4YN\nGxYWFl566aUzZ86svsPy5ctTqVRJSclHH310yy23nHTSSQ0bNuzUqdO8efMOvtQNGzY8+OCD\nDRo0ePXVV2tUXRRFbdq0mTRpUo1Lcfvr0aPH+eefH8fxkiVLqq85iqI77rijT58+X3zxxaxZ\nsw5+EKAOEnZAFrj11lsbNGjw+OOPV22ZPn36zp07Bw4cuP/OU6ZM6dKly6JFi3r27Hn33Xdf\ncsklM2fO7Nix47vvvlu1z6BBg7Zs2XLZZZcNGTLk+uuvX7NmzY033vjII4/UONRHH33UqVOn\ntWvX3njjjT179nzvvfd69eq1aNGigyx12rRp+/btu+WWW9q3b/9t+9SvX/87n3L6xylVVyg/\n++yzOXPmtG3b9qKLLiopKYmiaPLkyd95EKDOiQGOVbt3746iqGXLlnEc33rrrfn5+V988UX6\noeLi4tNPP72ioqJfv35RFM2dOze9ffXq1Xl5eVdcccWuXbuqjrNixYrjjz/+3HPPrdryr3/9\nq/qgnTt3duzYsWHDhlu3bk1vee+999IvkiNGjKisrExvfOqpp6Io6tWr10HWfNlll0VR9Oyz\nzx7WcywoKKi+cd68eTk5OalUatOmTektDz30UBRFY8aMqXr6qVRq3bp1hzgFqCNcsQOyw8CB\nA8vLy9NvO1i+fPnSpUv79++fk1PzRWzixInffPPNvffeu3Pnzi/+R1FRUdeuXVeuXPnhhx+m\ndzvttNOiKIrjuKys7LPPPtuxY8d11123e/fuGlfjTj/99JEjR1ZdNuvTp09BQcHixYsPss4t\nW7ZEUdSiRYvqG1esWPGLakaOHFnjq3bv3p1+aMCAAZdeemnPnj0rKyuHDBnSsmXL6H/eNpGT\nk3Pbbbel9y8pKYnj2FsogJpqOSwBvl31K3ZxHLdp06Z9+/ZxHN955505OTkffvhhHMc1rtgV\nFxcf5BXvrbfeSu+2bNmyq6++unHjxjV2mDhxYnqH9BW7a665psaS2rdvn5+ff5A1n3XWWVEU\nLVq0qPrGGvfDtW7dusZzrJKTk9OkSZPLLrvs6aefrtonfXPhFVdcUbXlyy+/zM/PP/nkk8vL\nyw/93ycQvGPuYwIAvs3AgQN/85vfvP7669OnT+/evfvpp5++/z5ffvllFEVz5sxp2LDh/o+e\nffbZURQtW7asS5cuDRo0+OUvf/njH/+4oKCgXr16CxYsGDdu3N69e6vvX1hYWOMIubm5FRUV\nB1lks2bNPvjggxqfunfttdfGcRxF0ZYtW5o3b77/V9V4V2wN6dvp0rfWpTVp0qRXr17PP//8\nCy+88POf//wg6wHqFGEHZI1+/foNHz78tttu2759+4ABAw64T0FBQRRFzZo169Sp07cdZ/z4\n8bt3754zZ063bt2qNi5dujQji7z44otff/31+fPn33zzzRk54Oeffz579uwoinr37t27d+8a\nj06ePFnYAVWEHZA1TjnllKuuumrWrFlNmza95pprDrjPhRdeuGLFihkzZhwk7DZt2pTes/rG\nhQsXZmSRJSUlDz/88PTp04cOHZq+QPg9PfHEE+Xl5cXFxeedd16Nh+bMmbNgwYKNGze2atXq\n+w8CAuDNE0A2GTdu3KxZs1588cVv+2zewYMH5+bmPvroozVC7euvv37uuefS/3zmmWdGUTR/\n/vyqR6dPn56psGvduvXw4cP37NnTvXv3V155pcajVe/eOHTpd0hMnDjx8f0MGjQojuPqnwID\n1HGu2AHZpFWrVge/OnXOOec89thjgwYN6tat209/+tMOHTpUVFSsWbNm4cKFZ5xxxk033RRF\n0eDBg6dPn967d++bbrqpZcuW77333ksvvXTDDTfU+IziIzZy5Mg4jh944IEePXq0atWquLi4\noKBg69at69evX7lyZU5OzrddbtzfG2+8UVpa+qMf/ahz5877PzpgwIDRo0dPmzZt1KhRx+Cv\nVgOS54UACM3tt99+/vnnjx8//o033nj99dePO+64oqKivn37pqsuiqLOnTsvWLBg5MiR6XvX\nOnbs+Oqrr37yySeZCrtUKnX//ff37t170qRJ6fvtdu7cecIJJ7Rr127YsGElJSVt27Y9xEOl\nL9cd8HOYoyg644wzunXrNn/+/Llz51533XUZWTyQ1fyuWACAQLjHDgAgEMIOACAQwg4AIBDC\nDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQ\nwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAg\nEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBD/D14Uz8VerYJeAAAAAElFTkSuQmCC",
      "text/plain": [
       "Plot with title “Bootstrapped Histogram for Mean GPA by Gender”"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# [Place your Answer here]\n",
    "meanGPAbygender<-data.frame(sample=integer(),FGPA=double(),MGPA=double())\n",
    "for (i in 1:1000){\n",
    "    smale<-data[sample(1:nrow(data), 50, replace = T, prob = (data$gender == 'M')),]\n",
    "    sfemale<-data[sample(1:nrow(data), 50, replace = T, prob = (data$gender == 'F')),]\n",
    "    ssample<-rbind(smale, sfemale) \n",
    "    temp<-as.data.frame(aggregate(GPA~gender, ssample, mean))\n",
    "    temp$gender<-NULL\n",
    "    meanGPAbygender[i,]<-c(i,t(temp))\n",
    "}\n",
    "hist(meanGPAbygender$MGPA, col=rgb(0,0,1,0.5),main=\"Bootstrapped Histogram for Mean GPA by Gender\", xlab=\"Mean GPA\")\n",
    "hist(meanGPAbygender$FGPA, col=rgb(1,0,0,0.5),add=TRUE)\n",
    "legend(\"topright\", c(\"Male\",\"Female\"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Systematic sampling\n",
    "Systematic sampling is a sampling technique that is used to sample from a sequence of items. To sample $n$ items from a sequence of $N$ items, we sample every $k$-th item, where $k = N/n$, and the starting point is randomly sampled from the first $k$ items.\n",
    "\n",
    "|<center>TASK</center>|\n",
    "| ---- |\n",
    "|<center> Consider using systematic sampling to sample 167 items from `data`. What is the value of $k$? How many different samples can you have? What are the average GPAs for these samples? <center>|"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# [Place your Answer here ]\n",
    "#k = N/n = nrow(data) / 167 = 835 / 167 = 5 , We have 167 kinds of different samples, 4.539 is the acerage GPAs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Extension\n",
    "\n",
    "We have included some extra material demonstrating how data has been generated for the k-anonymity part of this prac, and how the Python programming language could alternatively be used for the K-anonymity task.\n",
    "\n",
    "**THIS IS NOT ASSESSED**\n",
    "\n",
    "If you are interested, you can read through the notebooks in the [data_preparation](data_preparation) folder of Prac 2. Try to see if you can follow what is being done.\n",
    "\n",
    "The `KAnonymityWithPython` notebook demonstrates how you could potentially use the Python programming language instead of MySQL to perform the K-anonymity task of this practical.\n",
    "\n",
    "The `GetUQPrograms` notebook demonstrates *web-scraping*, which was used to generate the dataset used in this prac by scraping real programs from the https://www.uq.edu.au/study/browse.html?level=ugpg page.\n",
    "\n",
    "The `GenerateCSVs` notebook demonstrates how we can use Python to generate some sample data.\n",
    "These three notebooks demonstrate how you could potentially use the Python programming language instead of MySQL to perform the the K-anonymity task of this practical. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.4.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
