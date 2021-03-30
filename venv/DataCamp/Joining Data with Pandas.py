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

