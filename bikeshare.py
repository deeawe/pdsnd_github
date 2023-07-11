# Online Python compiler (interpreter) to run Python online.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('what city would you like to analyze? ').lower()
    while city not in VALID_CITIES:
        city = input('invalid input. Try again: ').lower()
    
    # get user input for month (all, january, february, ... , june)
    month = input('what month would you like to analyze? ').lower()
    while month not in VALID_MONTHS:
        month = input('invalid input. Try again: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('what day would you like to analyze? ').lower()
    while day not in VALID_DAYS:
        day = input('invalid input. Try again: ').lower()

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
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def display_data(df):
    five_rows = input("do you want to print the first 5 rows? (yes/no): ").lower()
    start = 0
    end = 5
    while five_rows  == "yes":
        print (df.iloc[start:end])
        five_rows = input("do you want to print the next 5 rows? (yes/no): ").lower()
        start += 5
        end += 5
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month: ', most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('most common day: ', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('most common hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('most common start station: ', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('most common end station: ', most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_and_end_station = (df['Start Station'] +' and '+ df['End Station']).mode()[0]
    print('most common start and end station: ', most_common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('number of user types: ', count_user_type)

    # Display counts of gender
    count_gender = df['Gender'].value_counts()
    print('number of genders: ', count_gender)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print('earliest birth year: ', earliest_birth_year)
    
    most_common_birth_year = df['Birth Year'].max()
    print('most recent birth year: ', most_common_birth_year)
    
    most_common_birth_year = df['Birth Year'].mode()[0]
    print('most common birth year: ', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
