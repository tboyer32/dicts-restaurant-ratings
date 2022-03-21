"""Restaurant rating lister."""
import sys
# put your code here
# bring in file scores.txt

def get_user_input:
    while True:
        choice = input("Enter 1 to see all ratings \n" +
                        "Enter 2 to add a new restaurant and it's rating " +
                        "Enter q to quit ")
        # if statements
    


def tokenize_file():
    file_name = open(sys.argv[1])
    restaurant_ratings = {}
    # remove white space
    # tokenized each line
    # store name of restaurant and rating in dictionary
    for line in file_name:
        line = line.rstrip()
        restaurant_info = line.split(":")
        restaurant_ratings[restaurant_info[0]] = restaurant_info[1] 

    return restaurant_ratings



# define a function to add new restaurant and rating
user_restaurant = input("Enter a restaurant name: ")

while True:
    try:
        user_rating = int(input("Enter the rating: "))
        if 1 <= user_rating <= 5:
            break
        else:
            print("Please enter user rating between 1-5.")
    except ValueError:
        print("Oops that's not a valid number. Please try again.")

restaurant_ratings[user_restaurant] = user_rating

# sort in alphabetical order and print
# define another function to print
sorted_ratings = sorted(restaurant_ratings)
for name in sorted_ratings:
    print(f"{name} is rated at {restaurant_ratings[name]}.")





# filename = sys.argv[1]
# tokens = tokenize(filename)
# word_counts = count_words(tokens)
# print_words(word_counts)



