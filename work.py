'''def product(a, b):
    return a * b'''

'''def weekday_name(day_of_week):
     DAYS = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

    return DAYS[day_of_week - 1]'''

'''def last_element(lst):
    if lst:
        return lst[-1]'''

'''def number_compare(a, b):
     if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"'''

'''def reverse_string(phrase):
        return phrase[::-1]'''

'''def single_letter_count(word, letter):
    return word.lower().count(letter.lower())'''

'''def multiple_letter_count(phrase):
     counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter'''

'''def list_manipulation(lst, command, location, value=None):
     if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)

    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst'''

'''def is_palindrome(phrase):
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]'''

'''def frequency(lst, search_term):
    return lst.count(search_term)'''

'''def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out'''

'''def multiply_even_numbers(nums):
    product = 1

    for num in nums:
        if num % 2 == 0:
            product = product * num

    return product'''

'''def capitalize(phrase):
    return phrase.capitalize()'''

'''def compact(lst):
    return [val for val in lst if val]'''

'''def intersection(l1, l2):
set2 = set(l2)

    return [val for val in l1 if val in set2]'''

'''def partition(lst, fn):
    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]'''

'''def mode(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        max_value = max(counts.values())
        for (num, freq) in counts.items():
          if freq == max_value:
             return num'''

'''def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "multiply":
        res = a * b
    elif operation == "divide":
        res = a / b
    else:
        return

    if make_int:
        res = int(res)

    return f"{message} {res}"'''

'''def friend_date(a, b):
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False'''

'''def triple_and_filter(nums):
     return [num * 3 for num in nums if num % 4 == 0]'''

'''def extract_full_names(people):
    return [f"{person['first']} {person['last']}" for person in people]'''

'''def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])'''

'''def list_check(lst):
    for item in lst:
        if not isinstance(item, list):
            return False

    return True'''

'''def remove_every_other(lst):
     return lst[::2]'''

'''def sum_pairs(nums, goal):
    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()'''

'''VOWELS = set("aeiou")


def vowel_count(phrase):
    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter'''

'''def titleize(phrase):
    return phrase.title()'''

'''def find_factors(num):
    n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]

    n_list.append(num)

    return n_list'''

'''def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()

    if start is None or isinstance(collection, set):
        return sought in collection

    return sought in collection[start:]'''

'''def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None

    return phrase * num'''

'''def truncate(phrase, n):
    if n < 3:
        return "Truncation must be at least 3 characters."

    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."'''


'''def two_list_dictionary(keys, values):
    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

    return out'''

'''def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])'''

'''def freq_counter(coll):
     counts = {}

     for x in coll:
        counts[x] = counts.get(x, 0) + 1

     return counts


def same_frequency(num1, num2):
       return freq_counter(str(num1)) == freq_counter(str(num2))'''

'''def two_oldest_ages(ages):
    uniq_ages = set(ages)
    oldest = sorted(uniq_ages)[-2:]
    return tuple(oldest)'''

'''def find_the_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)'''

'''def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total'''

'''def min_max_keys(d):
        def min_max_keys(d):'''

'''def two_oldest_ages(ages):
     uniq_ages = set(ages)
     oldest = sorted(uniq_ages)[-2:]
     return tuple(oldest)'''

'''def find_the_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)'''

'''def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total'''

'''def min_max_keys(d):
     keys = d.keys()

     return (min(keys), max(keys))'''

'''def find_greater_numbers(nums):
     count = 0

     for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1

                return count'''

'''def is_odd_string(word):
    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1'''

'''def valid_parentheses(parens):
    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1
            if count < 0:
             return False

    return count == 0'''

'''def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False'''

'''def reverse_vowels(s):
    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)'''

'''def read_file_list(filename):
    with open(filename) as f:
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")'''





