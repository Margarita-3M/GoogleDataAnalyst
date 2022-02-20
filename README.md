<h1 align='center'> Cyclistic: How do annual members and casual riders use Cyclistic bikes differently? </h1>

This case study is part of Google Data Analytics Certificate. The info about the case study is available [here](case_study_info.pdf). </br>
I will use Data Analysis Framework offered by Google to proceed with the case study:
1. [Ask](#step-1-ask)
2. [Prepare](#step-2-prepare)
3. [Process](#step-3-process)
4. [Analyze](#step-4-analyze)
5. [Share](#step-5-share)
6. [Act](#step-6-act)

# Step 1 Ask
**What is the problem we are trying to solve?**
## The Background:
Marketing Team is working on marketing strategies aimed at converting casual riders into annual members. In order to do that, they want to understand how annual members and casual riders differ.
## 1.1 The Business Task
Based on the most current data (2021, February - 2022, January):
* Assess if members and casual riders use Cyclistic bikes differently.
* If the differences exist:
    * determine how members and casual riders differ, 
    * and generate recommendations based on this analysis for the Cyclistic's marketing team to design marketing strategies for converting casual riders into members.
## 1.2 Stakeholders
* Lily Moreno: The director of marketing;
* Cyclistic executive team: The notoriously detail-oriented executive team will decide whether to approve the recommended marketing program.

# Step 2 Prepare
**What data do we need to answer the questions?**

## 2.1 Data sources
We will use *Cyclistic trip data* to analyze and identify patterns (if any) - [link](https://divvy-tripdata.s3.amazonaws.com/index.html). 
**Note_1:** The datasets have a different name because Cyclistic is a fictional company. The data has been made available by Motivate International Inc. under this [license](https://www.divvybikes.com/data-license-agreement).

- Data source meets ROCC standard:
    - *R*eliable;
    - *O*riginal;
    - *C*omprehensive;
    - *C*urrent;
    - *C*ited.

### 2.2 Details on the data
- Data is first-party data, generated internally on monthly basis by Cyclistic marketing analytics team.
- Data is 12 separate csv files, with 13 columns in each file, in a wide format. 
- Data range covered: 2021, February - 2022, January.
- Data is structured.

### 2.3 Data Ethics
- Data-privacy issues prohibit anyone from using riders’ personally identifiable information.
- Due to the above, we won’t be able to connect pass purchases to credit card numbers to determine e.g.:
    - if casual riders live in the Cyclistic service area
    - or if they have purchased multiple single passes.

## Step 3 Process
**Cleaning data and making it ready for analysis**
- I wrote 2 scripts
    - to combine all 12 csv files into one file and correct data types;
    - to clean data, remove missing data and duplicates

## Step 4 Analyze
**It's time to let the data speak for itself**
### I store data at:
- GitHub
- Tableau Public

### Data Vizuals
- have been made using Tableau Public - [link](https://public.tableau.com/app/profile/margarita8108/viz/GoogleDA_16453619905540/Dashboard1)

## Step 5 Share
**Insights generated from the analysis**
- Members and casual riders differ;
- 45% Cyclistic trips are made by casual riders. This is quite impressive number;
- Casual riders prefer warm and dry months;
- Most of casual rides are made on weekends;
- The most popular time for casual riders is 17 p.m.

#### Based on my analysis, I summarize that annaul members and casual riders use Cyclistic bikes differently via:
- seasons
- bike types
- bike ride lengths
- weekdays vs. weekends
- bike stations

## Step 6 Act
**Recommendations**
From 2021, February - to 2022, January, 45% of rides were made by casual riders. This is a huge piece of market which could potentionally switch to membership scheme.
1. Offer weekend membership for those who prefer to bike on weekends
2. Propose off-rush hours discounts for thos who bike before 7 a.m. and after 18 p.m.
3. Propose warm months membership for those who tend to travel by byke during warm and dry months.
