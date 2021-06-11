# Scientific_Networking

## Background

The goal of this project is to understand the penetration of publications and what drives scientific relevance.

The citation data was extracted from DBLP, ACM, MAG (Microsoft Academic Graph), and other sources. It is available on this [website](https://www.aminer.org/citation). 
The version used was the 13th version. It contains 5,354,309 papers and 48,227,950 citation relationships. Each paper is associated with abstract, authors, year, venue, and title.

The data set can be downloaded directly [here](https://originalstatic.aminer.cn/misc/dblp.v13.7z).

## Data Pipeline

The data is provided in a JSON format. However, due to some original data errors such as additional columns and null json rows, the data cannot be loaded in directly into Spark or Pandas without additional cleaning. This is addressed through the Json_File_Corrector.py.

These original errors pushed my first approach to a simplier method using File Open and manually changing each line into a workable Pandas DataFrame. Due to the size of the file and limitations with Memory, this limited my scope to the first 1.5 million publications. 

The DataFrame had sublists and subdictionaries that had key information about the authors, publishers, keywords. I created methods that extracted that information and simplified the DataFrame.

There were items where the year (1500 - 2021), author, and information were not available. These items were removed.

For more focused items, I set a minimum threshold of 10 citations as it is currently standard practice that any articles that are relevant are 10 or above.
These were not controlled for time.


## Questions

Starting off with some basic questions about the data

### General Data
* Amount of journal releases over the number of years
* How much has no or negligible citations (i.e. junk journals)?
    * This would assume either 0 citations and/or no author
    * What percentage is this of total?
* Of the junk citations - who are the worst offenders?
    * Look at Authors and Venues
    * Do they have a common area or tend to use a specific keyword?
    * Limit to top 10

###  Focused Data  
* Limit the citations to be something considered influential. 10 or more citations is considered to be solid.
    * Check the distribution of citations. It should be heavily focused to one-side
* What are the top ten venues, authors and keywords?
* Of the Top 10 everything - what is the distribution of citations for each?
* Is there a difference between the #1 and #10 source? What about #5 and #10?
    * Repeat for each venue, authors, keywords
* Is there a statistically significant difference between the #1 venue and #1 author?

## Insights from 'Junk Citations'

* Praxis der Informationsverarbeitung und Kommunikation ceased running in 2016 - means Information processing and communication practice
* SIGGRAPH Computer Animation Festival is a festival - more URL links
* Datenschutz und Datensicherheit - Data Protection and Data Safety


* Almost submissions are all only one author with 0 - negligble keywords tend to get 0 citations though some of the venues are high performing
* Most authors submitted to one journal/ group - if submit to other areas, its only a one off.
* Encyclopedias themselves get cited, but not necessarily the individual contributor

## Hypothesis Testing

### Null Hypothesis: There is no difference between all the most prolific Authors, Venues or Keywords

### Alternate Hypothesis: There is an intergroup difference between the Authors, Venues or Keywords. 

#### Note: Each Hypothesis is independent of one another

##### Alpha = 0.05

## Insights

1. The keyword failed to reject the null hypothesis in most cases. We can conclude there is no stat. sig. difference in keywords aside from computation complexity.
2. The last author failed to reject the null hypothesis in most cases except for 1. This means the most profilic last authors have no stat. sign. impact on # of citations other than vs Saharon.
3. The most prolific venue did have multiple significant difference where it is greater. Only BMC Informatics have similar penetration.

Assuming number of citations indicates it penetration in the scientific community

## Diving Deeper

### We would like to see if there is truly a difference between the most prolific Author and prolific Venue.

#### Null Hypothesis: There is no difference between all the most prolific Author and Venue

#### Alternate Hypothesis: There is an intragroup difference between the Author and Venue
##### Alpha is 0.05

