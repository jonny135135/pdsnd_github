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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    city_names = list(CITY_DATA.keys())

    # TO DO: get user input for month (all, january, february, ... , june)
    while not (city in city_names):
        city = input(f"Input city name {city_names}: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    month = ""
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
                    'july', 'august', 'september', 'october', 'november', 'december']

    # repeat until valid month
    while not (month in valid_months):
        month = input("Input month to filter (예: 'all', 'january' ... 'december'): ").lower()

   
    day = ""
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  
    while not (day in valid_days):
        day = input("Input day of the week to filter (example: 'all', 'monday' ... 'sunday'): ").lower()

    # print the input filter information
    print(f"\\n - city: '{city}', month: '{month}', day: '{day}'")

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
    file_path = CITY_DATA[city]
    df_city = pd.read_csv(file_path)
    df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])
    df_city['Month'] = df_city['Start Time'].dt.strftime('%B').str.lower()
    df_city['Day'] = df_city['Start Time'].dt.day_name().str.lower()


    # Filter data by month and day of the week
    if (month == 'all'):
        if (day == 'all'):
            df = df_city  
        else:
            df = df_city[df_city['Day'] == day] 
    else:
        if (day == 'all'):
            df = df_city[df_city['Month'] == month]  
        else:
            df = df_city[(df_city['Month'] == month) & (df_city['Day'] == day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print(f"Most frequent Month is : {common_month}")

    # TO DO: display the most common day of week
    common_day = df['Day'].mode()[0]
    print(f"Most frequent Day is: {common_day}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour  
    common_hour = df['Hour'].mode()[0]
    print(f"most frequent hour: {common_hour}h")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most used starting station is: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most used ending station is: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    start_and_end_station = df['Start Station'] + " -> " + df['End Station']
    freq_start_and_end_station = start_and_end_station.mode()[0]
    print(f"The most common start station and end station combinations: {freq_start_and_end_station}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_hours, total_mins, total_secs = get_hours_mins_secs(total_travel_time)
    print(f"Total time is {total_hours}h {total_mins}m {total_secs}s.")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_hours, mean_mins, mean_secs = get_hours_mins_secs(mean_travel_time)
    print(f"Mean travel time is {mean_hours}h {mean_mins}m {mean_secs}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def get_hours_mins_secs(total_time):
    """Convert time in seconds to hours, minutes, and seconds."""
    hours = int(total_time // 3600)  
    mins = int((total_time % 3600) // 60)  
    secs = round(total_time % 60, 2)  
    return hours, mins, secs


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print("Count by User Type:")
    print('-'*40)
    print(f"{counts_of_user_type}\\n")


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("Number by gender:")
        print('-'*40)
        print(f"{counts_of_gender}\\n")
    else:
        print("No gende data.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = int(df['Birth Year'].min())
        print(f"Oldest birth year: {min_birth_year}")

        max_birth_year = int(df['Birth Year'].max())
        print(f"Most recent birth year: {max_birth_year}")

        common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Most frequent birth year: {common_birth_year}")
    else:
        print("No birth year data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if len(df) == 0:
            print("There is no data that meets condition")
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
