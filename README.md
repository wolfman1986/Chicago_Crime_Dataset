# Chicago_Crime_Dataset
Galvanize Data Analytics Immersive Capstone

Background & Motivation
According to the Chicago Sun*Times, through analyzing crime statistics, Chicago had its deadliest year in 2021 since in nearly 30 years. There is no singular answer as to why Chicago is subject to a substantially higher amount of crime compared to other major cities. We frequently hear on the news, internet, and social media about prevalent criminal activity in Chicago that includes violent crimes, gun violence, homicides, drug addiction and more. Additionally, while some criminal offenders are put in jail, a 2018 report showed that 43% of those released from prison in Illinois will be convicted of another crime and return to prison.

To gain a better understanding of the situation, I analyzed a crime data from the city of Chicago from January 1st, 2001, to July 14th, 2023. I was curious to see if there were any correlations to certain crimes, locations and arrest rates and the time of day these crimes were most likely to occur. 

The Dataset
The Chicago Crime Database is a comprehensive repository of crime-related data collected and maintained by law enforcement agencies in the city of Chicago, Illinois, USA. The database serves as a critical tool for researchers, policymakers, and law enforcement professionals to analyze crime trends, identify patterns, and develop effective strategies to enhance public safety and well-being.

Data Collection: The Chicago Crime Database is a product of collaborative efforts between the Chicago Police Department (CPD) and other relevant agencies. It aggregates a vast amount of crime-related information, including incident reports, arrest records, case details, and offender profiles. The data collection process is ongoing, ensuring that the database remains up-to-date and relevant for crime analysis.


The Data
The City of Chicago maintains a robust dataset recording incidents of crime that occurred in the city. This data is extracted from the Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) system. 
The dataset records more than 7,846,809 criminal incidents. Much of the recorded criminal activity is accompanied by additional data to include, but not limited to: Case Numbers, DTG, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X,Y Coordinates, Year, Records Update DTGs. 

Hypothesis Test
My NULL Hypothesis is: For all crimes and reported incidents in this dataset, there will be no relationship between any of the independent variables the occurrences of arrest.
My ALTERNATE Hypothesis is: For all crimes and reported incidents in this dataset, there is a strong relationship between the independent variables and the occurrences of arrest.
As I performed my Exploratory Data Analysis I implemented statistic modeling based off logistic regression to either confirm or reject my Null hypothesis. 


Exploratory Data Analysis
After importing and cleaning my data using panda, one of my first goals was to determine how many different unique values and categories of data were present in the dataset. The column Primary Type contains a list of 36 criminal incidents, ranging from Theft as the most common to Ritualism and Non-Criminal as the least common. 

Feature Definition And Their Unique Value Count
Date [2001-2022] - All records use the date format 06/21/2023 08:00:00 PM
Block [63085] - In the context of urban planning and geographical references, a "block" typically refers to a bounded area of land within a city that is surrounded by streets or other physical boundaries. 
Primary Type [36] - Category of crime. Examples in this dataset include, but limited to, Theft, Robbery, Narcotics, Battery, Burlgary, Criminal Sexaul Assault and Arson
Description [548] - Provides additional details about the type or nature of the reported crime incident. 
Location Description [227] - The specific place or area where a crime incident occurred.
Arrest [TRUE/FALSE]
Domestic [TRUE/FALSE]
Districts [24] - A districts can refer to different administrative divisions, each serving a specific purpose. Examples include Police Districts, School Districts, Community Areas, Voting Districts and Fire Districts   
Ward [50] -  Each ward is represented by an alderman who advocates for the interests and concerns of the residents within that specific geographic area.
Community Area [78] - A Community Area refers to a geographic region within the city of Chicago that is defined by the city's official Community Area boundaries. These boundaries were established by the City of Chicago for administrative and data collection purposes. Each community area represents a distinct neighborhood or area within the city.


According to the data, from 2001 -2022, there was a gradual year-by-year negative percentage change until there was a strong uptick in 2014 and 2020. This could be attributed to racial tension changes in policing. 

The top 10 most frequent crimes dwarfed all other, with Theft, Battery and Criminal Damage representing just over half of all recorded incidents. 

When Crime Occurs
After importing and cleaning my data use pandas, one of my first goals was to determine whether there was any correlation between criminal activity, the time of day and day of the week. To answer this, I had to extract the day of the week and hour from the DTG value entries and group the data by day of the week and hour, and then get the count of crimes for each group. Perhaps unsurprisingly, the resulting heatmap shows that criminal activity is least likely to occur during the early hours of the morning, with peak times at noon and midnight. 

Due to the immense amount of data, I decided to become much more specific in my analysis, taking focus on all incidents where the crime was categorized as Domestic. As defined by the U.S. Department of Justice: “Domestic violence is a pattern of abusive behavior in any relationship that is used by one partner to gain or maintain power and control over another intimate partner.” More detailed definitions can be found at Office on Violence Against Women (OVW) | Domestic Violence (justice.gov).
In the dataset, the total number of occurrences where domestic was listed as a factor, amounts to 1,063,990. The number one domestic crime, unsurprisingly, involves the presence of children. 

