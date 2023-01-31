def basic_function(my_input):
    print(my_input)

basic_function("this is the basic function")

my_second = lambda my_second: print(my_second)

my_second("this is the lambda output")



# create a lambda function which will return true if number is greater than 10 eles false

true_false = lambda number: True if number > 10 else False

print(true_false(13))


print_greetings = lambda : print("Good morning!!")

print_greetings()


our_list = [1,3,4,5,6]

double = map(lambda input: input *2, our_list)

print(list(double))