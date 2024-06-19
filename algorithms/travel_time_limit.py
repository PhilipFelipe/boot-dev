def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    while time_left >= time_in_country:
        time_left -= time_in_country
        print("TIME LEFT: ", time_left)
        time_in_country *= factor
        print("TIME IN COUNTRY: ", time_in_country)
        count += 1
    return count


if __name__ == "__main__":
    print(num_countries_in_days(1, 0.5))
