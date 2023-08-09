# Chicago Crime Dataset 2001-2002
dataset source: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

## Galvanize Data Analytics Immersive Capstone

### Background & Motivation
- According to the Chicago Sun*Times, through analyzing crime statistics, Chicago had its deadliest year in 2021 since in nearly 30 years. There is no singular answer as to why Chicago is subject to a substantially higher amount of crime compared to other major cities. We frequently hear on the news, internet, and social media about prevalent criminal activity in Chicago that includes violent crimes, gun violence, homicides, drug addiction and more. Additionally, while some criminal offenders are put in jail, a 2018 report showed that 43% of those released from prison in Illinois will be convicted of another crime and return to prison.

- To gain a better understanding of the situation, I analyzed a crime data from the city of Chicago from January 1st, 2001, to July 14th, 2023. I was curious to see if there were any correlations to certain crimes, locations and arrest rates and the time of day these crimes were most likely to occur. 

### The Dataset
- The Chicago Crime Database is a comprehensive repository of crime-related data collected and maintained by law enforcement agencies in the city of Chicago, Illinois, USA. The database serves as a critical tool for researchers, policymakers, and law enforcement professionals to analyze crime trends, identify patterns, and develop effective strategies to enhance public safety and well-being.

Data Collection The Chicago Crime Database is a product of collaborative efforts between the Chicago Police Department (CPD) and other relevant agencies. It aggregates a vast amount of crime-related information, including incident reports, arrest records, case details, and offender profiles. The data collection process is ongoing, ensuring that the database remains up-to-date and relevant for crime analysis.

### The Data
The City of Chicago maintains a robust dataset recording incidents of crime that occurred in the city. This data is extracted from the Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) system. 
The dataset records more than 7,846,809 criminal incidents. Much of the recorded criminal activity is accompanied by additional data to include, but not limited to: Case Numbers, DTG, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Beat, District, Ward, Community Area, FBI Code, X,Y Coordinates, Year, Records Update DTGs. 



### Exploratory Data Analysis
After importing and cleaning my data using panda, one of my first goals was to determine how many different unique values and categories of data were present in the dataset. The column Primary Type contains a list of 36 criminal incidents, ranging from Theft as the most common to Ritualism and Non-Criminal as the least common. 

### Feature Definition And Their Unique Value Count
- Date [2001-2022] - All records use the date format 06/21/2023 08:00:00 PM., The first timestamp is 2001-01-01 00:00:00 and the last timestamp is 2022-12-31 23:55:00
- Block [63085] - In the context of urban planning and geographical references, a "block" typically refers to a bounded area of land within a city that is surrounded by streets or other physical boundaries. 
- Primary Type [36] - Category of crime. Examples in this dataset include, but limited to, Theft, Robbery, Narcotics, Battery, Burlgary, Criminal Sexaul Assault and Arson
- Description [548] - Provides additional details about the type or nature of the reported crime incident. 
- Location Description [227] - The specific place or area where a crime incident occurred.
- Arrest [TRUE/FALSE] - A TRUE value means an arrest was made. A FALSE value means an arrest was not made.
- Domestic [TRUE/FALSE] A TRUE value means that this crime was categorized as Domestic. A FALSE value means that it was not categorized as Domestic.
- Districts [24] - A districts can refer to different administrative divisions, each serving a specific purpose. Examples include Police Districts, School Districts, Community Areas, Voting Districts and Fire Districts   
- Ward [50] -  Each ward is represented by an alderman who advocates for the interests and concerns of the residents within that specific geographic area.
- Community Area [78] - A Community Area refers to a geographic region within the city of Chicago that is defined by the city's official Community Area boundaries. These boundaries were established by the City of Chicago for 
  administrative and data collection purposes. Each community area represents a distinct neighborhood or area within the city.


- According to the data, from 2001 -2022, there was a gradual year-by-year negative percentage change until there was a strong uptick in 2014 and 2020.
- An initial analysis revealed that, contrary of popular opinion, crimes per year, at least those being recorded, has reduced by more than half since 2001. 
- There are three significant changes in the yearly record, from 2001 to 2015 there was a gradual decrease of approximant 475,000 crimes per year to 260,000
  by the year 2015.
- From 2015 to 2019, crime rate remained constant and then between 2020 and 2021 there was another significant drop.
- A possible explanation for this was the Covid-19 lockdowns and changing in policing and recording crimes during that time period so it does not necessarily mean that 
  Crimes were not being committed, only that they were possibly not being recorded.
  
  ![Total_Crimes_By_Year_alt](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/d2d791f1-d04c-444a-8bc2-08419060de6b)
  ![10_most_frequent_crimes_pie](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/d191daa6-ced9-4130-abe6-e2685d0aa426)


- Also of note, of all 36 crime categories, the top 10 crimes represented 91.57% of all crimes.
- The top 10 most frequent crimes dwarfed all other, with Theft, Battery and Criminal Damage representing just over half of all recorded incidents. 

### Most Common Crimes
- To explore further and with more specificity, I calculated the top 5 most common crimes that were recorded. They too, showed a gradual decrease in with theft, battery and narcotics showing the strongest decline.
  
![crime_type_total_crime](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/1546d525-c554-439a-b0b4-1e8e017ecf50)
![sexual_assaults](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/851997a4-7312-46c7-b1da-3c727898f0db)

- Criminal sexual assault crimes, however, were discovered to be an extreme outlier to my EDA, where there was an increase of 2,454% from 2012 to 2022. I created a separate chart as to not drastically skew the first chart.
  

### When Crime Occurs
- This heatmap shows the relationship between the day of the week and time of day where a crime is most likely to occur. There are several important takeaways from this data.
- We can see that crimes are least likely to be committed during the weekday between the hours of 0100 and 0700 and slightly more likely during the same time period on the weekends.
- Noon and Midnight seem to have the strongest probability for a crime to occur daily
- The days of the week show that crime is more likely to occur on Friday evenings from 1800 to 2200 with Tuesday and Wednesday not far behind.
  
![crime_trends_by_day_week_hour](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/5696fa53-d1b0-43a7-851e-4c221ef2b2b7)
![crime_trends_by_month_year](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/2544e829-c6bf-4de7-aa25-59407ef5d08b)

### Hypothesis Test
- My NULL Hypothesis is: For all crimes and reported incidents in this dataset, there will be no relationship between any of the independent variables the occurrences of arrest.
- My ALTERNATE Hypothesis is: For all crimes and reported incidents in this dataset, there is a strong relationship between the independent variables and the occurrences of arrest.
- As I performed my Exploratory Data Analysis I implemented statistic modeling based off logistic regression to either confirm or reject my Null hypothesis. 

### Linear Regression Analysis for Hypothesis Testing
- With all the coefficients calculated through my logistic regression, the best way to assess my hypothesis is to example the results. 

### Results
- I analyzed the relationship between a set of independent variables (features) and a binary outcome, such as "Arrest" or "Not Arrested." The coefficients in the logistic regression model represent the strength and direction of the relationship between each feature and the likelihood of an arrest occurring.
- A simple sort of the coefficients revealed that the top 8 crimes with the LEAST LIKELY arrest rate were Burglary, Theft, Criminal Damage, Robbery and Motor Vehicle Theft, Kidnapping, Deceptive Practice and Stalking.
  
![probability_of_arrest](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/3c55b93d-db7a-4016-a2f2-b717816d5ee3)
![probability_of_arrest_loc](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/4149a01d-c1c5-4ea6-9f46-841a2eb4c9c9)
  
- The top 8 crimes with the MOST LIKELY arrest rate were Narcotics, Prostitution, Liquor Law Violation, Gambling, Interference with Public Officer, Concealed Carry License Violation, Weapons Violation and Obscenity. 
- The top 8 locations where arrest was MOST LIKELY was Department Store, Drug Store, Grocery Food Store, Chicago Transit Authority (CTA) Platform, Train Depot, Convenience Store, Warehouse and CTA Station 

### Arrest Probability Heatmap and Matrix
- For added granular data analysis, I cross-referenced the coefficients of crimes and their locations to create an intersectional heatmap. This visual representation shows the combinations of crime and location with the 
  probability of arrest. Each cell represents the probability, expressed as a percentage, of an arrest occurring when a specific crime is associated with a particular location.
  
![prob_of_being_arrested_heatmap_coef](https://github.com/wolfman1986/Chicago_Crime_Dataset/assets/36992236/80cc48e9-55a4-4d71-9da0-5ec6d76f8b71)

- Through our exploratory data analysis of arrest data through the application of logistic regression modeling, valuable and interesting insights have been obtained into this relationship. The 2 bar charts show the top and 
  bottom 8 most significant values for crime type and data location, clearly illustrating the coefficient deviation from the results expected in our null hypothesis. The crime and location heatmap further invalidate our null 
  hypothesis, showing a clear and decisive relationship between crime types, the locations where they are committed and the probability for arrest.

### Conclusion
- Based on our analysis, we reject our null hypothesis (H0) as the results demonstrated a non-random association between crime types, locations, and arrest probabilities. To put it simply, certain combinations of criminal 
  activity and their location exhibit higher or lower probabilities of arrests. 
