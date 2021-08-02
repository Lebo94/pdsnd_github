import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city would you like to see data from? Pick between chicago, new york city and washington: ').lower()
        if city not in CITY_DATA:
            print('Opps, looks like you put an invalid entry.Please try again\n')
            continue
            
        else:
            print('\nThank you! You will now be looking at ' + city + ' data') 
            break
            
            
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']       
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month =input('Please pick a month between january and june you are interested in, if you would like to see all the months type "all": ').lower()
        if month not in months:
            print('Please check month is spelt correctly, no acronyms')
            continue
        else: 
            break
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day =input('Please pick a day you are interested in, if you would like to see all the days type "all": ').lower()
        if day not in days_of_week:
            
            print('Please check day is spelt correctly, no acronyms')
            continue
        else: 
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Loading the data...\n')
    
         # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days_of_week.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
    i = 5       
    while True:
        data_display= input('Would you like to see the raw data, answer "yes" or "no": ')
        if data_display.lower() == 'yes':
            print(df.iloc[i-5:i,])
            i += 5    
        else: 
            break

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: '+ str(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: '+ str(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent station comination'] = df['Start Station']+" "+ df['End Station']
    print('The most frequent combination of start and end station trips is: '+ df['frequent station comination'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is: ' + str(popular_month))
          
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: '+ str(popular_day_of_week))
          
    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('The most popular start hour is: '+ str(popular_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: '+ str(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: '+ str(mean_travel_time))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The number of user types are: \n'+ str(df['User Type'].value_counts()))

    print('\nThe User demographic\n')
    print('Gender...')
    if city == 'washington':
        print('Sorry no data available')
    else:
    # TO DO: Display counts of gender
        print('The number of males and females are: \n'+ str(df['Gender'].value_counts()))
    print('\nYear of birth...')
    if city == 'washington':
        print('Sorry no data available')
    else: 
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is: '+ str(df['Birth Year'].min()) +'\nThe most recent year of birth is: '+ str(df['Birth Year'].max())+ '\nThe most common year of birth is: '+ str(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
          while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
          
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            print('\nYou have now seen all the stats')
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
