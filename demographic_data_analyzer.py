import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts("race")

    # What is the average age of men?
    average_age_men = round(sum(df.loc[df['sex'] == 'Male', 'age'])/ len(df.loc[df['sex'] == 'Male']), 1)

    # What is the percentage of people who have a Bachelor's degree?
    educationPercentage = df.value_counts("education", normalize=True)
    percentage_bachelors = round(educationPercentage['Bachelors'] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = percentage_bachelors + educationPercentage['Masters'] + educationPercentage['Doctorate'] 
    lower_education = 1 - higher_education

    # percentage with salary >50K
    numberOfRichHigher = len(df.loc[ ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K'), ['education', 'salary'] ])
    totalNumberOfHigher = len(df.loc[ ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) ])
    higher_education_rich = round( (numberOfRichHigher/totalNumberOfHigher) * 100, 1)
    numberOfRichLower = len(df.loc[ ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K'), ['education', 'salary']])
    totalNumberOfLower = len(df) - totalNumberOfHigher
    lower_education_rich = round( (numberOfRichLower/ totalNumberOfLower) * 100, 1 )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours]) 

    rich_percentage = round( (len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] =='>50K')]) / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    number_of_high_earners_per_country = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    number_of_people_per_country = df['native-country'].value_counts()
    percentage = number_of_high_earners_per_country/number_of_people_per_country
    highest_earning_country_percentage = round(percentage.max()* 100, 1)
    highest_earning_country = percentage[percentage == percentage.max()].index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[ (df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts('occupation').index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
