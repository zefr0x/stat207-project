# STAT-207 | Introduction to Satistics & Probability

## Final Project (Usage of Social Media Types Asociation with Personal Status and Interests)

> [!NOTE]
> Only the code for performing statistical analysis has been published as open-source.
>
> Both data sample and results of this study are private. However, data headers are avialable at [`sample.csv`](./sample.csv).

> [!NOTE]
> My focus was on statistical results rather than code quality and best practices. I improved few things, but expect ugly code 😁

### Details

- **Date:** February, 2023
- **Study Site:** Saudi Arabia’s society.
- **Objective:** Finding a link between a person's use of social networking sites and his interests or personal status.

### Variables

|                 **Variable**                  |  **Type**   |                                              **Values**                                              | Explanatory/Dependent |
| :-------------------------------------------: | :---------: | :--------------------------------------------------------------------------------------------------: | :-------------------: |
|                    Gender                     | Categorical |                                             Male,Female                                              |      Explanatory      |
|                      Age                      | Quantitate  |                                           {Integer Number}                                           |      Explanatory      |
|                  Work Status                  | Categorical |                           Student,Part-Time,Full-Time,Employer,Unemployed                            |      Explanatory      |
|                 Social Status                 | Categorical |                                       Married,Single,Divorced                                        |      Explanatory      |
|            Average Hours of Sleep             | Quantitate  |                                           {Decimal Number}                                           |      Explanatory      |
|             Religious Commitment              | Categorical |                                 {Integer Number} Percentage out of 5                                 |      Explanatory      |
|  Type of Videos Mostly Watch in Social Media  | Categorical |                               Stories,TikToks,Long Videos,Live Streams                               |       Dependent       |
|            Type of Blogs you Read             | Categorical |                                        Long Blogs,MicroBlogs                                         |       Dependent       |
|    Average Hours of Video Content pre Day     | Quantitate  |                                           {Decimal Number}                                           |       Dependent       |
|     Average Hours of Text Content pre Day     | Quantitate  |                                           {Decimal Number}                                           |       Dependent       |
|    Average Hours of Books Reading pre Day     | Quantitate  |                                           {Decimal Number}                                           |       Dependent       |
| Involved in Forum Focused on a Specific Topic | Categorical |                                                Yes,No                                                |       Dependent       |
|   Topics You Are Following in Social Media    | Categorical | [Fun],[Games],[World/Local News],[Sports],[Poeple Daily Live],[Learn/Sience],[Food],[Songs],[Random] |       Dependent       |
|    Following Friends That you Really Know     | Categorical |                                                Yes,No                                                |       Dependent       |
|    Interact with others or just watch them    | Categorical |                                         Interact,Just Watch                                          |       Dependent       |
|            Other content you Watch            | Categorical |                                     [Films],[TV Series],[Animes]                                     |       Dependent       |
|     Feel Different or Normal Among People     | Categorical |                                           Normal,Different                                           |      Explanatory      |

### Analysis Methods

> [!NOTE]
> Every Python file (from `1.py` to `11.py`) represents and implements those analysis respectively.

**Criteria for staistical significance:** p < 0.05 (α = 0.05)

#### Relations Analysis

|                                                 **Title**                                                 |               **Type**                |
| :-------------------------------------------------------------------------------------------------------: | :-----------------------------------: |
|                          Gender .vs Type of Videos Mostly Watch in Social Media                           |             Tow-Way Table             |
|             Following Friends That you Realy Know .vs Interact with others or just watch them             |             Tow-Way Table             |
|                              Age vs. Average Hours of Video Content pre Day                               | Scatter Plot, linear regression model |
|                               Age vs. Average Hours of Text Content pre Day                               | Scatter Plot, linear regression model |
| Religious Commitment .vs (Average Hours of Video Content pre Day + Average Hours of Text Content pre Day) |        Side-by-side box plots         |
|                  Type of Videos Mostly Watch in Social Media vs. Average Hours of Sleep                   |        Side-by-side box plots         |

#### Variables Analysis

|                                   **Title**                                    | **Type**  |
| :----------------------------------------------------------------------------: | :-------: |
|                  Type of Videos Mostly Watch in Social Media                   | Pie Graph |
|                             Type of Blogs you Read                             | Pie Graph |
|                    Topics You Are Following in Social Media                    | Bar Graph |
|                     Following Friends That you Realy Know                      | Pie Graph |
| Average Hours of Video Content pre Day + Average Hours of Text Content pre Day | Historam  |
