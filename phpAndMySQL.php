<?php
/*
 * PHP and MySQL
 * Basics and Tutorials
 * 
 * 
 * Written by Josh Lyell
 * 
 * 
 * //////////////////////////////////////////////////////////////////////////
 * 
 * Contents
 * 1. Introduction
 * 
 * 		1.1 What is PHP?
 * 		1.2 What is MySQL?
 * 		1.3 Understanding the Cloud
 * 
 * 2. Basics
 * 		
 * 		2.1 Variables
 * 		2.2 Displaying Variables
 * 		2.3 Displaying Text and Concatenating Variables
 * 
 * 3. Arrays
 * 
 * 		3.1 Arrays
 * 		3.2 Sorting Arrays
 * 		3.3 Multi-dimensional Arrays
 *
 * 
 * ///////////////////////////////////////////////////////////////////////////
 * 
 * 1 		Introduction
 * 1.1 		What is PHP?
 * 	
 * 
 * PHP is a general pupose scripting language that is especialy suited for web development and can be embedded into HTML.
 * It can also speak to MySQL databases to retrieve and store information. PHP originally stood for 'Personal Home Page'
 * but it now stands for the recursive acronym PHP: Hypertext PrePreprocessor. 
 * Unlike C++ and Python, PHP must be on a webserver, and ran through a browser to view code. Popular webservers include
 * Apache and XAMPP. (The text I have read insists on Abyss webserver, which seems to run fine.) The scripts are stored 
 * within the webservers directory and is called upon through a browser. For testing PHP is usually run through 
 * 'Localhost' which is native to the developers PC.
 * 
 * 
 * 1.2 		What is MySQL?
 * 
 * MySQL is he worlds most popular database software. PH and MySQL are both 'server-side' technologies. They reside on 
 * a webserver. They are not 'client-side' technologies resident o nthe users computer. Their magic takes place on 
 * 'The Cloud' (online).
 * 
 * 
 * 1.3 		Understanding the Cloud
 * 
 * Whenever a user ask to view a web page in their browser, it requests the page from the web sever, and recieves the page
 * in response, via the HTTP protocol. Where a webpage contains PHP script, the web server may first call upon the PHP 
 * engine to process code and if required, rerquest data from a MySQL database before sending the process to a browser.
 * 
 * 
 * 2		Basics
 * 2.1 		Variables
 * 
 * Variables store data within PHP. Variable names must:
 * - begin with a $
 * - not contain spaces
 * - first character must be a letter 
 * - variables in PHP do not need to be designated a type (int, char, so on) */
 
 
$body_temp = 98.6;
 
 
/* 2.2 	Displaying Variables
 * 
 * Variables can be displayed by using the 'echo()' function.
 */
  
  
echo 'This is a string';
echo $body_temp;
  
  
/* Strangely 'echo' is not actually a function, functions in PHP have the () syntax.
 * Strings can also be passed through the echo function. Variables passed through
 * do not need quotes.
 * 'echo()' is also slightly faster than 'print()' and tus is recommended.
 * 
 * 
 * 2.3	Displaying Text and Variables
 * 
 * To display text and variables, concatenation has to be used to join them together. The concatenate operator is a full stop
 * '.' */
 
 
echo 'Body temperature is' . $body_temp . 'degrees celsius.';


/* This line of code will produce the line: Body temperature is 98.6 degrees celsius.
 * 
 * When you want to show strings that use quotes, you can use backslashes before the quotes to signify that the quote is to 
 * be part of the string. */
 
 
echo 'The Dear Hunter \"In Cauda Venenum\"';


/* 3 	Arrays
 * 3.1 	Producing Arrays
 * 
 * An array variable can store mulyiple items of data in sequential arrays 'elements' that are numbered or 'indexed' from 0.
 * Array items have a key (which is the sequential index in most cases) and the value, which is the stored variable. */
 
 
$days = array('Mon', 'Tues', 'Weds');
echo $days[1];


/* This will display the value at the key of '1', = 'Tues'. */


$months = array(	'jan' => 	'January',
					'feb' =>	'February',
					'mar' =>	'March');

echo $months['feb'];


/* This statement would output 'February' as 'feb' is the key for the value February.
 * 
 * 3.2 	Sorting Arrays
 * 
 * The following functions can sort arrays: */
 
 
sort(); 	// sorts by value, lowest to highest

asort(); 	// sorts by value in ascending alphanumeric order (a-z 1-9)

ksort(); 	// sorts by key in alphanumeric order

// For example: 

sort($cars);
asort($books);
ksort($movies);
		
 


   
  
 
?>
