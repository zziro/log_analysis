# log_analysis
Project related to track most popular articles, authors and erros.

When it comes to run the project you should follow the below steps:

P.S: I am asuming you have the vagrant virtual machine and connected to the database "news".

1.- Go to the file "source_code.txt" and there you will find three views. 
2.- Run one by one all of those views.
3.- In order to execute the views, run the bellow commands:

	SELECT * FROM most_popular_articles;
	SELECT * FROM most_popular_authors;
	SELECT * FROM days_with_more_errors;
4.- Once you do that, you will be able to see the results like output.txt file.


