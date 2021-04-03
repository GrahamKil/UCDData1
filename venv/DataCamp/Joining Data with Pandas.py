### Data Merging Basics
## Inner Join


# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on= 'vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)






##   SUFFIXES
# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))


# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())




# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)
> >> <script.py> output:
    wards_census table shape: (50, 9)




# Print the first few rows of the wards_altered table to view the change
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)
> >> <script.py> output:
> >> ward
0   61
1    2
2    3
3    4
4    5
wards_altered_census table shape: (49, 9)






# Print the first few rows of the census_altered table to view the change
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)
> >> <script.py> output:
> >>    ward
0  None
1     2
2     3
3     4
4     5
wards_census_altered table shape: (49, 9)









### One to Many relationships
## One to many merge

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head()))
> >> <script.py> output:
> >>                 account
title
PRESIDENT           6259
SECRETARY           5205
SOLE PROPRIETOR     1658
OTHER               1200
VICE PRESIDENT       970








### Merging 3 or more tables  backslash needed \
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations)






## Total number of Rides in a month

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == 'Weekday')
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())







## Three table merge
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))
> >> <script.py> output:
> >>                            income
alderman
Ameya Pawar                 66246
Anthony A. Beale            38206
Anthony V. Napolitano       82226
Ariel E. Reyboras           41307
Brendan Reilly             110215
Brian Hopkins               87143
Carlos Ramirez-Rosa         66246
Carrie M. Austin            38206
Chris Taliaferro            55566
Daniel "Danny" Solis        41226
David H. Moore              33304
Deborah Mell                66246
Debra L. Silverstein        50554
Derrick G. Curtis           65770
Edward M. Burke             42335
Emma M. Mitts               36283
George Cardenas             33959
Gilbert Villegas            41307
Gregory I. Mitchell         24941
Harry Osterman              45442
Howard B. Brookins, Jr.     33304
James Cappleman             79565
Jason C. Ervin              41226
Joe Moore                   39163
John S. Arena               70122
Leslie A. Hairston          28024
Margaret Laurino            70122
Marty Quinn                 67045
Matthew J. O'Shea           59488
Michael R. Zalewski         42335
Michael Scott, Jr.          31445
Michelle A. Harris          32558
Michelle Smith             100116
Milagros "Milly" Santiago   41307
Nicholas Sposato            62223
Pat Dowell                  46340
Patrick Daley Thompson      41226
Patrick J. O'Connor         50554
Proco "Joe" Moreno          87143
Raymond A. Lopez            33959
Ricardo Munoz               31445
Roberto Maldonado           68223
Roderick T. Sawyer          32558
Scott Waguespack            68223
Susan Sadlowski Garza       38417
Tom Tunney                  88708
Toni L. Foulkes             27573
Walter Burnett, Jr.         87143
William D. Burns           107811
Willie B. Cochran           28024












### One to many merge with multiple tables
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))



# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'],
                                   as_index=False).agg({'account':'count'})







# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'],
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'],
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
> >> <script.py> output:
> >>          ward  pop_2010  vacant  account
47    7     51581      19       80
12   20     52372      15      123
1    10     51535      14      130
16   24     54909      13       98
7    16     51954      13      156













### Left Join
## Counting Missing rows with left Join

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, how='left')


# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)
> >> <script.py> output:
> >> 1574








## ENRICHING A DATASET

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
> >> < script.py > output:       id        title  popularity release_date                   tagline
0  10193  Toy Story 3   59.995418   2010-06-16  No toy gets left behind.
1    863  Toy Story 2   73.575118   1999-10-30        The toys are back!
2    862    Toy Story   73.640445   1995-10-30                       NaN
(3, 5)



# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
> >> < script.py > output:        id        title  popularity release_date                   tagline
    0  10193  Toy Story 3   59.995418   2010-06-16  No toy gets left behind.
    1    863  Toy Story 2   73.575118   1999-10-30        The toys are back!
    (2, 5)










### RIGHT JOIN TO FIND UNIQUE MOVIES

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')


# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())
> >> < script.py > output:  movie_id genre_act        genre_sci
    0        11    Action  Science Fiction
    1        18    Action  Science Fiction
    2        95    Action  Science Fiction
    3       106    Action  Science Fiction
    4       154    Action  Science Fiction


# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]



# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner',
        left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)
> >> < script.py > output:       id                         title  popularity release_date  movie_id genre_act        genre_sci
    0  18841  The Lost Skeleton of Cadavra    1.680525   2001-09-12     18841       NaN  Science Fiction
    1  26672     The Thief and the Cobbler    2.439184   1993-09-23     26672       NaN  Science Fiction
    2  15301      Twilight Zone: The Movie   12.902975   1983-06-24     15301       NaN  Science Fiction
    3   8452                   The 6th Day   18.447479   2000-11-17      8452       NaN  Science Fiction
    4   1649    Bill & Ted's Bogus Journey   11.349664   1991-07-19      1649       NaN  Science Fiction
    (258, 7)






### POPULAR GENRES WITH RIGHT JOIN
# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                      left_on='movie_id', right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()



# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) |
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
> >> < script.py > output:  character_1      id           name_1 character_2 name_2
    0                       Yinsen   17857       Shaun Toub         NaN    NaN
    2  Obadiah Stane / Iron Monger    1229     Jeff Bridges         NaN    NaN
    3                  War Machine   18288  Terrence Howard         NaN    NaN
    5                         Raza   57452      Faran Tahir         NaN    NaN
    8                   Abu Bakaar  173810    Sayed Badreya         NaN    NaN







###  SELF JOIN - MERGING A TABLE TO ITSELF

# Merge the crews table to itself
crews_self_merged = crews.merge(crews,on='id', how='inner', suffixes=('_dir', '_crew'))


# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a Boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]


# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())
> >> < script.py > output:  id   job_dir       name_dir        job_crew          name_crew
    156  19995  Director  James Cameron          Editor  Stephen E. Rivkin
    157  19995  Director  James Cameron  Sound Designer  Christopher Boyes
    158  19995  Director  James Cameron         Casting          Mali Finn
    160  19995  Director  James Cameron          Writer      James Cameron
    161  19995  Director  James Cameron    Set Designer    Richard F. Mays







# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())
> >> < script.py > output:   id
257            Oliver Twist   20.415572   2005-09-23           6.7       274.0
14290  Better Luck Tomorrow    3.877036   2002-01-12           6.5        27.0
38365             Grown Ups   38.864027   2010-06-24           6.0      1705.0
9672               Infamous    3.680896   2006-11-16           6.4        60.0
12819       Alpha and Omega   12.300789   2010-09-17           5.3       124.







# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']








# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]





# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())











#### FILTERING JOINS
### semi-join
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])






# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))







### Concatenate DataFrames together vertically
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)



# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)



# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)








### Concatenating with keys

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                            keys=['7Jul','8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()








### Using the append method

# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(['quantity'], ascending=False))







### Verifying integrity
## Concatenate and merge to find common songs

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)




# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid', how='inner')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
> >> < script.py > output:
        pid   tid
    3    12  3479
    10   12  3439
    21   12  3445
    23   12  3449
    48   12  3437
    50   12  3435











### USING MERGE_ORDERED()
## Correlation between GDP and S&P500

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left')

# Print gdp_sp500
print(gdp_sp500)
> >> < script.py > output:
 country code  year           gdp    date  returns
0          USA  2010  1.499210e+13  2010.0    12.78
1          USA  2011  1.554260e+13  2011.0     0.00
2          USA  2012  1.619700e+13  2012.0    13.41
3          USA  2012  1.619700e+13  2012.0    13.41
4          USA  2013  1.678480e+13  2013.0    29.60
5          USA  2014  1.752170e+13  2014.0    11.39
6          USA  2015  1.821930e+13  2015.0    -0.73
7          USA  2016  1.870720e+13  2016.0     9.54
8          USA  2017  1.948540e+13  2017.0    19.42
9          USA  2018  2.049410e+13     NaN      NaN






# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left',  fill_method='ffill')

# Print gdp_sp500
print (gdp_sp500)
> >> < script.py > output:
        country code  year           gdp  date  returns
    0          USA  2010  1.499210e+13  2010    12.78
    1          USA  2011  1.554260e+13  2011     0.00
    2          USA  2012  1.619700e+13  2012    13.41
    3          USA  2012  1.619700e+13  2012    13.41
    4          USA  2013  1.678480e+13  2013    29.60
    5          USA  2014  1.752170e+13  2014    11.39
    6          USA  2015  1.821930e+13  2015    -0.73
    7          USA  2016  1.870720e+13  2016     9.54
    8          USA  2017  1.948540e+13  2017    19.42
    9          USA  2018  2.049410e+13  2017    19.42





# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())
> >> < script.py > output:
              gdp   returns
gdp      1.000000  0.212173
returns  0.212173  1.000000







# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on='date', how='inner')

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter')
plt.show()
> >> < script.py > output:
date      cpi     seriesid                  data_type  unemployment_rate
    0  2014-01-01  235.288  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.7
    1  2014-06-01  237.231  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.1
    2  2015-01-01  234.718  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.6
    3  2015-06-01  237.684  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.3
    4  2016-01-01  237.833  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.0
    5  2016-06-01  240.167  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.9
    6  2017-01-01  243.780  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.7
    7  2017-06-01  244.182  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.3
    8  2018-01-01  248.884  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.1
    9  2018-06-01  251.134  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.0








## merge_ordered() caution, multiple columns

# Merge gdp and pop on date and country with fill and notice rows 2 and 3

ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'],
                             fill_method='ffill')
# Print ctry_date
print(ctry_date)
<script.py> output:
             date    country           gdp  series_code_x       pop series_code_y
    0  1990-01-01  Australia  158051.13240  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
    1  1990-01-01     Sweden   79837.84599  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    2  1990-04-01  Australia  158263.58160  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    3  1990-04-01     Sweden   80582.28597  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    4  1990-07-01  Australia  157329.27900  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    5  1990-07-01     Sweden   79974.36017  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    6  1990-09-01  Australia  158240.67810  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    7  1990-09-01     Sweden   80106.49738  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
    8  1991-01-01  Australia  156195.95350  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
    9  1991-01-01     Sweden   79524.24192  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    10 1991-04-01  Australia  155989.03270  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    11 1991-04-01     Sweden   79073.05901  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    12 1991-07-01  Australia  156635.85760  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    13 1991-07-01     Sweden   79084.77036  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    14 1991-09-01  Australia  156744.05660  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    15 1991-09-01     Sweden   79740.60625  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
    16 1992-01-01  Australia  157916.08110  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
    17 1992-01-01     Sweden   79390.92175  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    18 1992-04-01  Australia  159047.82710  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    19 1992-04-01     Sweden   79060.28298  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    20 1992-07-01  Australia  160658.17600  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    21 1992-07-01     Sweden   78904.60477  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    22 1992-09-01  Australia  163960.22070  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    23 1992-09-01     Sweden   76996.83684  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
    24 1993-01-01  Australia  165097.49510  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
    25 1993-01-01     Sweden   75783.58777  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    26 1993-04-01  Australia  166027.05900  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    27 1993-04-01     Sweden   76708.54823  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    28 1993-07-01  Australia  166203.17860  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    29 1993-07-01     Sweden   77662.01816  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    30 1993-09-01  Australia  169279.34790  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
    31 1993-09-01     Sweden   77703.30364  NYGDPMKTPSAKD   8718561   SP.POP.TOTL



# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'],
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)
<script.py> output:
         date    country           gdp  series_code_x       pop series_code_y
0  1990-01-01  Australia  158051.13240  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
1  1990-04-01  Australia  158263.58160  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
2  1990-07-01  Australia  157329.27900  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
3  1990-09-01  Australia  158240.67810  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
4  1991-01-01  Australia  156195.95350  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
5  1991-04-01  Australia  155989.03270  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
6  1991-07-01  Australia  156635.85760  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
7  1991-09-01  Australia  156744.05660  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
8  1992-01-01  Australia  157916.08110  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
9  1992-04-01  Australia  159047.82710  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
10 1992-07-01  Australia  160658.17600  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
11 1992-09-01  Australia  163960.22070  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
12 1993-01-01  Australia  165097.49510  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
13 1993-04-01  Australia  166027.05900  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
14 1993-07-01  Australia  166203.17860  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
15 1993-09-01  Australia  169279.34790  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
16 1990-01-01     Sweden   79837.84599  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
17 1990-04-01     Sweden   80582.28597  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
18 1990-07-01     Sweden   79974.36017  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
19 1990-09-01     Sweden   80106.49738  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
20 1991-01-01     Sweden   79524.24192  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
21 1991-04-01     Sweden   79073.05901  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
22 1991-07-01     Sweden   79084.77036  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
23 1991-09-01     Sweden   79740.60625  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
24 1992-01-01     Sweden   79390.92175  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
25 1992-04-01     Sweden   79060.28298  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
26 1992-07-01     Sweden   78904.60477  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
27 1992-09-01     Sweden   76996.83684  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
28 1993-01-01     Sweden   75783.58777  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
29 1993-04-01     Sweden   76708.54823  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
30 1993-07-01     Sweden   77662.01816  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
31 1993-09-01     Sweden   77703.30364  NYGDPMKTPSAKD












### USING merge_asof()

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time',
                              suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()







# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color='r', rot=90)
plt.show()

















### Selecting data with .query()

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country', 'date'],
                             fill_method='ffill')




## SUBSETTING ROWS WITH .QUERY()

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']



# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot table of gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')




# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()










### Reshaping data with .melt()
## Using .melt() to reshape government data

# Unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month',
                       value_name='unempl_rate')

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()





# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date',
                            suffixes=('_dow', '_bond'), how='inner')

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()