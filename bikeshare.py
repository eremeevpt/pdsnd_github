import time
import pandas as pd
import numpy as np
import calendar

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nWhich city data would you like to investigate: Chicago, New York City or Washington? Print C, NY or W to choose\n')
    city = ''
    while city.upper() != 'C' or 'NY' or 'W':
        city = input('You choose: ')
        if city.upper() != 'C' and city.upper() != 'NY' and city.upper() != 'W':
            print('Oops! There might be a misprint! Print only C or NY or W to choose a city')
            continue
        else: break
    if city.upper() == 'C':
        city = 'chicago'
    elif city.upper() == 'W':
        city = 'washington'
    else: city = 'new york city'
    print('\nThank you! You\'ve chosen: {}'.format(city.title()))
    # get user input for month (all, january, february, ... , june)
    print('\nWhich month would you like to filter by?\nPrint the month\'s corresponding ordinal from 1 to 6 to choose from January to June.\nIf you wouldn\'t like to filter by month, print \"all\".\n')
    month = ''
    while month.lower() != 'all' or month not in ['1', '2', '3', '4', '5', '6']:
        month = input('You choose: ')
        if month.lower() != 'all' and month not in ['1', '2', '3', '4', '5', '6']:
            print('Oops! There might be a misprint!\nPrint only corresponding ordinal from 1 to 6 to choose from January to June or \"all\" if you don\'t want to filter by month')
            continue
        elif month.lower() == 'all': 
            print('\nThank you! The data won\'t be filtered by month')
            break
        elif month in ['1', '2', '3', '4', '5', '6']:
            print('\nThank you! You\'ve chosen {}!'.format(calendar.month_name[int(month)])) 
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nWhich day of week would you like to filter by?\nPrint the weekday\'s corresponding ordinal from 1 to 7 to choose from Monday to Sunday.\nIf you wouldn\'t like to filter by day of week, print \"all\".\n')
    day = ''
    while day.lower() != 'all' or day not in ['1', '2', '3', '4', '5', '6', '7']:
        day = input('You choose: ')
        if day.lower() != 'all' and day not in ['1', '2', '3', '4', '5', '6', '7']:
            print('Oops! There might be a misprint!\nPrint only corresponding ordinal from 1 to 7 to choose from Monday to Sunday or \"all\" if you don\'t want to filter by day of week')
            continue
        elif day.lower() == 'all': 
            print('\nThank you! The data won\'t be filtered by day of week')
            break
        elif day in ['1', '2', '3', '4', '5', '6', '7']:
            print('\nThank you! You\'ve chosen {}!'.format(calendar.day_name[int(day)-1])) 
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    if month.lower() != 'all':
        month = int(month)
        df = df[df['month'] == month] 
    if day.lower() != 'all':
        day = int(day)-1
        df = df[df['day of week'] == day]

    return df

# This function displays time stats - the most popular hour, month and weekaday. 
# Be attentive - it displays only the beginning period of time, 
# so if the trip started at 23:59 on Sunday it will be shown as a Sunday-trip
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = calendar.month_name[df['month'].mode()[0]]
    com_month_count = len(df[df['month'] == df['month'].mode()[0]])
    print('The most common month in the given period was {}.\n In this month users took trips {} times.\n'.format(most_common_month, com_month_count))
    # display the most common day of week
    most_common_weekday = calendar.day_name[df['day of week'].mode()[0]]
    com_day_count = len(df[df['day of week'] == df['day of week'].mode()[0]])
    print('The most common day of week in the given period was {}.\n In this weekday users took trips {} times.\n'.format(most_common_weekday, com_day_count))
    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    com_hour_count = len(df[df['hour'] == df['hour'].mode()[0]])
    print('The most common hour to start a trip in the given period was {}.\n In this hour users started their trips {} times.\n'.format(most_common_hour, com_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    com_start_count = len(df[df['Start Station'] == df['Start Station'].mode()[0]])
    print('The most commonly used start station in the given period was {}.\n Users started there {} times.\n'.format(most_common_start, com_start_count))
    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    com_end_count = len(df[df['End Station'] == df['End Station'].mode()[0]])
    print('The most commonly used end station in the given period was {}.\n Users ended their trip there {} times.\n'.format(most_common_end, com_end_count))
    # display most frequent combination of start station and end station trip
    most_common_route = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    com_route_count = len(df[df['Start Station'] + ' - ' + df['End Station'] == (df['Start Station'] + ' - ' + df['End Station']).mode()[0]]) 
    print('The most common route in the given period was {}.\n Users used it {} times.\n'.format(most_common_route, com_route_count))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time in the given period was {} seconds.\n'.format(total_time), 'It is approximately {} minutes or {} hours.\n'.format(round(total_time/60,1), round(total_time/3600,1)))
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average time of a trip in the given period was {} seconds.\n'.format(mean_time), 'It is approximately {} minutes or {} hours.\n'.format(round(mean_time/60,1), round(mean_time/3600,1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts().rename_axis('USER TYPE')
    print('\nThe counts of user types are as follows:\n\n', user_count, '\n')
    # Display counts of gender

    if 'Gender' not in df.columns and 'Birth Year' not in df.columns:
        print('Unfortunately, there is no gender and birth year data for the city of Washington!\n')
    else:
        gender_count = df['Gender'].value_counts().rename_axis('USER GENDER')
        print('\nThe counts of genders are as follows:\n\n', gender_count, '\n')
        # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print('\nThe earliest year of client\'s birth is {}.\n'.format(earliest_year))
        if earliest_year < 1927:
            print(' There is probably a mistake in the database. It is hard to imagine a person of this age to use bike sharing. The result needs a double check!\n')
        recent_year = int(df['Birth Year'].max())
        print('\nThe most recent year of client\'s birth is {}.\n'.format(recent_year))
        if recent_year > 2010:
            print(' There is probably a mistake in the database. It is hard to imagine a person of this age to use bike sharing. The result needs a double check!\n')
        most_common_year = int(df['Birth Year'].mode()[0])
        com_year_count = len(df[df['Birth Year'] == df['Birth Year'].mode()[0]])
        print('\nThe most common year of client\'s birth is {}.\n There were {} users of this age.\n'.format(most_common_year, com_year_count))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        df = df.drop(['month', 'day of week', 'hour'], axis=1)

        raw = input('\nWould you like to access raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            n = 0
            m = 5
            while True:
                for i in range(n,m):
                    print (df.iloc[[i]], '\n')
                    i+=1
                raw_again = input('\nWould you like to see 5 more rows of data? Enter yes or no.\n')
                if raw_again.lower() == 'yes':
                    n+=5
                    m+=5
                    continue
                else: break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            restart_final = input('\nDoes this really mean \"no\"? If true, enter any text. If not, enter \"again\"\n')
            if restart_final.lower() != 'again':
                break


if __name__ == "__main__":
	main()
