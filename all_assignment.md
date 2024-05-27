# Assignment

We told you we would be revisiting `contains_duplicates`!
This time, you'll implement it using sets.

So, what's a set?
Well, let's compare them to lists, as its easier to define sets in terms of their differences.

Lists are boring.
They store values, and they keep track of where you put each value.
Lists excel when you ask them 'give me item #5', but that's mostly it.
Other operations are rather slow:

* Inserting an element requires all later elements to be moved one spot.
  Same for deleting elements.
* Checking if an element is in a list is slow: you need to go through the entire list.
  Imagine having to look up a word in a dictionary whose words are not sorted alphabetically.

A set can do all of this much faster.
Sets are the best!

Admittedly, there's a catch.
You have to give something in return: sets get to choose themselves how they order their elements internally, meaning you can't assign indices to elements.
Also, a set can contain an element at most once.
Adding some value `x` to a set that already contains `x` does literally nothing:

```python
>>> xs = {1, 2, 3}
>>> xs.add(1)
>>> xs
{1, 2, 3}

>>> xs.add(0)
>>> xs
{0, 1, 2, 3}
```

Now, find a way to implement `contains_duplicates` using a set.
After you have solved this exercise, you can run `benchmark.py`: it measures the difference in time between a naive implementation and one that uses sets.
You will see the set-based solution easily runs 1000x faster for larger lists.


# AssocList

An _associative container_ is a container that, well, associates "keys" with "values".
Okay, that's pretty vague.
Maybe a few examples can help.

* A English-to-French dictionary associates English words with their French translation.
  Here, the _key_ is the English word and the _value_ is the French translation.
* An attendance sheet associates names (= key) with a boolean value (= value), indicating whether that particular someone is present or not.
* An item catalog associates items (= keys) with their prices (= values).

Notice how it typically only works well in one direction: given an English word, it is easy to look up the French translation in an English-to-French dictionary, but it'd take a lot more effort to do the opposite.

We want to create a class named `AssocList` that allows us to store such associations.
Here's an example of how we could use it:

```python
# Create an empty dictionary
>>> en_to_fr = AssocList()

# Populating our dictionary
>>> en_to_fr['cat'] = 'chat'
>>> en_to_fr['dog'] = 'chien'
>>> en_to_fr['cheese'] = 'fromage'

# Look up translations
>>> word = 'cat'
>>> f'The translation of {cat} is {en_to_fr(cat)}.'
'The translation of cat is chat.'
```

## Implementation

The goal of this exercise is to define the `AssocList` class.

We know `AssocList` needs to keep track of the key/value associations, meaning we need a way to store them.
There are many ways to do this, and you are free to pick your own.
Here, we will discuss how to use a list of pairs.

The idea is very simple: each `key`/`value` pair association is stored in a pair `[key, value]`.
Typically pairs are represented using tuples, but here we'll use a list so that we can modify them when needed (see later.)
All these pairs need to be stored somewhere, so we'll just dump them in a list: `[[key1, value1], [key2, value2], ...]`.

For example, the English to French dictionary above would be represented using

```python
[
    ['cat', 'chat'],
    ['dog', 'chien'],
    ['cheese', 'fromage']
]
```

### Empty AssocList

Let's start with defining the class `AssocList`.
Initially, an `AssocList` should be empty, which we can represent using the empty list `[]`.

```python
class AssocList:
    def __init__(self):
        self.__items = []
```

### Adding New Key/Value Pairs

Say we want to add a new association `key`/`value` to the `AssocList`.

```python
>>> assoc_list = AssocList()

>>> assoc_list['cat'] = 'chat'
```

First, we need to determine which method to define in order to make this assignment possible.
In this case, this is dunder method `__setitem__(self, key, value)`:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # ???
```

As explained in a previous section, `assoc_list['cat'] = 'chat'` is translated into `assoc_list.__setitem__('cat', 'chat')`.

Adding a new key/value pair should be straightforward: we can simply `append` the pair to the list:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # append [key, value] to __items
```

However, what what if a `key` already exists in our `AssocList`?
In this case, we want the new value to overwrite the old one.

```python
>>> assoc_list = AssocList()

>>> assoc_list['cat'] = 'chot'
# 'cat' is associated with 'chot'

>>> assoc_list['cat'] = 'chat'
# Now 'cat' should be associated with 'chat' instead
```

To achieve this, we need to refine our logic somewhat:

```python
class AssocList:
    # ...

    def __setitem__(self, key, value):
        # find pair in __items that has pair[0] == key
        # if no such pair can be found
        #   append [key, value] to __items
        # else
        #   overwrite pair[1] with value
```

### Looking Up

Given a key, we want to be able to ask the `AssocList` what value is associated with it:

```python
>>> assoc_list = AssocList()
>>> assoc_list['cat'] = 'chat'

# Ask what's associated with cat
>>> assoc_list['cat']
'chat'
```

To allow this `assoc_list[key]` syntax, we need to define `__getitem__(self, key)`.
The above lookup `assoc_list['cat']` corresponds to `assoc_list.__getitem__('cat')`.

```python
class AssocList:
    # ...

    def __getitem__(self, key):
        # ???
```

Here, we need to write code that goes through `__items__` and looks for the `pair` for which `pair[0] == key`.
When it finds such a pair, `__getitem__` should return the corresponding value.
If no such pair can be found, raise an error (`raise KeyError()`).

## Task

Define a class `AssocList` with the following members:

* A constructor that creates an empty `AssocList`.
* `assoc_list[key] = value` associates `key` with `value`.
  If `assoc_list` already associates `key` with something, it is overwritten by `value`.
* `key in assoc_list` checks if `key` appears in `assoc_list`. Hint: `__contains__`.
* `assoc_list[key]` returns the `value` associates with `key`.
* `len(assoc_list)` returns the number of key/value pairs.
* `assoc_list.keys` returns a list of keys.
* `assoc_list.values` returns a list of values.
# CLASSES

A class is a special type of value in an object-oriented programming language like Python. Just like a string, integer or float, a class is essentially a custom type that has some special properties.

An object is an instance of a class type. In this example, health is an instance of an integer type.

```python
health = 50
```

In `object-oriented programming`, we create special types called "classes". And each instance of a class is called an "object".

## HOW DO I CREATE A CLASS?

In Python, you just need to use the `class` keyword, and you can set custom properties in the following way. It is a common convention in Python to capitalize the first character in the name of your class.

```python
class Soldier:
    health = 5
```

Then to create an instance of a `Soldier` we simply call the class. Notice that a class isn't a function. It doesn't take input parameters directly.

```python
first_soldier = Soldier()
print(first_soldier.health)
# prints "5"

```

# Task

Create a class called `Wall` on line 1. It should have a property called `armor` that is initialized to `10` and a `height` that starts at `5`.
# METHODS

After the last exercise, you might be wondering why classes are useful, they seem like `dictionaries` but worse!

What makes classes cool is that they allow us to define custom `methods` on them. A method is a function that is associated with a class, and it has access to all the properties of the object.

```python
class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"
```

## THE SPECIAL "SELF" VALUE


As you can see, methods are nested within the class declaration. Methods always take a special parameter as their first argument called `self`. The self variable is a reference to the object itself, so by using it you can read and update the properties of the object.

Notice that methods are called directly on an object using the dot operator.

```python
object.method()
```

# Task

Add a `fortify()` method to your wall class. It should double the current `armor` property.

# METHODS CAN RETURN VALUES

If a normal function doesn't return anything, it's typically not a very useful function. In contrast, methods often don't return anything explicitly because they may mutate the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values!

```python
class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"
```

# ASSIGNMENT

Add a `.get_cost()` method to your `wall` class. What would you expect it to return?

The cost of a wall is the product of its height and armor:

```
cost = armor * height
```
# METHODS VS FUNCTIONS

## WHAT IS A FUNCTION?
A function is a piece of code that is called by a name. It can receive data to operate on through parameters and may, optionally, return data. All data that is passed to a function is explicitly passed through parameters.

## WHAT IS A METHOD?
A method is a piece of code that is called by a name that is associated with an object. Methods and functions are similar but have two key differences.

1. A method is implicitly passed the object on which it was called. In other words, you won't see all the inputs in the parameter list.
2. A method can operate on data that is contained within the class. In other words, you won't see all the outputs in the return statement.

## THE OOP DEBATE
Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.

For example, while methods are more implicit and often make code more difficult to read, they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase.


# CONSTRUCTORS (OR INITIALIZERS)

It's quite rare in the real world to see a class that defines properties in the way we've been doing it.

```python
class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2
```

It's much more practical to use a `constructor`. In Python, the constructor is the `__init__()` method, and it is called when a new object is created.

So, with a constructor, the code would look like this.

```python
class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2
```

However, because the constructor is a method, we can now make the name, starting armor and number of weapons configurable with some parameters.

```python
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"
```

# Task

Add a constructor to our `Wall` class. It should take `depth`, `height` and `width` as parameters, in that order, and set them as properties. It should also compute an additional property called `volume`. Volume is the width times height times depth.
# MULTIPLE OBJECTS

If a class is just a type, then an object is just a value.

You'll hear often that an object is an "instance" of a class. Let's look at what that word means.

```
In object-oriented programming, an instance is a concrete occurrence of any object... "Instance" is synonymous with "object" as they are each a particular value... "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.
-- Wikipedia
```

So for our wall class, I can create three different "instances" of the class. Or in other words, I'll create three separate objects.

```python
wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)
```

In the example above, `Wall` and `Integer` are types, and each variable is an instance of one of those types.

# Task

Take a look at the `Brawler` class and the `fight` function provided. In the `main` function, create 4 new brawlers with the following stats:

- Name: Aragorn. Speed: 4. Strength: 4.
- Name: Gimli. Speed: 2. Strength: 7.
- Name: Legolas. Speed: 7. Strength: 7.
- Name: Frodo. Speed: 3. Strength: 2.
Then call fight twice. The first fight should be Aragorn vs Gimli. The second will be Legolas vs Frodo.
# CLASS VARIABLES VS INSTANCE

## VARIABLES
So far we've worked with both class variables and instance variables, but we haven't talked about the difference yet. Below are 2 code samples that demonstrate the variable height being declared as an instance variable, and a class variable.

## INSTANCE VARIABLES
Instance variables vary from object to object and are declared in the constructor.

```python
class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"
```

## CLASS VARIABLES
Class variables remain the same between instances of the same class and are declared at the top level of a class definition.

```python
class Wall:
    height = 10

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height)
# prints "20"
```

## WHICH SHOULD I USE?
Generally speaking, stay away from class variables. Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making data updates. However, it is important to understand how they work because you may see them out in the wild.

## ASSIGNMENT
Due to our terrible class design, some lazy code owned by a different development team is causing some bugs in our class. We can fix it by using instance variables instead of class variables.

In the `main()` function (that our team isn't responsible for), a line like `Dragon.element = "fire"` should not affect our existing dragon instances! We don't like near-global variables. We want our users to specify each dragon's element in the constructor.

Update the `Dragon` class. Remove the `element` class variable and instead use an instance variable that's configurable via the constructor.

# ENCAPSULATION
Encapsulation is one of the strongest tools in your tool belt as a software engineer. As we covered in chapter one, writing code that machines understand is easy, but writing code that humans can understand is very difficult.

Encapsulation is the practice of hiding information inside a ["black box"](https://en.wikipedia.org/wiki/Black_box) so that other developers working with the code don't have to worry about it.

## ENCAPSULATION IN OOP
In the context of object-oriented programming, we can practice good encapsulation by using [private](https://docs.python.org/3/tutorial/classes.html#tut-private) and public members. The idea is that if we want the users of our class to interact with something directly, we make it public. If they don't need to use a certain method or property, we make that private to keep the usage instructions for our class simple.

## ENCAPSULATION IN PYTHON
To enforce encapsulation in Python, developers prefix properties and methods that they intend to be private with a double underscore.

```python
class Wall:
    def __init__(self, height):
        # this stops us from accessing the __height
        # property directly on an instance of a Wall
        self.__height = height

    def get_height(self):
        return self.__height
```

In the example above, we don't want users of the `Wall` class to be able to change its height. We make the `__height` property private and expose a public `get_height` method so that users can still read the height of a wall without being tempted to update it. This will stop developers from being able to do something like:

```python
# front_wall is an instance of a Wall
front_wall.__height = 10 # this results in an error

```

## ASSIGNMENT
Complete the `Wizard` class. Its constructor should take a `name` as input. It should set the public name property to the given name. It should also initialize private `__mana` and `__health` properties to `45` and `65` respectively.

Create two "getter" methods. One called `get_mana()` and one called `get_health()`. They should return the current mana and health of the class instance respectively.
# Task

Create a class `Account`.

* It should have a publically accessible attribute `login`.
* It should have a private attribute `password`.
* Both these attributes must be initialized by constructor parameters.
* Provide a method `is_correct_password(self, pw)` that checks if `pw` is equal to the password.

## Important

We have to admit that the `Account` class is actually a _really_ bad example.
We only used it because it is very intuitive to want to hide a password, which gives us an easy to explain reason for as why we would want to hide members.

In reality, "hidden" members are still very easily accessible in Python, so the password is still very much exposed.
Python's method of hiding attributes is not meant as a safety feature, but simply as a way to convey intent.
It protects against Murphy, but not against Machiavelli.

Also, as a general rule, passwords are *never* stored, regardless of the technology used, i.e., this is not a Python-specific rule.
For example, websites such as Google, Amazon, Reddit, etc. never store your password as it would be incredibly unsafe to do so.
If you're wondering how a website can check whether your password is correct without having access to it, feel free to ask your lecturer.
# Queue

## Concepts Used

* Classes
* Access control

## Some Explanation

Imagine you go to your favorite sandwich shop (which of course is 't Smullerke).
Sadly it's around noon, so the there's a long queue of two dozen people.
Oh well, at least there's five people working in parallel, so the wait is bearable.

Let us focus on this queue thing, what exactly is it?
Well, it's kind of a "list" of people.
When someone wants to buy a sandwich, that person must take place at the very end of the queue.

When a worker is ready, he or she will serve the next customer in the queue.
That person is the one in the front of the queue.

So, in essence:

* Adding a customer to the queue = adding them at the *end* of the list
* Retrieving a customer from the queue = removing them from the *beginning* of the list

## Task

We want to implement queues in Python.

* Create a class `Queue`.
* Its constructor takes no parameters.
  A new queue is initially empty.
* Add a method `add(self, item)` to add an item to the queue.
* Add a method `next(self)` that removes and returns the next item from the queue.
* Add a method `is_empty(self)` that checks if the queue is empty.

It is important that `add` and `next` behave as described above:

```python
# Create an empty queue
queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

queue.next()   # Alice arrived first, so she's the first to be served next
queue.next()   # This must return Bob
queue.next()   # Finally, it's Charlie's turn
```

Internally, the `Queue` object will rely on a `list` to keep track of all the customers, let's call it `items`.
However, this `list` must remain hidden, otherwise some malicious person could cut in line.

```python
# Mallory inserts herself at the beginning of the queue instead of at the end
queue.items.insert(0, "Mallory")
# Many frowns ensue
```

In other words, the `items` must be made private.

## Conclusion

A `list` is a general purpose data structure that allows you to access any item you want, and add or remove items anywhere you want.
A `Queue` is a more limited list, one that enforces a "queueing discipline": only add at the end, only remove at the beginning.
Therefore, it needs to hide the list it internally uses for storage so as to prevent abuse.

In general, objects will often hide their internal state (i.e., its attributes) to prevent outsiders from tinkering directly with it.
An attribute can be public if it can take any value, but as soon as you want to limit what can be done with it, you should make it private and only allow access to it indirectly using methods.

A few examples:

* A `Point` class that represents a point with `x`, `y` coordinates does not need to hide its attributes: `x` and `y` are free to have any value they want.
* A `Person` class might want to restrict its `age` to positive values.
  The `age` should then be stored in a private attribute and setting the field should be done using a method (or better, a property) which checks that the new value is indeed positive.
# ENCAPSULATION IN PYTHON
Python is a very dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards. That's why encapsulation in Python is achieved mostly by [convention](https://en.wikipedia.org/wiki/Coding_conventions) rather than by force.

Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff. If a developer wanted to break convention, there are ways to get around the double underscore rule.

```python
class Wall:
    def __init__(self, height):
        # this warns developers to not
        # access the `__height` property directly
        self.__height = height

    def get_height(self):
        return self.__height

```


Python `can not` enforce encapsulation by fully preventing developers from touching private class members

# Assignment

Say we have written the following class.

```python
class Person:
    def __init__(self, age):
        self.age = age
```

This class is used throughout our codebase, many times over.
However, there's a problem with it: `age` can take any value you want.
Somewhere, we made a mistake and in certain cases the `age` becomes negative.
This causes a lot of problems.

The problem with public attributes is that they're rather... dumb.
It's just a simple memory location that can be overwritten at whim.
We somehow want to make it smarter somehow, so that it can disallow negative values.

Enter properties.
Properties allow us to make "intelligent attributes".
In essence, there's two things we can do with attributes: we can read their value, and we can overwrite their value.
Properties make it possible for us to define what exactly should happen when someone tries to read or write it.
In the case of our `age`, properties allow us to prevent anyone from writing a negative value to it.

The nice thing about properties is that they obey the "Uniform Access Principle".
This simply means that the code used to read/write attributes is exactly the same as the code used to read/write properties.

```python
# In case age is a simple attribute
print(person.age)
person.age = 5

# In case age is a smart property
print(person.age)
person.age = 5
```

See! No difference at all.
This is great news: we can promote our dumb `age` attribute to a smart `age` property without having to change any of the client code!
This actually is a very important rule in software development: we want to be able to make local changes (upgrading `age`) without having it global ramifications.

## Readonly Properties

Let's start with a very basic application of properties.
Say we want to have an attribute/property, but we don't want to allow it to be changed:

```python
print(person.age)   # Should be allowed
person.age = 10     # Should raise an error
```

How do we go about it?
First of all, we still need a place to store the actual age.
For this, an attribute is inevitable.
Luckily, as we discussed previously, we can hide this attribute.

```python
class Person:
    def __init__(self, age):
        self.__age = age
```

Okay, we store our age in the private `__age` attribute.
Now we want the user to be able to query a `person`'s `age` using the syntax `person.age`.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

Here, we have defined the property named `age`.
It looks like a regular method, except for the fact that it has `@property` added just in front of it.
This is a *decorator*, and you can do all kinds of fancy stuff with it, but that's not important for now.

So, what does this `@property` decorator do?
It tells Python that whenever the user tries to read from `age`, that it should call that method.
Because of this, it is also called a *getter method*.
In our example, the `age` getter method simply returns the value hidden in the private `__age` attribute.

Right now, we can write

```python
>>> person = Person(18)

>>> print(person.age)
18
```

The method can actually do whatever it wants.
Say we change it to

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        print("Reading age!")
        return self.__age
```

Then reading the `person`'s `age` will also cause a message to be printed:

```text
>>> person = Person(18)

>>> print(person.age)
Reading age!
18
```

So, we can now *read* the `age`.
But can we write to it?

```text
>>> person = Person(18)

>>> person.age = 10
AttributeError: can't set attribute
```

Yay.
This is exactly what we want.

The reason we can't write is that we only defined a *getter* method.
We didn't define a *setter* method.
We'll show you how to do that in a later exercise.
For now, try to contain your excitement.

## Task

Define a class `MusicalNote`.
It must have two readonly properties: `name` and `pitch`.

```text
>>> note = MusicalNote('a4', 440)

>>> note.name
a4

>>> note.pitch
440

>>> note.name = 'b4'
AttributeError: can't set attribute

>>> note.pitch = 450
AttributeError: can't set attribute
```
# Assignment

Let's delve a little further in what we can do with properties.
Say we have our `Person` class, and we want a person to have an age.

```python
class Person:
    def __init__(self, age):
        self.age = age
```

Now, we don't want this age to be directly modifiable, so we hide it and make a readonly property.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

We need this age to be accurate: once a year it should go up by one.
We make a method for this.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    def increment_age(self):
        self.__age += 1
```

Of course, we need to know on what day we need to increment a person's age, meaning we need to store their birthday.

```python
class Person:
    def __init__(self, age, birthday):
        self.__age = age
        self.__birthday = birthday

    @property
    def age(self):
        return self.__age

    @property
    def birthday(self):
        return self.__birthday

    def increment_age(self):
        self.__age += 1
```

This is a bit weird.
Say we have a long list of `Person` objects, then we would need to check if it's their birthday every day:

```python
def process_birthdays(people):
    today = find_out_todays_date()
    for person in people:
        if person.birthday == today:
            person.increment_age()
```

We're not particularly fond of this solution.
One big issue with it is that it suffers from redundancy: the same information is stored twice.
The age can be derived from a person's birthday, meaning there's no need to store both the age and birthday.
The birthday only should suffice.

We want to get rid of the `__age` attribute.
However, we still want to be able to use `person.age` to determine the `person`'s age.

```python
class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    @property
    def age(self):
        ???

    @property
    def birthday(self):
        return self.__birthday
```

`age` can be computed: we know the `person`'s birthday (it's stored in `__birthday`) and we can find out what the current date is.

```python
class Person:
    def __init__(self, birthday):
        self.__birthday = birthday

    @property
    def age(self):
        today = find_out_todays_date()
        difference = today - self.__birthday
        return difference.years

    @property
    def birthday(self):
        return self.__birthday
```

Using this code, the `age` will be computed based on the birthday, which is why it's also called a *computed attribute*.
It looks like an attribute, but it's not really stored anywhere.
Whenever you read it, its value is computed and returned.
By implementing `age` this way, there is no redundancy.

Redundancy is always a tricky thing.
If we were to store both the birthday and the age, we could end up with inconsistent data:

```python
# Say we are in 2023
person = Person(age=18, birthday=Date(day=18, month=12, year=1980))
```

Clearly, this is incorrect: the person should be 42, not 18.
By removing redundancy, such errors cannot occur: the age will always be consistent with the birthday.

## Task

Write a class `BMICalculator` that we can use as follows:

```text
>>> calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)

>>> calc.bmi
24.69

>>> calc.category
normal
```

The bmi is computed as follows:

```python
bmi = weight_in_kg / height_in_m**2
```

The category can take one of three values:

* `"underweight"` if `bmi` is less than `18.5`.
* `"normal"` if `bmi` is between `18.5` and `25`.
* `"overweight"` if `bmi` is greater than `25`.

# Setters

As of yet, we have only defined getter methods, i.e., methods that tell Python what to do when the user *reads* from a property.
We will now take a look at *setter methods*, which are called whenever a user *writes* to a property.

Let's go back to our old version of the `Person` class:

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
```

In this version, changes are disallowed.
Let's say we want to allow the user to make arbitrary changes to `age`, as long as the `age` is set to a positive number.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        ???
```

We added another `age` method, but this one has `@age.setter` in front of it.
This tells Python that it's the `age`'s setter method.
The `value` parameter (you can choose whichever name you like, but as always, keep it descriptive) is the value the user is trying to assign to `age`.

```python
person = Person(18)
person.age = 19
```

This code would call the `age` setter with `value` set to `19`.

A simple implementation for the setter would be

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
```

Okay, this works, but it doesn't do anything special.
In fact, this implementation works exactly the same as if you simply made `age` a regular public attribute.
No need for properties.

However, we want to add some intelligence to it: we want to allow only positive ages.
Let's add an `if` to the setter.

```python
class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

As you can see, the setter will loudly complain when `value < 0`:

```text
>>> person = Person(20)
>>> person.age
20

>>> person.age = 21
>>> person.age
21

>>> person.age = -1
ValueError: age must be positive
>>> person.age
21
```

## Fixing the Constructor

The above code contains a glaring flaw:

```python
>>> person = Person(-20)
>>> person.age
-20
```

The constructor doesn't check the age, so it _is_ possible to have `Person` objects with invalid ages.
It's like a hole in `Person` that we need to fix.

```python
class Person:
    def __init__(self, age):
        if age < 0:
            raise ValueError('age must be positive')
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

This works, but you should immediately notice the duplication of logic: both the constructor and the `age` setter contain the same logic.
Such repetition needs to be avoided, so we rewrite it as

```python
class Person:
    def __init__(self, age):
        self.age = age       # Calls age's setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be positive')
        self.__age = value
```

This pattern is quite common in code: you will have one gatekeeper (the one who knows the rules and has direct access) and everyone else should delegate to this gatekeeper.
Here, the `age` setter is the gatekeeper to `__age`.
The constructor wants to set `__age` but needs to have the discipline to go through the `age` setter.
If other methods were to be added that need to modify the age, they should all rely on the `age` setter.

## Task

We want to keep track of time of days, i.e. a time between 00:00:00 and 23:59:59.
Write a class `Time` that represents such a time of day.

* It must keep track of hours, minutes and seconds.
* The value of `hours` must be between 0 and 23.
* The value of `minutes` and `seconds` must be between 0 and 59.
* The constructor takes three parameters `hours`, `minutes` and `seconds` and uses them to initialize the object's attributes.
* The values of `hours`, `minutes` and `seconds` must be settable and gettable.
* A getter should always be before its brother setter, think about it why.
* Rely on properties to guard `hours`, `minutes` and `seconds` against invalid values.

A short example:

```text
>>> time = Time(0, 0, 0)
>>> time.hours = 8
>>> time.hours = -1
ValueError
>>> time.hours = 24
ValueError
```
# Assignment

A more challenging exercise: write a class `LengthConverter` that helps you convert between different units of measurement.
Usage is as follows:

```python
>>> converter = LengthConverter()

# Set the distance to 100 meter
>>> converter.meter = 100

# Convert the 100 meter into feet
>>> converter.feet
328.084

# Convert the 100 meter into inch
>>> converter.inch
3937.01

# Convert the 100 meter into meter
>>> converter.meter
100

# Set the distance to 5 feet
>>> converter.feet = 5

# Convert 5 feet into inches
>>> converter.inch
60
```

We support three units: meter, feet and inches.
In order to use the converter, you must first set it to a certain distance:

```python
# Set distance to 10 inch
converter.inch = 10
```

In other words, *writing* to a property sets the distance in the corresponding unit (here inches).
To convert it to another unit, simply read the corresponding property:

```python
# Converting to meter
print(converter.meter)

# Converting to feet
print(converter.feet)
```

## Hints

* Internally, rely on a single private attribute that stores the distance in meter, e.g. `__distance_in_meter`.
* Each getter method should read `__distance_in_meter` and convert it to the corresponding unit.
* Each setter should convert the new value to the meters and store it in `__distance_in_meter`.

# Operator Overloading

As you know, classes can have different kinds of members: attributes, methods and properties.
Accessing any one of these members is always done using the same "dot notation":

```python
some_object.attribute   # Accessing an attribute
some_object.method()    # Invoking a method
some_object.property    # Accessing a property
```

However, there are also other kinds of interactions possible.
For example, you can add things together using the operator `+`:

```python
5 + 3             # Adding numbers
"a" + "b"         # Adding strings
[1, 2] + [3, 4]   # Adding lists
```

However, if we use `+` on one of our objects:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p + q
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

As you can see, this gives an error.
This makes sense: why would Python know how you mean to add two points together?

Let's add a regular method `add` that defines how this addition must take place:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

This allows us to write

```python
>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p.add(q)
Point(4, 6)
```

This is great, but we'd really like to write `p + q` instead of `p.add(q)`.
Luckily, it is simple to make this happen:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

We try once again:

```python
>>> p = Point(1, 2)
>>> q = Point(3, 4)
>>> p + q
Point(4, 6)
```

When Python sees code like `obj1 + obj2`, it will automatically transform this into `obj1.__add__(obj2)` for you.
So, in essence, there's nothing new really: you simply have to know how to name the method: in the case of `+` we must name the method `__add__`.

There are many other operators, e.g., `-`, `*`, `/`, `%`, etc.
Each of them have a [corresponding method](https://docs.python.org/3/reference/datamodel.html):

|Operator|Method|
|-|-|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |
| `**` | `__pow__` |

As you might have noticed, these methods share a pattern: they're all enclosed by two underscores (`__`).
For this reason, they're often called [dunder methods](https://wiki.python.org/moin/DunderAlias).

Notice that these methods should always return a _new_ object and not modify `self`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Correct implementation
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    # Wrong implementation, never do this!
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
```

## Task

Create a class `Money` that represents a certain `amount` of money in a certain `currency`:

```python
>>> money = Money(10, "EUR")
>>> money.amount
10

>>> money.currency
"EUR"
```

We want to be able to add `Money`s together, but only if their currencies match.

```python
>>> Money(10, "EUR") + Money(20, "EUR")
Money(30, "EUR")

>>> Money(10, "EUR") + Money(20, "USD")
RuntimeError("Mismatched currencies!")
```

Same for subtraction:

```python
>>> Money(30, "EUR") - Money(10, "EUR")
Money(20, "EUR")

>>> Money(30, "EUR") - Money(10, "USD")
RuntimeError("Mismatched currencies!")
```

Finally, we also want to be able to multiply a `Money` with a number.
Notice that we are *not* multiplying two `Money`s together, but a `Money` with an `int` or `float`.

```python
>>> Money(20, "EUR") * 5
Money(100, "EUR")
```
# Circular Buffer

We want to create a special kind of list, namely one that only keeps track of the N most recently added elements.
An example will make this clearer:

```python
# We are only interested in the last 3 items
>>> buffer = CircularBuffer(3)

# Initially the buffer is empty
>>> len(buffer)
0

# Let's add a few items
>>> buffer.add('a')
>>> buffer.add('b')
>>> buffer.add('c')
>>> len(buffer)
3

# We want to be able to read the elements
>>> buffer[0]
'a'
>>> buffer[1]
'b'
>>> buffer[3]
'c'

# Now watch what happens when we add a fourth element!
>>> buffer.add('d')
>>> len(buffer)
3
>>> [buffer[0], buffer[1], buffer[2]]
['b', 'c', 'd']
```

As you can see, when we added the fourth item `d`, we went over the maximum size of `3`, so the "oldest" element was removed, i.e., `'a'`.
Let's add a fifth element:

```python
>>> buffer.add('e')
>>> len(buffer)
3
>>> [buffer[0], buffer[1], buffer[2]]
['c', 'd', 'e']
```

## Length

Given a `CircularBuffer` object, it can be useful to be able to ask for its size, i.e., how many items it contains.
We could simply define a method:

```python
class CircularBuffer:
    def size(self):
        # ...
```

However, Python would prefer you to stick to the standard way of doing things, namely using `len()`.
You should already know `len` from other data structures:

```python
# len works on lists
>>> len([1, 2, 3])
3

# and on strings
>>> len("abcd")
4

# and on sets
>>> len({1, 2, 3, 4, 5})
5
```

How do we make `len` understand our `CircularBuffer`?
Very simple: `len(obj)` will actually call `obj.__len__()` behind the scenes.
So, for example,

```python
class CircularBuffer:
    def __len__(self):
        return 10

>>> buffer = CircularBuffer(3)
>>> len(buffer)
10
```

## Indexing

You should also be familiar with indexing using the `[]` operator:

```python
# Indexing arrays
>>> [1, 2, 3, 4][0]
1

# Indexing strings
>>> 'abcd'[1]
'b'
```

You can have your own classes respond to `[]` by defining the `__getitem__` dunder method:

```python
class CircularBuffer:
    def __getitem__(self, index):
        # ...
```

## Task

Implement the `CircularBuffer` class as described above.

* `CircularBuffer(n)` should create a `CircularBuffer` object with maximum size `n`.
* `buffer.add(item)` adds an extra item to the buffer. If the maximum size is reached, the oldest element is removed.
* `buffer[index]` returns the `index`th item in the buffer.
* `len(buffer)` returns the number of items in the buffer. This can never be greater than `n`.
# Static Methods

A class is typically described as a blueprint for objects.
Another way of looking at it is to see a class as a factory of objects.
As far as you know, there's very little you can do with the class itself, except for asking it to create an object.

```python
class Plumbus:
    def schleem(self):
        ...

# Invalid
Plumbus.schleem()

# Valid
plumbus = Plumbus()    # Create an object
plumbus.schleem()      # Now we can call the shleem method
```

The syntax for defining classes is perhaps a bit misleading: it seems to imply that members are part of the class, while in fact they are members of _objects_ of that class.
However, it is indeed possible to attach methods to the class itself instead of to its objects:

```python
class Plumbus:
    def schleem(self):
        # ...

    @staticmethod
    def fleeb():     # No self parameter!
        # ...
```

Here, `fleeb` is a _static method_ (do **not** call it a class method, that's something different).
We can now write the following code:

```python
Plumbus.fleeb()
```

As you can see, we call `fleeb` directly on the class instead of creating an object first.
Also notice that `fleeb` is missing the `self` parameter: `self` is meant to refer to the object a method is called on, but in this case, there is no object, so having a `self` parameter would make no sense.

## Usage: Factory Functions

So, what good are these static methods?
How useful are they?

Well, they're definitely used way less than regular methods.
But they do have a purpose.
You can see them as regular functions (i.e., functions outside of a class) that conceptually belong to a class: placing them inside the class makes this relation clear.

Consider the following class:

```python
class Distance:
    def __init__(self, size):
        self.size = size

distance = Distance(10)
```

Here, we created a `Distance` object of size 10.
But 10 what?
10 meters?
10 miles?
10 lightyears?
We don't know: it's not clear from the code.

We can make it a bit clearer:

```python
class Distance:
    def __init__(self, size_in_meters):
        self.size_in_meters = size_in_meters

distance = Distance(10)
```

If you just see the last line, again, it's not clear what unit of distance is used.
We could make it explicit as follows:

```python
distance = Distance(size_in_meters=10)
```

However, mentioning the parameter name is optional.
We can force the user to mention it using [keyword-only arguments](https://peps.python.org/pep-3102/):

```python
class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

distance = Distance(10)                  # Error
distance = Distance(size_in_meters=10)   # Valid
```

But what if we want to express our distance in a different unit, like miles?
It would make sense that we have some helper functions for this.

```python
def meters(amount):
    return Distance(size_in_meters=amount)

def millimeters(amount):
    return Distance(size_in_meters=amount / 1000)

def miles(amount):
    return Distance(size_in_meters=amount * 1609.34)

# and so on
```

Since their only purpose is to _create_ objects, such functions are also _factory functions_.
This is a perfectly valid approach: code creating distance will be clear since the unit is always mentioned explicitly.
It can, however, be helpful to bundle these functions together.
And this is where static methods come into play:

```python
class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

    @staticmethod
    def meters(amount):
        return Distance(size_in_meters=amount)

    @staticmethod
    def millimeters(amount):
        return Distance(size_in_meters=amount / 1000)

    @staticmethod
    def miles(amount):
        return Distance(size_in_meters=amount * 1609.34)

    # ...
```

Creating a distance can now be written as

```python
distance = Distance.miles(5)
```

## Task

Create a class `Duration` that can be used as follows:

```python
>>> duration = Duration.from_seconds(60)
>>> duration.seconds
60

>>> duration.minutes
1

>>> duration = Duration.from_hours(1)
>>> duration.minutes
60

>>> duration.seconds
3600
```

We want the following members:

* Static factory methods named `from_seconds`, `from_minutes` and `from_hours`.
* Readonly properties named `seconds`, `minutes` and `hours`.

Note: the reason we named the factory functions `from_unit()` instead of just `unit()` is that we wanted to be able to name our properties after the units.
Sadly, we cannot have static methods and properties with the same name inside one class.
# INHERITANCE
We've made it to the Holy-grail of object-oriented programming: inheritance. Inheritance is the defining trait of object-oriented languages. Non-OOP languages like Go and Rust provide encapsulation and abstraction features as almost every language does. Inheritance on the other hand tends to be unique to class-based languages like Python, Java, and Ruby.

## WHAT IS INHERITANCE?
Inheritance allows one class (aka "the child class") to inherit the properties and methods of another class (aka "the parent class").

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

## SYNTAX
In Python, one class can inherit from another using the following syntax.

```python
class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"
```
To use the constructor of the parent class, we can use Python's built-in `super()` method.

```python
class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)
```

## ASSIGNMENT
In Age of Dragons, all the archers in the game are humans, though not all humans are necessarily archers. The thing all humans have in common is that they need a name, so the `Human` class has taken care of the naming logic.

Now we need to write an `Archer` class. Archers are humans, and therefore need a name, but we don't want to re-write all that code! Let's just inherit the `Human` class!

Complete the `Archer` class. It should inherit from its parent. In its constructor it should call its parent's constructor, then also set its unique `__num_arrows` property.
# WHEN SHOULD I USE INHERITANCE?
Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when every instance of the child class can also be considered the same type as the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance probably is not the best answer. In that case, you would probably just want to share some functions, or maybe make a new parent class that both classes inherit from.

 `ALL CATS ARE ANIMALS BUT NOT ALL ANIMALS ARE CATS`

# INHERITANCE HIERARCHY
There is no limit to how deeply we can nest an inheritance tree. For example, a `Cat` can inherit from an `Animal` that inherits from `LivingThing`. That said, we should always be careful that each time we inherit from a base class the child is a strict subset of the parent. You should never think to yourself "my child's class needs a couple of the parent's methods, but not these other ones" and still decide to inherit from that parent.

## ASSIGNMENT
The game designers have decided to add a new unit to the game: `Crossbowman`. A crossbowman is always an archer, but not all archers are crossbowmen. Crossbowmen have several arrows, but they have an additional method: `triple_shot()`.

1. Add a `use_arrows(self, num)` method to the `Archer` class. It should remove `num` arrows. If there aren't enough arrows to remove, it should raise a `not enough arrows` exception.
2. The `Crossbowman` class's constructor should call its parent's constructor.
3. The crossbowman's `triple_shot` method should use `3` arrows.
4. The crossbowman's `triple_shot` method takes a `target` as a parameter and returns `{} was shot by 3 crossbow bolts` where `{}` is the name of the `Human` that was shot.

# Inheritance

## Duplication in Functions

Say you have the following two functions:

```python
def smallest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return min(sums)


def greatest_sum(ns):
    sums = (
        x + y
        for x in ns
        for y in ns
    )
    return max(sums)
```

As you can see, they both compute the same `sums`.
Generally, you should really avoid duplication.
Shared code should be factored out as follows:

```python
def compute_sums(ns):
    return (
        x + y
        for x in ns
        for y in ns
    )


def smallest_sum(ns):
    return min(compute_sums(ns))


def greatest_sum(ns):
    return max(compute_sums(ns))
```

## Duplication in Classes

Duplication can also occur on the level of classes.
To demonstrate this, let's implement a (very small) part of a chess game.

You are given a file `startercode.py`.
Take a good look at the code inside.
Let's briefly discuss the three classes inside.

### `Position`

`Position` is a class that represents, well, positions.
Nothing special about it, really.

### `Pawn`

`Pawn` objects have a `position` and `color`.

* The `pawn.position` is only valid if it refers to a position on the chessboard (chessboards are 8&times;8 grids).
  The logic for checking resides in `is_valid_position`.
* `pawn.color` can only have one of two values: `black` or `white`, as is verified in `is_valid_color`.
* `pawn.is_legal_move(new_position)` checks if the `pawn` can move from its current position to `new_position`.
  The details behind the logic are not very important.
* `pawn.move(new_position)` moves the `pawn` to `new_position` on condition that it represents a legal move as determined by `is_legal_move`.

### `King`

You will notice that `King` is very similar to `Pawn`.
There's really only one difference, namely the logic in `is_legal_move`.
All the rest is identical.

## Factoring Out the Common Code

As mentioned before, `Pawn` and `King` have a lot of code in common.
However, duplication is generally a Very Bad Thing: it just adds more opportunities for bugs to arise.
The more code you write, the higher the odds you make a mistake.

So, let's try to get rid of all duplicated code.

* Start by copying all starter code to your own `student.py` file.
* Run the tests.
  They should all pass, because all functionality is implemented correctly.
* Create a new class `ChessPiece`.
* Move all members `Pawn` and `King` have identical implementations for to `ChessPiece`.
* Only one method should remain in `Pawn` and `King`, namely their specialized implementation for `is_legal_move`.

Restructuring code like this is called [refactoring](https://en.wikipedia.org/wiki/Code_refactoring): it is the process of modifying code _without changing its behavior_.
Remember this word as you will hear it often.

Now we need a way to say that `Pawn` and `King` must "import" all members defined in `ChessPiece`.
The actual term used in Python is _inherit_: `Pawn` and `King` must _inherit_ members from `ChessPiece`.
For this reason, `ChessPiece` is often called the _parent class_ (or base class).
`Pawn` and `King` are _child classes_ of `ChessPiece`.

How do we tell Python about this relationship?
Very simple:

```python
class ChessPiece:
    # ...

class Pawn(ChessPiece):
    # ...

class King(ChessPiece):
    # ...
```

In essence, this means that `Pawn` "copies" all members of `ChessPiece` and then adds its own extra members.
Idem for `King`.

Run the tests.
They should all pass.

## Refactoring

Refactoring is a very common process and its importance cannot be overstated.
As explained before, the goal is to perform _structural_ changes, not _behavioral_ ones.

In order to safely refactoring, you will typically start off with tests.
Tests check behavior, they "pin" it down as it were.
Next, you perform a small modification (refactoring) to your code, after which you run the tests again.
They should all keep passing.
If they don't, you accidentally broke something and you'll need to fix it.
You repeat this process of making small changes and running the tests until your code is cleaned up.

Few students like this refactoring process because they're already content that their code works.
However, building on top of badly structured code is a risky endeavor:

* the complexity of your code grows quickly and soon enough you won't understand it more: it works seemingly by magic but you don't want to touch it out of fear to break something
* bugs tend to appear out of nowhere and are very hard to locate
* your progress slows down to a crawl

This is known as [technical debt](https://en.wikipedia.org/wiki/Technical_debt) and it has been the downfall of many.
# Abstract Methods

Let's revisit the chess example from the previous exercise.
The end result looked a bit like this:

```python
class ChessPiece:
    # Some code (omitted)

    def move(self, new_position):
        if not is_legal_move(new_position):
            raise ValueError('invalid move')
        self.__position = new_position


class Pawn(ChessPiece):
    def is_legal_move(self, new_position):
        # Some code (omitted)


class King(ChessPiece):
    def is_legal_move(self, new_position):
        # Some code (omitted)
```

For this explanation, it is important to notice that `ChessPiece`'s code relies on the existence of a method named `is_legal_move`, which is only getting defined in the child classes.

## Abstract Classes

What happens if we do this?

```python
piece = ChessPiece(Position(0, 0), 'white')
```

This is kind of nonsensical: we create a chess piece, but we remain vague about which one it is.
Is it a king, a pawn, a queen, a rook, ...?
No, it's just ... _a piece_.
It's as if you go to a restaurant and ask the waiter for literally "a menu item".
It makes no sense; you need to be more specific.

Also, if you were to try to move this `piece`:

```python
piece = ChessPiece(Position(0, 0), 'white')
piece.move(Position(4, 4))
```

Again, utter nonsense: in order to check whether it's a valid move, you need to know what piece it is.
A queen or bishop would be allowed to make that move, but other pieces wouldn't be.

Python would also not be happy: `move` calls `is_legal_move`, but this method is not defined in `ChessPiece`.
You would simply get an `AttributeError` thrown at you.

We want to be able to express that `ChessPiece` on its own is merely an abstract concept, a "dummy" class that acts as a parent to other classes.
We do this as follows:

```python
from abc import ABC


class ChessPiece(ABC):
    # some code
```

Here, `ABC` stands for [_Abstract Base Class_](https://docs.python.org/3/library/abc.html). `from abc import ABC` is the actual import, not just some letters from the alphabet!
Base class is a synonym for parent class.

Does this solve our problem?
If we try to create a `ChessPiece` object, no error is thrown, so it didn't really help much.
However, it is a required step towards our goal of forbidding `ChessPiece` to be instantiated.

## Abstract Methods

As mentioned earlier, `ChessPiece` relies on `is_legal_move`.
However, this is not immediately apparent: you have to sift through the code and notice that somewhere in there there's a call to a nonexistent method.
It'd be better to make it explicit that there's a "hole" in the class.

```python
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    @abstractmethod
    def is_legal_move(self, new_position):
        ...
```

**Important**
> We wish to point out that `...` is literally the code that needs to be there.
It's not a way of omitting uninteresting details: the actual code contains three dots.

Using `@abstractmethod` we have made clear that `ChessPiece` needs `is_legal_move` to be implemented.
Let's now try to instantiate `ChessPiece`:

```text
>>> piece = ChessPiece(Position(0, 0), 'black')
TypeError: Can't instantiate abstract class ChessPiece with abstract method is_legal_move
```

Great!
This is exactly what we want.

## Task

The exercise is a bit of a puzzle and focuses on the actual rules regarding abstract classes and methods.
Copy the code from `startercode.py` to `student.py`.
Make the necessary classes and method abstract.

A summary of the rules to follow:

* Pick a class.
* Determine which methods it contains, i.e., the methods it defines itself, and the ones it inherits.
  Let's call this set of methods D.
* Determine which methods are called on `self` within the class.
  Let's call this set of methods C.
* If C contains methods not in D, it means there are "holes", in which case we need to add `@abstractmethod` declarations and make the class abstract.

A quick example:

```python
class A:
    def f(self):
        self.h()

    def g(self):
        self.f()

class B:
    def h(self):
        pass
```

We start with class `A`.
It defines methods named `f` and `g`.
It calls `f` and `h` on itself.
This means that `h` is missing from `A`: we need to make it abstract and add a declaration for `h`:

```python
class A(ABC):
    def f(self):
        self.h()

    def g(self):
        self.f()

    @abstractmethod
    def h(self):
        ...
```

Next comes `B`.
It has methods `f`, `g` (both inherited) and `h`.
It doesn't call methods on itself, so there are no "holes".
Nothing needs to be changed to `B`.
# Abstract Properties

Similarly to abstract methods, it's also possible to have abstract properties.

```python
class Foo:
    @property
    @abstractmethod
    def my_property(self):
        # ...

    @my_property.setter
    @abstractmethod
    def my_property(self, value):
        # ...
```

> You might notice that `@abstractproperty` exists, but it's been [deprecated](https://docs.python.org/3/library/abc.html#abc.abstractproperty).
> This means you shouldn't use it because it's been replaced by something else (`@abstractmethod`) and it might disappear in a future version of Python.

# Task

Copy the code from `startercode.py` to `student.py`.
The code defines two classes `Rectangle` and `Circle`.
Define a class `Shape` that acts as their parent class.

Look at what members `Rectangle` and `Circle` have in common.
Add those as abstract members to `Shape`.

You might wonder what use this might be: `Shape` only contains abstract members, so there's no shared code to speak of.
You can see `Shape` as a sort of "contract": it provides a guarantee that all of its child classes must contain certain members.
Say you were to define a new shape, say `Triangle`. In case you forget to implement a member, Python will point this out to you.
# Overriding

```python
class Parent:
    def method(self):
        return "Parent.method"

class Child(Parent):
    def other_method(self):
        return "Parent.other_method"
```

Consider the two classes above.

* `Parent` has one method named `method`.
* `Child` has two method: `method` (inherited from `Parent`) and `other_method`.

Let's try something new.
What happens if we write this:

```python
class Parent:
    def method(self):
        return "Parent.method"

class Child(Parent):
    def method(self):
        return "Child.method"
```

Here, `Child` declares a method with exactly the same name as the one in `Parent`.
But is this allowed? The answer is yes. This idea of redefining a method with the same name is called _overriding_ (not overwriting).

What happens is what you would expect happens: the `Child` implementation of `method` "wins".
Take a look at this code:

```python
>>> parent = Parent()
>>> parent.method()
"Parent.method"

>>> child = Child()
>>> child.method()
"Child.method"
```

In this example, one could say that it makes little sense to have `Child` inherit from `Parent` since it overrides all of its parent methods anyway.
Nothing that is inherited survives.
This is true, but there are cases where it still could be useful.

## Task

Copy the contents of `startercode.py` to `student.py`.
Take a quick look at the code:

* A `Customer` has a name, an age and a country.
* A `ShoppingList` has an owner (a `Customer`) and a list of `Item`s.

The `Item` class still needs to be defined.
That'll be your job.

Start off by defining a class `Item`.
An `Item` should have a `name` and a `price` which are set using the constructor.

As you can see, `shopping_list.add(item)` relies on the `shopping_list.can_be_sold_to(item)` method: it checks if it is legal to sell `item` to the `owner` of the `shopping_list`.
If it's not, `add` refuses to actually add the `item` to the `shopping_list`.
You must therefore equip your `Item` class with a `can_be_sold_to` method.
You can keep it simple: simply have it return `True`.

Next, we want to introduce the concept of an `AgeRestrictedItem`.
It is only allowed to be sold to `Customer`s with `age` at least `18`.
Create a new class `AgeRestrictedItem` which is a child class of `Item`.
Override the `can_be_sold_to` method so that it returns `False` for underage `Customer`s.

Finally, we also want a `CountryRestrictedItem`.
Such `Item`s cannot be sold to people from `Arstotzka`.
# Super

In the previous exercise we had `AgeRestrictedItem`s that could only be sold to `Customer`s who are at least 18 years old.
Similarly, a `CountryRestrictedItem` could not be sold to `Customer`s residing in `Arstotzka`.

```python
class AgeRestrictedItem(Item):
    def can_be_sold_to(self, customer):
        return customer.age >= 18


class CountryRestrictedItem(Item):
    def can_be_sold_to(self, customer):
        return customer.country != 'Arstotzka'
```

The age (18) and country (Arstotzka) are hardcoded.
That's generally not a good solution: we can so easily generalize these classes, i.e., make them more flexible, by relying on parameters.
We want users of the class to be able to specify the minimum age or forbidden countries.
Let's try this:

```python
class AgeRestrictedItem(Item):
    def __init__(self, minimum_age):
        self.minimum_age = minimum_age

    def can_be_sold_to(self, customer):
        return customer.age >= minimum_age


class CountryRestrictedItem(Item):
    def __init__(self, forbidden_countries):
        self.forbidden_countries = forbidden_countries

    def can_be_sold_to(self, customer):
        return customer.country not in forbidden_countries
```

Can you see a problem with this?
We'll give you a few moments to think.

&vellip;

Okay, that's enough moments.
Let's see what happens when we instantiate an `AgeRestrictedItem`:

```python
>>> item = AgeRestrictedItem(18)
>>> item.name
AttributeError: 'AgeRestrictedItem' object has no attribute 'name'

>>> item.price
AttributeError: 'AgeRestrictedItem' object has no attribute 'price'
```

The error makes perfect sense: we never mentioned the item's name or price.
Can we perhaps... pass them along to the constructor?

```python
>>> item = AgeRestrictedItem('lightsaber', 5, 18)
TypeError: AgeRestrictedItem.__init__() takes 2 positional arguments but 4 were given
```

That was bound to happen: `AgeRestrictedItem` has overridden its parent class's `__init__` method.
The new version only takes one (or two, if you count `self`) parameters.

We clearly want to be able to specify a name and a price, as well as a minimum age.
This means `AgeRestrictedItem.__init__` will have to accept three parameters:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        ???
```

We could simply perform the initialization in `AgeRestrictedItem`'s constructor:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        self.name = name
        self.price = price
        self.minimum_age = minimum_age
```

This is a rather bad idea, however: most of the code already exists in `Item`.
We would like to delegate the initialization of `name` and `price` call `Item.__init__`.
And that's exactly what we can do:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        super().__init__(name, price)
        self.minimum_age = minimum_age
```

`super()` allows you to access the "old" versions of methods.
Here, `super().__init__` refers to the `__init__` method defined in `Item`.

So, what happens is simple:

* You want to make an `AgeRestrictedItem` with a certain `name`, `price`, and `minimum_age`.
  In code, this is written `AgeRestrictedItem(name, price, minimum_age)`.
* `AgeRestrictedItem.__init__` is called with the given arguments.
* `AgeRestrictedItem.__init__` first calls `super().__init__`, which refers to `Item.__init__`.
* `Item.__init__` initializes the `name` and `price` of the object.
* After `Item.__init__` has finished, execution returns to `AgeRestrictedItem.__init__` which initializes the third attribute, `minimum_age`.

## Task

Copy the starter code to `student.py`.
As you can see, it defines an abstract class `Shape` with abstract properties `perimeter` and `circumference`.
We ask of you to write four classes.

### `Rectangle`

`Rectangle` is a child class of `Shape`.
It should have two readonly properties `length` and `width`.

### `Square`

`Square` is a child class of `Rectangle`.
A `Square` is a special `Rectangle` with `length == width`.
Its constructor should only accept a single parameter `side`.

Even though `Square` inherits the `length` and `width` properties from `Rectangle` it should nonetheless also add its own readonly property `Side`.
It should return the same value as `length` and `width`.

### `Ellipse`

`Ellipse` is another kind of shape.
It should have two readonly properties `major_radius` and `minor_radius`.

Note that there is [no nice formula](https://www.youtube.com/watch?v=5nW3nJhBHL0) for the perimeter of an ellipse.
Have the `perimeter` property raise a `NotImplementedError`.

### `Circle`

A `Circle` is a special kind of ellipse where `major_radius == minor_radius`.
The constructor should therefore only accept a single parameter, which we'll name `radius`.
Also add a readonly property `radius` which returns the same value as `major_radius` and `minor_radius`.

## Formulae

In case you forgot the formulae for area and perimeter:

| Shape | Perimeter | Area |
|-:|:-:|:-:|
| Rectangle | 2 &times; (`width` + `height`) | `width` &times; `height` |
| Square | 4 &times; `side` | `side`<sup>2</sup> |
| Ellipse | ??? | &pi; &times; `minor_radius * major_radius` |
| Circle | 2 &times; &pi; &times; `radius` | &pi; &times; `radius`<sup>2</sup> |
# Regular Expressions

Consider the following functions:

* `is_valid_time(string)` which checks if `string` has the form `hh:mm:ss`.
* `is_valid_student_id(string)` which checks if `string` has the form `rNNNNNNN` where each `N` is a digit.
* `is_valid_email_address(string)` which checks if `string` has the form `fname.lname@subdomain.domain`.

Each of these performs the same job: check if the given string satisfies a certain pattern.
This kind of functionality occurs often (e.g. user input validation). While it is certainly
possible to write algorithms that perform these tasks, it is quite arduous and bug prone to do so.

Regular expressions (regexes for short) were developed to simplify implementing pattern checking algorithms:
these are a minilanguage highly specialized in succinctly describing patterns.

Regular expressions are not specific for Python: almost all languages
have support for them.

* Java: the [`Pattern`](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) class.
* JavaScript: regexes built into the language.
* C#: the [`Regex`](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex) class.

## Regular Expressions in Python

In Python, regular expression functionality is provided through the [`re` module](https://docs.python.org/3/library/re.html). This module consists of many functions,
each one corresponding to a specific use of regular expressions. For now, we focus on simply checking
if a string matches a pattern.

The function `re.fullmatch(regex, string)` does exactly that: it determines whether
`string` satisfies the pattern described by `regex`. If it does, `fullmatch` returns
a truthy value, otherwise a falsey one. The only question that remains is, what does
this regex minilanguage look like? What form should `regex` take?

Let us start with a very simple pattern: we want to check whether `string`
consists of exactly one character, namely `a`. The regex expressing this pattern is
simply `a`.

In order to check if some string `string` matches a pattern described by `a`, we rely
on `fullmatch`:

```python
if re.fullmatch('a', string):
    # string does indeed match the pattern 'a'
```

## Assignment

Write a function `equals_a(string)` that checks if `string` equals
the `'a'` making use of regular expressions.
# Assignment

I know what you're thinking. You're probably not very impressed by all this regular expression stuff.
Why not simply use `string == 'whatever'`? Much simpler.

Ok, we'll kick it up a notch. Say you want to check if a string consists solely of `a`s?
For example, `"a"` would be fine. Also `"aa"`. Even `"aaaaaa"`. But not `"b"`.

Ordinarily, you would need some sort of a looping construct, something like this:

```python
def one_or_more_a(string):
    return all( char == 'a' for char in string )
```

But now let's do it with regular expressions. How do we express that something can be repeated in regex talk?
Quite simply using the `+` operator of course! The regex `a+` means 'one or more `a`s'.
Note that, contrary to what you're accustomed to, `+` is *not* an infix operator, i.e., you don't put it *between* two things, like `a+b`. The regex `+` is a *postfix operator*, meaning it applies to the element that comes before it, in our case `a`. Note that `a+b` is indeed a valid regular expression: it means "one or more `a`s, followed by one `b`."

Write a function `one_or_more_a(string)` that checks whether `string` consists
of one or more `a`s.
# Assignment

What if we want `abc` to be repeated one or more times?

* `abc+` would not work: the `+` only applies to the `c`. In other words, `abcccc` would match, but that's not what we want.
* `a+b+c+` is not correct either. This would result in `aaaabbbcccc`, not `abcabcabc`.

We need the `+` operator to apply on all three letters `abc`. Like in mathematics, we can achieve this using parentheses: `(abc)+`.

Write a function `one_or_more_abc(string)` that checks whether `string` equals
one or more times `abc`.
# Assignment

This should not come as a surprise... Write a function `ten_times_abc(string)` that checks whether `string` equals exactly ten consecutive `abc`s.

Luckily for you, regexes allow you to express you want a certain pattern to be repeated N times. The syntax for this is `x{N}`, where `x` is whatever you want repeated.
# Assignment

Write a function `three_to_ten_times_abc(string)` that checks whether `string` consists of minimally three repetitions of `abc` and maximally ten repetitions.

As you saw in the last exercise, you can use `x{N}` to repeat `x` exactly N times. A variant of this construct allows you to specify a range. Look up in the [Python docs](https://docs.python.org/3/library/re.html) what the syntax is.
# Assignment

Write a function `ten_or_more_abc(string)` that checks whether `string` equals ten or more times `abc`.
Search the [Python docs](https://docs.python.org/3/library/re.html) to find how to express this using the `{...}` syntax.
# Assignment

Write a function `zero_or_more_abc(string)` that checks whether `string` consists of zero or more times `abc`.

Just like `x{1,}` is the same as `x+`, there is a special operator for `x{0,}`.
Consult the [Python docs](https://docs.python.org/3/library/re.html) to find out which one.
# Assignment

Say you want a string to be equal to either `abc` or `xyz`. These are the only two allowed possibilities.
For this, you'll need a new regex operator: `|`. Read the [Python docs](https://docs.python.org/3/library/re.html) to find out how to use it.

Write a function `abc_or_xyz(string)` that checks whether `string` equals `abc` or `xyz`.
# Assignment

Write a function `only_vowels(string)` that checks whether `string` contains only vowels.
For this, you'll need to combine the following regex ingredients:

* The alternation operator `|`.
* The grouping parentheses `()`.
* The Kleene star `*`.
# Assignment

Write a function `only_digits(string)` that checks whether `string` contains only decimal digits, i.e. `0`, `1`, ..., `9`.
While using the `|`-operator is certainly possible, it is quite clumsy when there are so many allowed options.

Regexes provide *character classes* as a more readable means to describe many single character alternatives:
instead of `a|b|c|d`, you can also write `[abcd]`.

Note that `[abcd]` matches exactly one letter which must be either `a`, `b`, `c` or `d`.
`abcd` is not a match as there are four characters.
# Assignment

Write a function `only_letters(string)` that checks whether `string` contains only letters. Both lowercase and uppercase
are allowed.

We now need to list 52 possibilities. Even with our recently discovered character classes,
this would be a bit too much.

Fortunately, character classes also allow you to specify ranges. For example,
`[a-e]` is equivalent with `[abcde]`. A more complex example is
`[aeiou0-9]`: this matches a single lowercase vowel or digit.
# Assignment

Write a function `is_dna(string)` that verifies that `string` is a valid DNA string.
DNA strings can only contain four characters: `G`, `A`, `T` and `C`.
# Assignment

Write a function `contains_three_digits(string)` that checks whether `string` contains at least three digits.
`string` is allowed to contain any number of arbitrary characters, as long as three of these characters
are digits. The digits need not be next to each other.

To solve this exercise, you need a way to express 'any character'. The regex symbol
for this is `.`. For example `...` matches strings that consist of exactly three characters.
`.*` literally matches any string.
# Assignment

Write a function `contains_a(string)` that checks whether `string` contains an `a`.
You can achieve using the regex `.*a.*`. However, let's do it a bit differently.

Until now, you've always used the `re.fullmatch(regex, string)` function. This function
demands that the *entire* string satisfies the pattern described by `regex`.
In general, however, this is not how regexes behave.

Take a look at regexes in other languages:

```java
// Java
Pattern.matches(regex, string)
```

```csharp
// C#
new Regex(regex).IsMatch(string)
```

```ruby
# Ruby
/regex/ =~ string
```

```javascript
// JavaScript
/regex/.exec(string)
```

All these implementations differ from `re.fullmatch` in that they
only expect a *substring* of `string` to satisfy the pattern.

For example, consider the regex `a`. In Python, `re.fullmatch('a', string)`
only returns a truthy value if `string` equals `a`, because `fullmatch`
requires the *entire* string to be described. In other words, `re.fullmatch('a', 'bab')` is not a match.

In the other languages, however, matching the regex `a` with the string `bab` will succeed since the regex will be interpreted as "There is a substring of `bab` that matches the regex `a`." It is important you are aware of this distinction to avoid unpleasant surprises in the future.

Now, is there a way to make Python behave like the other languages? There sure is!
Simply use `re.search` instead of `re.fullmatch`. In essence, `re.search(regex, string)` is the same as `re.fullmatch('.*regex.*', string)`.

Make use of `re.search` to solve this exercise.
# Assignment

As discussed before, Python provides the following functions:

* `re.fullmatch(regex, string)` expects the entire `string` to match `regex`.
* `re.search(regex, string)` expects part of `string` to match `regex`.

There is a third function that checks if the *beginning* of `string` matches `regex`.
Look for it in the [Python docs](https://docs.python.org/3/library/re.html) and use it to solve this exercise.

Write a function `starts_with_a(string)` that checks whether `string` starts with an `a`.
# Assignment

Write a function `is_number(string)` that determines if `string`
represents a valid number. A number consists of a number of digits,
*optionally* followed by a dot and another series of digits.

The dot might prove problematic: `.` already means something in regex-speak.
If you need an actual dot to appear in the string,
you will need to *escape* it: use `\.` instead of `.`

You already know about the following shortcut operators:

* `x*` means the same as `x{0,}`.
* `x+` means the same as `x{1,}`.

There exists another such prefix operator corresponding to `x{0,1}`, i.e.,
expressing that `x` is optional. Look for it in the [documentation](https://docs.python.org/3/library/re.html) and make use of it for this exercise.
# Assignment

Write a function `is_valid_student_id(string)` that verifies if `string`
represents a valid student id. A student consists of either `s` or `r` (both lowercase and uppercase are allowed)
followed by seven digits.
# Assignment

Write a function `twice_repeated(string)` that checks if `string`
consists of two repetitions of the same character, e.g., `aa`, `55` of `...`.

## Backreferences

To solve this, you will need *backreferences*. These allow you
to refer to something encountered earlier in the string.
In essence, to solve this exercise, you want to build a regex with the following structure:

* Match a single character. Since there are no restrictions on what this character can be,
  we use `.` to represent this.
* This next character must be followed by *the same character* encountered earlier.

Backreferences allow you to express the second step as follows:

* First, you need to express the first character is important, that it needs to be 'remembered'. You achieve this by putting this pattern between parentheses. In our case, this leads to `(.)`
* In order to refer to whatever matches with `(.)`, you use a backreference `\1`.

This gives you `(.)\1` as regex. However, there's still a small annoying issue you need to deal with.

## Raw Strings

Technically, the regex `(.)\1` is the correct solution to this exercise. Unfortunately, using

```python
def twice_repeated(string):
    return re.fullmatch('(.)\1', string)
```

will not work. Why not?

Say you need a string with a newline in it, for example

```text
a
b
c
```

 In most languages, you can't just add these newlines in a string directly:

 ```java
 // Invalid code
 String str = "a
 b
 c";
 ```

Instead, you need to rely on escape sequences:

```java
String str = "a\nb\nc";
```

Here, the compiler sees the string literal `"a\nb\nc"` and replaces
each occurrence of `\n` by an actual newline. At runtime,
the string is 5 characters long.

`\n` is not the only existing escape sequence. There's also `\t` for tabs,
`\b` for backspace, etc. If you need your string to contain an actual
backslash, you can use `\\`. You can also refer to symbols using their
[ASCII code](http://www.asciitable.com/), e.g. `\42`.

The newline character has decimal code 10. You might expect `\10` to be synonymous with `\n`, but that would of course be too simple: instead, the `\10` is interpreted
as an *octal* value, not decimal. 10 in octal is 12, so `\12` corresponds to the newline character. You can verify this in the Python shell:

```python
>>> '\12'
'\n'
```

So, why do we tell you this? Well, let's go back to our regex: `(.)\1`.
The Python interpreter sees this `\1` and thinks that you mean
to refer to the character with ASCII code 1, so it replaces
`\1` with this character. Next, the regex engine receives
this weird character instead of `\1`, meaning it will not
recognize it as a backreference.

Somehow, you need `\1` to reach the regex engine unscathed. One way would
be to escape the backslash: `\1` thus becomes `\\1`. The Python interpreter
sees `\\1`, recognizes the escape sequence `\\` and replaces it with a single backslash,
resulting in the regex engine receiving `\1`.

Doubling all backslashes solves our problem, but there is a more readable
solution: raw strings. By prefixing a string with `r`, you tell
the Python interpreter to leave the string alone.
For example, whereas `\n` is a string containing a single character (a newline),
`r'\n'` is a string counting two characters: a backslash followed by the letter `n`.

Back to our exercise: you need `(.)\1` to reach the regex engine.
You can achieve this in either of the following ways:

```python
# Using escape sequences
return re.fullmatch('(.)\\1', string)

# Using raw strings
return re.fullmatch(r'(.)\1', string)
```

We strongly advise you to make use of raw strings. It might even
be safer to simply always use raw strings when dealing with
regexes, regardless of whether it is actually necessary.
# Assignment

Write a function `thrice_repeated(string)` that checks if `string`
consists of three repetitions of the same characters, e.g.,
`xxx`, `121212` or `abcabcabc`.
# Assignment

Write a function `ababa(string)` that checks if `string`
exhibits an `ABABA` structure, meaning that it starts
with some pattern `A` followed by some pattern `B`.
After this, `A` is repeated, then `B` is repeated,
and lastly `A` is repeated once more.
# Assignment

Write a function `contains_no_a(string)` that checks that `string` does not contain the letter `a`.

To solve this problem, you could of course enumerate all characters *except* `a`, but that
would result in quite a long regex. Luckily, there is a shorter way: *negated character classes*.
Look up the syntax and use it to implement `contains_no_a`.
# Assignment

Write a function `is_valid_time(string)` that verifies if `string` represents a valid time.
Time must be formatted as `hh:mm:ss.fff`, where `fff` represents milliseconds and is optional.
# Assignment

Write a function `is_valid_email_address(string)` that verifies if `string`
represents a valid email address. The rules are as follows:

* `string` must contain exactly one `@`.
* Before the `@`, only lowercase letters, digits and dots are allowed.
* After the `@`, one of the following domains must appear:
  * `ucll.be`
  * `student.ucll.be`
# Assignment

Write a function `is_valid_password(string)` that checks if `string`
satisfies the following conditions:

* It must be at least 12 characters long.
* It must contain at least one digit.
* It must contain at least one lowercase letter.
* It must contain at least one uppercase letter.
* It must contain at least one of the following special character: `+-*/.@`.
* It must not contain three times the same character in a row.
* It must not contain four times the same character.
# Assignment

Regular expressions have more than one use. Until now, you've only used them
to check if they match a specific pattern.

Say you ask the user for a time of day. You expect it to be in the format
`hh:mm:ss`. To check whether this pattern is satisfied, you write:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}', string):
    # ...
```

where `\d` is short for `[0-9]`. Once you've ensured that `string` has
the correct format, you can proceed to extract the hours, minutes and seconds from it.
One way to do this would be:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}', string):
    h, m, s = string.split(':')
```

Simple enough. Now, imagine you also want to introduce milliseconds: `hh:mm:ss.fff` but where the milliseconds are optional. You update your check:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}(\.\d{3})?', string):
    # ...
```

Grabbing the components becomes a bit more complex though. You could do it as follows:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}(\.\d{3})?', string):
    if '.' in string:
        left, ms = string.split('.')
        h, m, s = left.split(':')
    else:
        h, m, s = string.split(':')
        ms = '.000'
```

It works, but it's certainly not as clean. You can imagine this quickly
becomes more complex with more elaborate patterns.

Luckily, regexes offer functionality to *capture* pieces of the string.
This is done by marking the parts of the pattern you're interested in using
parentheses:

```python
if re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string):
    # ...
```

This tells the regex engine to store the parts of `string` that match those
patterns. Now, how do we access this data?

`fullmatch`, as well as `match` and `search`, don't return a boolean value.
If the string does not match the pattern, they return `None`, which is a falsey value,
making the `if` condition fail. But if there is a match, a `Match` object is returned, which contains all kinds of interesting information.

Let's take a closer look at our regex:

```text
(\d{2}):(\d{2}):(\d{2})(\.\d{3})?

|-----| |-----| |-----||-------|
   1       2       3       4
```

There are four pairs of parentheses, each of which designate a *group*.
Each group has its own index, starting counting from 1. To get the
strings that corresponds to each group, you can write:

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h = match.group(1)
    m = match.group(2)
    s = match.group(3)
    ms = match.group(4) or '.000'
```

The `or '.000'` is necessary because the fourth group is optional: if `string`
were to equal `12:34:56`, then `match.group(4)` would return `None` to indicate
that that part was omitted in `string`. The `or '.000'` is equivalent to

```python
ms = match.group(4)

if ms is None:
    ms = '.000'
```

This trick is not specific to regexes: you can use it anywhere you
wish to replace a 'missing' value with a default value.

`match.groups()` returns all groups as a tuple, which allows you to shorten your code to

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h, m, s, ms = match.groups()
    ms = ms or '.000'
```

The `groups` method also allows you to specify defaults for missing values:

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h, m, s, ms = match.groups('.000')
```

Now write the function `parse_time(string)` that expects a time with optional milliseconds.
The time can be any stopwatch-based time: e.g. 00:00:00:001, 11:12:13 or 37:42:09.642 all should be valid strings.
If `string` is invalid, the function should return `None`, otherwise it should
return a tuple with four integers representing the hours, minutes, seconds
and milliseconds components of the given time.
# Assignment

Write a function `parse_link(string)` that receives an html `a`-element `<a href="...">...</a>`, extracts the link and caption from it, and returns it as a tuple `(caption, link)`.

If `string` is not a well-formed `a` element, it should return `None`.
# Assignment

Write a function `collect_links(string)` that receives an html document
and collects all `href`s from `a` elements.

Look through the [documentation](https://docs.python.org/3/library/re.html)
for a function that takes over the brunt of the work for you.
# Assignment

Write a function `scrape_email_addresses(string)` that extracts all email addresses
occurring in `string`.
# Assignment

Regular expressions can also be used to perform substitutions in text:
you can ask any substring that matches a certain pattern
to be replaced according to some rules. This functionality
is embodied by the `sub` function in the `re` module.

Let's start with something relatively simple.

Are you one of those people who can't stand useless whitespace
at the end of lines in your code? Do you maniacally
remove it whenever you notice it? Did you perhaps
even look for an option in your editor to automatically
remove that trailing whitespace (because there is one in Visual Studio Code, you know.)
Good news, everyone! This exercise will let you write a function `remove_trailing_whitespace(string)` that hunts down those horrible
utterly useless spaces and shreds them to nothingness.

`sub` takes three parameters:

* A regex
* A replacement string
* The string in which to perform the substitutions

Let's find out which values to pass to `sub`.

The third parameter is easy: it's whatever string `remove_trailing_whitespace` receives.
The second parameter is not too difficult either: since we want
to make something disappear, the replacement string should simply be `''`.

Lastly, the regex. We need a pattern that matches trailing whitespace, i.e.,
spaces that appear at the end of a line. We'll let you look for the answers
to this riddle in the [documentation](https://docs.python.org/3/library/re.html).
Hints: there is a special character that matches the end of lines, but you
need to turn on multiline mode.
# Assignment

Sometimes, when you're typing some text, you accidentally type a word twice.
Or even thrice.
It happens to the best of us.
So let's write a function `remove_repeated_words` that removes duplicated words.

To accomplish this, you'll need to know a bit more about `sub`: if your regex contains one or more groups, you can refer to them in the `sub`'s second parameter.
For example:

```python
re.sub(r'(.)', r'\1\1', string)
```

The `.` in the regex matches with any character.
The parentheses around the dot tell `sub` that whatever matches `.` should be remembered.
Next, the `r'\1\1'` in the replacement string expresses that whatever matched `(.)` needs to be repeated twice.
If you were to try it out in a Python shell, you'd get:

```python
>>> re.sub(r'(.)', r'\1\1', 'abc')
'aabbcc'
```

Tip: look in the documentation for a way to define the start and end of a word.

# Assignment

Some foolish American lady wrote a long text but with all the dates wrong!
She used `2/1/2000` to refer to the first of February 2000, while the correct notation is of course `1/2/2000`.
This means we'll have to write a script that swaps around day and month in all dates.

Write a function `correct_dates(string)` that performs this task.
# Assignment

Write a function `hide_email_addresses(string)` that replaces
all email addresses occurring in `string` by `***`, as many
asterisks as there are characters in the address.

Solving this one requires delving deeper into `sub`'s capabilities.
Instead of passing a string as second parameter, you can
also pass a function that computes the replacement string.

As an example, let's revisit the previous exercises
and rewrite them using a function replacement parameter.

```python
def remove_trailing_whitespace(string):
    def replace(match):
        return ''

    return re.sub(' +$', replace, string, flags=re.MULTILINE)
```

Here, `''` has been replaced by a function returning `''`.
This is a typical pattern in programming: replace
data with code that produces the same data. Once you
have done that, you can make the function smarter.

Next, `remove_repeated_words`:

```python
def remove_repeated_words(string):
    def replace(match):
        return match.group(1)

    return re.sub(r'([a-zA-Z]+)( \1)+', replace, string)
```

Notice how `replace` accepts an argument: this is a match object
like the one `fullmatch`, `match` and `search` return.
`replace` then asks for the match object for the contents
of the first group, which corresponds to the duplicated word.

Lastly, `correct_dates`:

```python
def correct_dates(string):
    def replace(match):
        m, d, y = match.groups()
        return f'{d}/{m}/{y}'

    return re.sub(r'(\d+)/(\d+)/(\d+)', replace, string)
```

Here, `replace` uses the `groups()` method to retrieve
the month, day, and year and returns a string where
they have been reordered.

Now you should be able to write `hide_email_addresses`.



**For the documentation, I'm sure u can find this online, so I'm nog gonna paste it in here.**

# Mapping

Consider the following algorithm:

```python
def squares(ns):
    result = []
    for n in ns:
        result.append(n**2)
    return result


>>> squares([0, 1, 2, 3, 4])
[0, 1, 4, 9, 16]
```

While it may not be the most useful code, it follows a certain pattern: given a list of values, it applies an operation on each of them and collects the results in a new list.
Here, the operation is squaring.

This pattern occurs quite often, typically as part of a bigger whole:

* Given a list of items, get the price of each item (and take the sum to get the total cost).
* Given a list of enemies, check if any one of them touches the player (and if so, the player is dead).
* Given a list of exam questions, grade each of them (and compute the final grade).

This pattern is called _mapping_: it _maps_ each value from an input list to corresponding value which is stored in an output list.
Python provides a special syntax for this mapping operation.
We can rewrite the function above as

```python
def squares(ns):
    return [n**2 for n in ns]
```

This is called a _list comprehension_ and is a more concise (and readable) way to perform mappings.
They also have performance benefits.
Running the provided script `benchmark.py` shows this:

```bash
$ py benchmerk.py
squares_loop used 0.764 seconds
squares_loop2 used 0.867 seconds
squares_comprehension used 0.642 seconds
```

## Tasks

The file `movie.py` (which you'll find not in this exercise's directory but one directory up) defines the class `Movie`.
Its attributes are

* title
* runtime
* director
* actors
* year
* genres

Write the following functions, many of which operate on a list of `Movie` objects:

* `titles(movies)` returns the movie titles.
* `titles_and_years(movies)` returns the movie titles and their year, grouped in pairs: `[(title1, year1), (title2, year2), ...]`.
* `titles_and_actor_counts(movies)` returns the movie titles paired up with the number of actors.
* `reverse_words(sentence)` must reverse each word in the given string `sentence`.
  Words are separated by one space.
# Filtering

```python
def select_adults(people):
    result = []
    for person in people:
        if person.age >= 18:
            result.append(person)
    return result
```

This little function selects `Person`s whose age is at least `18`.
Or, more generally, given a list `lst` of values, it returns a new list that contains all items from `lst` that satisfy a certain condition.
This is typically called _filtering_.

As with mapping, Python also has a special syntax for it.
Fortunately, it fits in with the already existing syntax for list comprehensions:

```python
def select_adults(people):
    return [person for person in people if person.age >= 18]
```

It is of course possible to combine mapping with filtering.
Say you want the names of all adults:

```python
def select_adult_names(people):
    return [person.name for person in people if person.age >= 18]
```

For the sake of readability, you might want to spread it over multiple lines:

```python
def select_adult_names(people):
    return [
        person.name
        for person in people
        if person.age >= 18
    ]
```

## Tasks

Write the following functions:

* `movies_from_year(movies, year)` returns the titles of movies from the given `year`.
* `movies_with_actor(movies, actor)` returns the titles of movies that have `actor` in it.
* `divisors(n)` returns the divisors of `n` in increasing order. For example, `divisors(12)` should return `[1, 2, 3, 4, 6, 12]`.
# Set Comprehension

A list comprehensions constructs a list, no big surprise there.
If instead we want a set, this is also possible: we need only change the brackets.

```python
def squares(ns):
    return {n**2 for n in ns}
```

Using a set instead of a list will cause duplicates to disappear from the end result:

```python
>>> [n**2 for n in range(-10, 10)]
[100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> {n**2 for n in range(-10, 10)}
{64, 1, 0, 100, 36, 4, 9, 16, 81, 49, 25}
```

Also note how the order of the items is not preserved.

## Tasks

Write the following functions:

* `directors(movies)` collects all directors in a set.
* `common_elements(xs, ys)` should return the set of values that occur both in `xs` and `ys`.
# Dictionary Comprehension

One can also rapidly construct dictionaries using _dictionary comprehensions_.
Say for example we have a list of `Student`s and want to quickly find a `Student` object based on its `id`.
Using a list would require a linear search:

```python
def find_student_with_id(students, id):
    for student in students:
        if student.id == id:
            return student
```

By storing them in a dictionary, this search can be done much more efficiently:

```python
>>> students_by_id = {student.id: student for student in students}

>>> students_by_id[id]
```

You can run the provided `benchmark.py` script to check how much execution time is improved by using a dictionary:

```bash
$ py benchmark.py
13.86886960011907
0.009574900148436427
```

## Tasks

Write the following functions:

* `title_to_director(movies)` returns a `dict` whose keys are movie titles and values are the corresponding director.
* `director_to_titles(movies)` returns a `dict` where keys are directors and values are lists of movie titles by that director.
  You will need to combine different kinds of comprehensions for this one.
  Note that we are not looking for an efficient solution.
# FlatMap

Consider the following list comprehension:

```python
>>> [[(x, y) for x in range(3)] for y in range(3)]
[
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)]
]
```

As you can see, nothing prevents you from using comprehensions within comprehensions.
In the example above, the result is a list of lists of coordinates.
However, what if we didn't want this nested structured, but instead wished for a list of coordinates?

We want to "flatten" the list of lists into a list.
We can achieve this by rewriting the comprehension above as follows:

```python
>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

You can combine as many `if`s and `for`s as you wish in this way.

## Tasks

* Write a function `genres(movies)` that collects all movie genres in a set.
* Write a function `actors(movies)` that collects all movie actors in a set.
* Write a function `repeat_consecutive(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_consecutive([1, 2, 3], 4)` should return `[1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]`.
* Write a function `repeat_alternating(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_alternating([1, 2, 3], 4)` should return `[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]`.
* Write a function `cards(values, suits)` that returns a set of all cards that can be made using `values` and `suits`.
  For example, `cards([2, 5, 10], ['hearts', 'diamonds'])` should return `{Card(2, 'hearts'), Card(5, 'hearts'), Card(10, 'hearts'), Card(2, 'diamonds'), Card(5, 'diamonds'), Card(10, 'diamonds')}`.
  You should import the `Card` class from `util`.
# Functions

Python comes with a number of built-in functions, most of which you probably already know.
These functions are often used in conjunction with comprehensions, so let's make a few exercises on them.

> Note that these functions are not aware how their arguments are constructed.
> You can use them on any list/set/dictionary: the only thing that matters is that it is _iterable_.

We give a short overview of these functions.
Use it as a hint to solve the exercises.

## `len`

`len` returns the number of items in the collection.

## `min` and `max`

These functions, as their names imply, look for the smallest and greatest element of a collection (a list, a set, anything iterable).
Make sure though not to pass an empty collection.

## `sum`

`sum` takes the sum of all the elements.

## `all` and `any`

`all` checks if all elements in the given collection are truthy.
If so, the function returns `True`, otherwise `False`.

`any` is easier to please: it will return `True` is at least one of the values in the given collection is truthy.

## `zip`

`zip` takes two collections and pairs up their first elements, then second elements, etc.
An example will make this clearer:

```python
>>> xs = ['a', 'b', 'c']
>>> ys = [1, 2, 3]
>>> list(zip(xs, ys))
[('a', 1), ('b', 2), ('c', 3)]
```

## `enumerate`

Enumerate pairs up elements with their index.

```python
>>> xs = ['a', 'b', 'c']
>>> list(enumerate(xs))
[(0, 'a'), (1, 'b'), (2, 'c')]
```

## Tasks

Write the following functions and rely on comprehensions and the functions above.

* `movie_count(movies, director)` returns the number of movies made by `director`.
* `longest_movie_runtime_with_actor(movies, actor)` returns the runtime duration of the longest movie in which `actor` appears.
* `has_director_made_genre(movies, director, genre)` returns `True` is `director` made a movie of the given `genre`.
* `is_prime(n)` checks whether `n` is a prime number, i.e., that it is only divisible by 1 and itself.
* `is_increasing(ns)` checks whether the values in `ns` appear in nondecreasing order.
  For example, `is_increasing([1, 1, 2, 3, 4, 6])` should return `True`, whereas `is_increasing([3, 2, 1])` should yield `False`.
* `count_matching(xs, ys)` counts how many of the corresponding elements are equal.
  For example, `count_matching([1, 2, 3], [3, 2, 1])` should return `1`, because only equal values on equal positions are counted.
* `weighted_sum(ns, weights)` should multiply each value in `ns` with its corresponding weight in `weights` and return the sum of these products.
  For example, `weighted_sum([a, b, c], [x, y, z])` should return `a * x + b * y + c * z`.
* `alternating_caps(string)` should change the case of each character such that they alternate between upper and lower case.
  For example, `alternating_caps("abcdef")` should return `AbCdEf`.
* `find_repeated_words(sentence)` first collects all words in the given string `sentence`.
  A word is defined as a series of letters (can be both upper and lowercase).
  Next, the function has to look for repeated consecutive words and collect them in a set.
  The case of letters should be ignored: `"dog"` and `"Dog"` are to be considered the same word.
  For example, `find_repeated_words("This sentence has has repeated words.   Words.")` should return the set `{'has', 'words'}`.
  The returned set should contain all of its words in lower case.
  Note also that interpunction, spaces, etc. should also have no impact on deciding whether a word is repeated or not.

# Smart Parameters

Say we're working on our `Movie`s and we want to determine how many movies a certain director has made.
We can then write the following code:

```python
len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

For some reason, we need this in multiple places.
We build a function around it so we don't need to repeat this code:

```python
def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

Now, hard coding values like this is a bit of a [code smell](https://en.wikipedia.org/wiki/Code_smell).
Let's first put the string in a separate variable:

```python
def count_movies_by_spielberg(movies):
    director = 'Steven Spielberg'
    return len([movie for movie in movies if movie.director == director])
```

And now we can turn this very specific function into a more generalized one by promoting the `director` variable to a parameter:

```python
def count_movies_by_director(movies, director):
    return len([movie for movie in movies if movie.director == director])
```

This is much better: it still allows us to count movies made by Spielberg, but also by any other director.

But what if we want to count movies with a certain actor in it?
We can easily write a new function:

```python
def count_movies_with_actor(movies, actor):
    return len([movie for movie in movies if actor in movie.actors])
```

Oh no, now we want to count the number of movies made in a certain year:

```python
def count_movies_in_year(movies, year):
    return len([movie for movie in movies if movie.year == year])
```

Or movies made during a certain time period:

```python
def count_movies_between_years(movies, min_year, max_year):
    return len([movie for movie in movies if min_year <= movie.year <= max_year])
```

You see where this is going: these functions have a lot in common, and that counts as duplication.
And that's a bit of a problem.
Let's see how we can solve this.

## Generalizing `count_movies_by_spielberg`

Let's go back to our `count_movies_by_spielberg` function.

```python
def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if movie.director == 'Steven Spielberg'])
```

It is identical to all other functions except for the condition in the `if`.
Let's move this condition in a separate function.

```python
def is_made_by_right_director(movie):
    return movie.director == 'Steven Spielberg'


def count_movies_by_spielberg(movies):
    return len([movie for movie in movies if is_made_by_right_director(movie)])
```

Remember what we did when we generalized `count_movies_by_spielberg` to `count_movies_by_director`?
This is very similar: instead of introducing a new variable (`director`) we put the entire condition in a separate function `is_made_by_right_director`.
Now we can perform the same trick and turn it into a _parameter_:

```python
def count_movies_by_director(movies, is_made_by_right_director):
    return len([movie for movie in movies if is_made_by_right_director(movie)])
```

This will work: functions are values just like integers, booleans, list, etc. so there's no reason to believe we cannot pass them as arguments.

## Generalizing `count`

Let's see how we can use `count_movies_by_director`:

```python
def is_made_by_spielberg(movie):
    return movie.director == "Steven Spielberg"

def is_made_by_scorsese(movie):
    return movie.director == "Martin Scorsese"


>>> count_movies_by_director(movies, is_made_by_spielberg)
>>> count_movies_by_director(movies, is_made_by_scorsese)
```

This is not very impressive: we could do that before too.
But if you look at `count_movies_by_director`'s implementation, there's nothing specific about _directors_.
The function is not restricted to only considering a movie's director.

```python
def has_tom_cruise_as_actor(movie):
    return 'Tom Cruise' in movie.actors

>>> count_movies_by_director(movies, has_tom_cruise_as_actor)
```

This would actually work and return the number of movies with Tom Cruise in it.
The name of the function, `count_movies_by_director`, is quite misleading really: it can actually be used with _any_ condition.
Let's rename it:

```python
def count_movies(movies, should_be_counted):
    return len([movie for movie in movies if should_be_counted(movie)])
```

This function `count_movies` can replace all the functions we discussed above.
For example,

```python
def is_from_eighties(movie):
    return 1980 <= movie.year < 1990

>>> count_movies(movies, is_from_eighties)
```

## Higher Order Functions

`count_movies` takes a function as parameter.
Functions receiving functions are called _higher order functions_.

We can further generalize `count_movies`: nowhere does it "know" its first parameter is a list of `Movie`s.
It could be a list of `Person`s, strings, numbers, etc.

```python
def count(xs, should_be_counted):
    return len([x for x in xs if should_be_counted(x)])
```

Now we have a single `count` function that can count any kind of objects based on any condition.
This would not have been possible without using function arguments.

This kind of generalization is very important.
When writing code, you should always watch out for arbitrary limitations and see if introducing parameters can make it more generally usable.

## Task

Let's have you write some higher order functions.
We start off simple:

```python
def say_hello():
    print("Hello!")

>>> repeat(say_hello, 5)
Hello!
Hello!
Hello!
Hello!
Hello!
```

Write a function `repeat(function, n)` that simply calls `function` `n` times.
You can assume `function` takes no arguments and returns nothing useful.
# Generalizing

In the last exercise, we showed how we could construct a very flexible `count` function.
We'll take on a different function in this exercise.

```python
def children_and_adults(people):
    children = []
    adults = []

    for person in people:
        if person.age < 18:
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

This function partitions a given list `people` into two parts: the children (whose `age` is less than 18) and adults (all the rest).
In order to generalize this function, we need to identify which part needs to become a parameter.

An unambitious effort would be

```python
def children_and_adults(people, cutoff_age):
    children = []
    adults = []

    for person in people:
        if person.age < cutoff_age:
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

We turned the `18` into a parameter, allowing us to pick the age (e.g. `16`, `21`, ...) that serves as cutoff point.
We can do better than that though.
Let's replace the entire `if` condition:

```python
def children_and_adults(people, condition):
    children = []
    adults = []

    for person in people:
        if condition(person):
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

We should update the names of the function and variables as there is nothing in this code that ties it specifically to `Person`s.

```python
def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)
```

## Task

Generalize the following function:

```python
def find_first_book_by_author(books, author):
    for book in books:
        if book.author == author:
            return book
    return None
```
# Group By

Write a function `group_by(xs, key_function)` that groups elements with the same key in a dictionary.
The key of an element can be found using `key_function`.
A few examples might make this clearer:

## Example 1

```python
def age(person):
    return person.age


>>> group_by([
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
], age)
{
    14: [Person(name='John', age=14)],
    15: [Person(name='Sophie', age=15), Person(name='Morgan', age=15)],
    17: [Person(name='Marc', age=17), Person(name='Chris', age=17)]
}
```

The above code groups `Person`s by age.

## Example 2

```python
def card_suit(card):
    return card.suit


>>> group_by([
    Card(value=2, suit='hearts'),
    Card(value=5, suit='clubs'),
    Card(value=4, suit='hearts'),
    Card(value=10, suit='hearts'),
])
{
    'hearts': [Card(value=2, suit='hearts'), Card(value=4, suit='hearts'), Card(value=10, suit='hearts')],
    'clubs': [Card(value=5, suit='clubs')]
}
```

Here, the same function is used to group cards by suit.
# Take While

Write a function `take_while(xs, condition)` that looks for the first element in `xs` for which the function `condition` does not return a truthy value.
All values before this element should be put in one list, the remaining in another.
These two lists should be returned in a tuple.

```python
def is_negative(x):
    return x < 0

>>> take_while([-4, -2, 0, -1, 4, 6],is_negative)
([-4, -2], [0, -1, 4, 6])
```

The difference with `partition` is that `partition` goes through the entire list whereas `take_while` stops at the first element for which `condition` yields a falsey value.
# Indices Of

Write a function `indices_of(xs, condition)` that returns the indices of all the elements for which `condition` returns a truthy value.

```python
def is_odd(x):
    return x % 2 != 0

>>> indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd)
[0, 2, 4, 6]
```
# Merge Dictionaries

Say we represent orders as dictionaries, where keys are items and values are amounts.

```python
>>> order1 = {'banana': 4, 'coke': 12}
>>> order2 = {'mustard': 1, 'chocolate': 7}
```

We'd like to combine both orders into a single dictionary.
The easiest way to achieve this in Python is to use the `**` operator:

```python
>>> combined = {**order1, **order2}
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 7}
```

However, what happens if the dictionaries share keys?

```python
>>> order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
>>> order2 = {'mustard': 1, 'chocolate': 7}
>>> combined = {**order1, **order2}
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 7}
```

As you can see, `order2` "wins": the three chocolates from `order1` completely disappear.
We would like a smarter dictionary merge, one that takes the sum of the values:

```python
>>> order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
>>> order2 = {'mustard': 1, 'chocolate': 7}
>>> combined = merge_dictionaries(order1, order2)
{'banana': 4, 'coke': 12, 'mustard': 1, 'chocolate': 10}
```

However, sometimes the sum is not what we want.
Say the dictionaries represent grades:

```python
>>> january_exams = {'P1': 9, 'FE': 15}
>>> august_exams = {'P1': 7}
```

Combining `january_exams` and `august_exams` should yield the final grades, but taking the sum, while it sounds very inviting, is not the right way to deal with shared keys.
Rather, the rule is that the combination must contain the _maximum_ of the grades:

```python
>>> final_grades = merge_dictionaries(january_exams, august_exams)
{'P1': 9, 'FE': 15}
```

`merge_dictionaries` cannot know whether it should take the sum, or the maximum, or something else altogether.
We therefore need to supply this information using a parameter, namely a function that decides what to do when two values vie for a place in the final dictionary.

Write a function `merge_dictionaries(d1, d2, merge_function)` that returns a new dictionary using the following rules:

* If a key only appears in `d1`, simply copy it and its corresponding value to the resulting dictionary.
* Same for `d2`.
* If a key `k` appears both in `d1` and `d2`, then the corresponding values `d1[k]` and `d2[k]` are fed to `merge_function`.
  This becomes the value for `k` in the resulting dictionary.
# Nested Functions

Let's revisit an old example:

```python
def is_made_by_spielberg(movie):
    return movie.director == 'Steven Spielberg'


def count_films_by_spielberg(movies):
    return count(movies, is_made_by_spielberg)
```

We had to define a separate little function `is_made_by_spielberg` to be passed to `count`.
This feels rather clumsy.

What if we want to write a function `count_films_by_director(movies, director)` and rely on `count` in the process?
Let's try...

```python
def is_made_by_director(movie):
    return movie.director == director


def count_films_by_director(movies, director):
    return count(movies, is_made_by_director)
```

This won't work: we mean `is_made_by_director` to refer to `count_films_by_director`'s second parameter, but Python will not understand it that way.
Parameters are by definition local and only accessible within the corresponding function.
So, how can we give `is_made_by_director` access to `director`?

Well, we just said that parameters are only visible inside the corresponding function.
That's the solution!
We can move `is_made_by_director` inside `count_films_by_director`!

```python
def count_films_by_director(movies, director):
    def is_made_by_director(movie):
        return movie.director == director

    return count(movies, is_made_by_director)
```

This is called a _nested_ or _inner_ function.
This has two consequences:

* `is_made_by_director` can now access variables inside `count_films_by_director` such as `movies` and `director`.
* `is_made_by_director` is only accessible from within `count_films_by_director`: it is essentially a local variable.

## Tasks

Write the following functions:

* `count_older_than(people, min_age)` counts the number of people who are older than `min_age`.
* `indices_of_cards_with_suit(cards, suit)` returns the indices of all the `Card`s whose suit equals `suit`.

Rely on previously defined higher order functions.
# Lambdas

When calling a higher order function like `count`, we need to pass it some function.
Previously, we discussed how it was possible to define this function locally:

```python
def count_films_by_director(movies, director):
    def is_made_by_director(movie):
        return movie.director == director

    return count(movies, is_made_by_director)
```

Having to define local functions like this can become tiring quickly.
Luckily, Python offers a shorter syntax.
Let's do something weird first and let's define `is_made_by_director` using an alternative syntax:

```python
def count_films_by_director(movies, director):
    is_made_by_director = lambda movie: movie.director == director
    return count(movies, is_made_by_director)
```

Let's dissect this weird new thing.

* The name `lambda` comes from [the lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus), which is a tiny programming language developed around a century ago.
  You can simply pretend lambda means "function".
* `movie` is the parameter of this function.
* What follows the `:` is the body of the function.
  No `return` is necessary, it happens implicitly.

Now, we also know that

```python
x = 5
print(x)

# is the same as

print(5)
```

Let's apply this substitution trick on our function:

```python
def count_films_by_director(movies, director):
    return count(movies, lambda movie: movie.director == director)
```

So, a _lambda_ is nothing more than an anonymous function.
It is used in cases where we need to quickly define a function with the whole `def`
Instead, we define it inline where it's needed.
In essence, it's a throw-away function.
We don't even bother naming it.

Note that lambdas can only be used for very simple functions: the lambda's body is limited to a single expression.
This is a Python-specific limitation: for nontrivial logic, the language wants you to define a named function using `def`.

## Task

Write the following functions, relying on lambdas and on the helper classes/functions provided in `util.py`:

* `group_by_suit(cards)` groups `cards` by their suit.
* `group_by_value(cards)` groups `cards` by their value.
* `partition_by_color(cards)` splits `cards` into two lists: the first list contains only black cards, the second list only red cards.
  The color of a card is determined by its suit: spades and clubs are black, hearts and diamonds are red.
# Sorting

Python comes with two standard ways of sorting lists:

```python
>>> ns = [1, 3, 9, 7, 8, 4, 6, 2, 5]

# sorted returns a *new* list
>>> sorted(ns)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# ns is left untouched by sorted
>>> ns
[1, 3, 9, 7, 8, 4, 6, 2, 5]

# You can also sort in-place
>>> ns.sort()
>>> ns
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Which one you need depends on your needs.

Now, how do `sort`/`sorted` decide what order to put the list's values in?
With numbers, it might seem intuitive to order them from smallest to greatest, but what about strings?
Alphabetically seems standard, but case sensitive or insensitive?
Should spaces count or be ignored?
And what if we sort `Person`s, `Item`s, `ChessPiece`s?

## `__lt__`

By default, sorting will rely on the `<` operator: if `x < y`, then `x` belongs to the left of `y` in the sorted list.
If you want to be able to sort a list of `Person`s, you will have to give meaning to `person1 < person2`.
You can achieve this by defining the `__lt__` method:

```python
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __lt__(self, other):
        return self.name < other.name
```

Here, we say that a `Person` is "less than" another `Person` if the former's name is "less than" the latter's name.
`<` on strings corresponds to alphabetical case sensitive order: for example, `A < B` and `Z < a`.

This approach is a rather constraining though: we can only define a single sorting order.
We can easily imagine wanting multiple sorting orders on `Person`s: by name, by age, by weight, etc.

## `key`

Both `sort` and `sorted` can take an extra [(keyword) parameter](https://docs.python.org/3/glossary.html#term-argument) `key`: you give it a function that for each element in the list returns the actual value to be used in the sorting process.
For example,

```python
cards.sort(key=lambda card: card.value)
```

Here, the `key` function returns a card's value.
This tells `sort` that the cards should be ordered by value.
If you wanted to sort them by suit, you could write

```python
cards.sort(key=lambda card: card.suit)
```

## Sorting by Two (or More) Values

Say you want to sort your cards by suit, but if they have the same suit, they should be ordered by value.
You can achieve this easily by relying on tuples.

Tuples come with a built-in order.
Consider how to determine if `(a, b) < (c, d)` evaluates `True`:

* First, the first elements are compared: if `a < c`, then `True` is returned.
  If `a > c`, `False` is returned.
* If, however, `a == c`, then the focus shifts on the second elements of the pairs.
  If `b < d`, then `True` is returned.
  If `b > d`, then `False` is returned.
* Since there are no third elements to look at, the comparison ends here and `False` is returned.
  If there had been third, fourth, ... elements, they would have been compared in turn.

So, if we construct a tuple `(card.suit, card.value)` we will get exactly what we desire: first the `suit`s will be compared and if they are equal, the `value`s will be considered.

```python
# Sorts first by suit, then by value
cards.sort(key=lambda card: (card.suit, card.value))
```

## `attrgetter`

In case you find yourself writing many `lambda obj: obj.member` methods, know that there's a quicker way:

```python
from operator import attrgetter


cards.sort(key=attrgetter('suit'))
```

`attrgetter(id)` constructs a function for you, one that takes a function and returns the value of its member called `id`.
In the code shown above, the cards will be sorted by their suit.
In other words

```python
attrgetter('foo')

# is the same as

lambda obj: obj.foo
```

## Task

Write the following functions.
Each function must leave its argument unmodified and return a new list.

* `sort_by_age(people)` orders the `Person`s by increasing `age`.
* `sort_by_decreasing_age(people)` orders the `Person`s by decreasing `age`.
* `sort_by_name(people)` orders the `Person`s by `name`, alphabetically.
* `sort_by_name_then_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by increasing `age`
* `sort_by_name_then_decreasing_age(people)` orders the `Person`s by `name`, and in case of equal `name`s, by decreasing `age`
# Min and Max

We can find the maximum of a series of numbers:

```python
max(numbers)
```

This way we can also find the maximum age of a bunch of `Person`s:

```python
max([person.age for person in people])
```

However, how can we easily find the `Person`s with the maximum age?
`max`, like `sort`, relies on `__lt__`.
This means we could have `Person`'s `__lt__` method compare ages, but that would be very limiting: what if we want the heaviest person, the tallest person, etc.?

We could work in two steps:

```python
max_age = max([person.age for person in people])
oldest_people = [person for person in people if person.age == max_age]
```

However, we'd rather not go through the `Person`s twice (in some cases, this might actually not even be possible, as you'll see later.)
Fortunately, there is a way to tell `max` what we want to maximize.
Like `sort`, it takes a (keyword) parameter `key`.
This should be a function that, given an element of the list, returns the value that should be used for comparisons.

```python
oldest_person = max(people, key=lambda person: person.age)
tallest_person = max(people, key=lambda person: person.height)
heaviest_person = max(people, key=lambda person: person.weight)
```

And of course, the same is true for `min`.

## Task

Write a function `closest(points, target_point)`.

* `points`: a list of points.
* `target_point`: a point.

The function should return the point from `points` that is closest to `target_point`.
In case of a tie, return the point that occurs first in the list.

Points are represented by pairs `(x, y)`.
The distance between two points `(x1, y1)` and `(x2, y2)` equals `((x2-x1)**2 + (y2-y1)**2)**0.5`.
# Iterable

You've encountered multiple collections:

* Lists
* Tuples
* Strings
* Sets
* Dictionaries

Each collection supports a number of operations:

* Each of the four above implements `__len__`, meaning you can use `len(collection)` to determine how many elements it contains.
* Lists, tuples and dictionaries implement `__getitem__`, allowing you to use `collection[k]` to fetch elements.
* Lists offer `append`, while sets have `add` to add values to the container.
  Tuple, being readonly, has no member to add extra elements.

One important operation these collections share may not be so apparent: each of them allow to be _iterated_.
Consider the following pieces of code:

```python
for x in collection:
    # ...

min(collection)

max(collection)

sum(collection)

all(collection)

any(collection)

[expr for x in collection]

" ".join(collection)
```

All of these need to visit each element of `collection` in turn.
They want to be able to operate on any type of collection (set, tuple, list, whatever), but they don't want to have specialized implementations for each such type of collection.
The best way to achieve this is to agree on some standard, uniform way of getting access to all elements of a collection.

For example, one option would be to have each collection type offer a `copy_to_list` method that copies all its items to a list.
This way, no matter what type of collection (set, list, tuple, ...) we receive, we can always rely on `copy_to_list` to get the elements in a list and be on our way.
However, copying everything to a list takes time and memory.
Fortunately, there is a better alternative: _iterators_.

## Iterators

An iterator is an object that can be used to enumerate all elements of a collection.
Say we create such an iterator for lists.
We want to use it as follows:

```python
>>> iterator = ListIterator([1, 2, 3])

>>> iterator.next()
1

>>> iterator.next()
2

>>> iterator.next()
3

>>> iterator.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

As you can see, each call to `next` gives an element of the list.
Let's implement this `ListIterator` class:

```python
class ListIterator:
    def __init__(self, lst):
        self.__list = lst
        self.__current_index = 0

    def next(self):
        # Check if we reached the end
        if self.__current_index == len(self.__list):
            # Raise StopIteration to notify user end of list has been reached
            raise StopIteration()
        # Fetch current element
        result = self.__list[self.__current_index]
        # Move over to next element in list
        self.__current_index += 1
        # Return fetched element
        return result
```

## The Iterator Protocol

Python knows about the concept of iterators.
For example, the `for` loop internally relies on iterators.

Now, in order for Python to recognize an object as an iterator, it expects the object to implement two methods: `__iter__` and `__next__`.
We can adapt our `ListIterator` above to conform to this rule:

```python
class ListIterator:
    def __init__(self, lst):
        self.__elts = lst
        self.__current_index = 0

    def __next__(self):
        # Check if we reached the end
        if self.__current_index == len(self.__elts):
            # Raise StopIteration to notify user end of list has been reached
            raise StopIteration()
        # Fetch current element
        result = self.__elts[self.__current_index]
        # Move over to next element in list
        self.__current_index += 1
        # Return fetched element
        return result

    # Ignore this method for now
    def __iter__(self):
        return self
```

As always, a dunder method should not be called directly.
Using this `ListIterator` goes as follows:

```python
>>> iterator = ListIterator([1, 2, 3])

>>> next(iterator)   # Calls __next__ internally
1

>>> next(iterator)
2

>>> next(iterator)
3

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

As you can see, this `ListIterator` consumes little memory: it does not copy the list, but merely keeps a reference to it.
No matter how long the list, a `ListIterator` will always occupy the same small amount of memory.

## `iter`

Now, this `ListIterator` class actually already exists.
There was no need for us to implement it.
Given a list, we can ask it for an iterator as follows:

```python
>>> xs = [1, 2, 3]
>>> iterator = iter(xs)      # Actually calls xs.__iter__() internally

>>> next(iterator)
1

>>> next(iterator)
2

>>> next(iterator)
3

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

In general, given a `collection`, we are able to call `iter(collection)` on it and get an iterator specialized in that collection.

Note that an iterator is a single-use object: once the end of the collection has been reached, the iterator ceases to be useful.

## Summary

There are two classes two consider: on the one hand we have the the collection or _iterable_ class, on the other we have the corresponding _iterator_ class.

The iterable (collection) class implements `__iter__`.
Examples are `list`, `str`, `tuple`, `set` and `dict`.
This `__iter__` method should return an _iterator_ object.

An iterator object must have these two methods:

* `__iter__`: which simply returns itself.
* `__next__`: which, when called repeatedly, returns the elements of the collection.

An iterator object is single use: it goes through its elements once, after which it ceases to be useful.
If you need to go through the same elements again, you'll have to ask the _iterable_ object for a new iterator.

Following this convention has two advantages:

* On the one hand, functions that operate on a collection (`min`, `max`, `sum`, `any`, etc.) have a uniform, standardized way of accessing all types of collections.
  No specialized code for each collection type is required.
* If you create a new collection class of your own, equipping it with `__iter__` makes is compatible with all existing code that relies on iterators.

This is a recurring concept in software development: conventions make it possible to define new functions/classes/... that fit in a greater whole.
In certain programming languages, it is actually possible to make this intention explicit and ask the language "Did I implement this class correctly? I want it to be iterable."
This is the case with Python: you can _optionally_ make your intention known and ask Python to check your code.
Other languages such as C++, C#, Java, TypeScript _demand_ that you make such intentions clear and will refuse to run your code if you don't.

## Task

You probably have encountered `range` before.
In older versions of Python (pre 3.0), `range` would simply return a list:

```python
# pre Python 3.0
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

However, for large ranges, creating this list would take time and memory.
From Python 3.0 on, `range` is actually a class.

Say you iterate over a `range` object:

```python
for i in range(10):
  # ...
```

Here, `range(10)` creates a `range`-object.
This object is _iterable_, but not an _iterator_.
The `for`-loop needs an _iterator_`, so it uses `iter` to have the iterable create an iterator.
Calling `next` on this iterator produces all the elements of the range.

Create your own `InclusiveRange` (= iterable) and accompanying `InclusiveRangeIterator` (=iterator) class.
It should be usable as follows:

```python
>>> for i in InclusiveRange(1, 5)
...     print(i)
1
2
3
4
5
```

For this to work, `InclusiveRange` needs an `__iter__` method that returns a `InclusiveRangeIterator` object.
`InclusiveRangeIterator` should implement `__iter__` (just have it return `self`) and `__next__`.

Note that `InclusiveRange` should be reusable, but `InclusiveRangeIterator` should be single use:

```python
>>> r = InclusiveRange(1, 5)
>>> list(r)
[1, 2, 3, 4, 5]

>>> list(r)
[1, 2, 3, 4, 5]


>>> iterator = iter(r)
>>> list(iterator)
[1, 2, 3, 4, 5]

# We've used up the iterator, so no more elements are generated by it
>>> list(iterator)
[]
```
# Zip

As explained before, `zip` is a built-in function that pairs up corresponding elements in two or more iterables:

```python
>>> list(zip('abcd', [1, 2, 3, 4]))
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

>>> list(zip('abcd', [1, 2, 3, 4], 'xyzw'))
[('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z'), ('d', 4, 'w')]
```

Note the surrounding call to `list`: this is necessary because `zip` returns an iterator object.

```python
>>> zip('abcd', [1, 2, 3, 4])
<zip object at 0x00000273D6895BC8>
```

Adding `list` forces the iteration over all the elements and stores them in a list, allowing us to see the elements printed out.

What happens when we call `zip` to iterables of unequal size?

```python
>>> list(zip('abcde', [1, 2, 3]))
[('a', 1), ('b', 2), ('c', 3)]
```

It seems that `zip` stops as soon as one of its arguments runs out of elements.

## Task

Write a iterator class `PadZip` that continues producing tuples as long as the _longest_ provided iterable is not empty.
Where values are missing, `None` is added:

```python
>>> list(PadZip('abcde', [1, 2, 3]))
[(a, 1), (b, 2), (c, 3), (d, None), (e, None)]
```

We want to be able to define our own padding value:

```python
>>> list(PadZip('abcde', [1, 2, 3], padding=0))
[(a, 1), (b, 2), (c, 3), (d, 0), (e, 0)]
```

As you can see, the constructor's parameters are

* An iterable object `left`
* An iterable object `right`
* An optional `padding` that defaults to `None`

Note that a `PadZip` object will be an _iterator_, not an _iterable_, meaning it's single use (just like `zip` is):

```python
>>> xs = PadZip('abc', 'xyz')

# First time works
>>> list(xs)
[('a', 'x'), ('b', 'y'), ('c', 'z')]

# Second time does not
>>> list(xs)
[]
```

This means `PadZip` needs the following methods:

* `__iter__` simply returns `self`: for this exercise we don't make a separate iterable class, only an iterator class
* `__next__` returns the next pair

**Hint** You'll need to be able to detect whether an iterator has run out of elements.
For this, you'll have to catch the `StopIterator` exception:

```python
try:
    next_element = next(iterator)
except StopIterator:
    # no elements remain
```
# Repeat

An iterator can also represent infinite collections.
Write a class `Repeat` that keeps producing the same element:

```python
>>> xs = Repeat(5)
>>> next(xs)
5

>>> next(xs)
5

>>> next(xs)
5
```

You should of course be careful with this iterator, lest you end up in an infinite loop:

```python
>>> list(Repeat(5))
# takes a very long time
```

> This functionality [already exists](https://docs.python.org/3/library/itertools.html#itertools.repeat) in Python's standard library.
  The reason we give it as an exercise is because it's easy to implement.
# Cycle

Another example of an infinite sequence is `Cycle`:

```python
>>> xs = Cycle('abcd')
>>> itertools.islice(xs, 10)  # Take 10 first elements
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
```

Implement `Cycle` as an iterator.

> This functionality also [already exists](https://docs.python.org/3/library/itertools.html#itertools.cycle).
> But again, good exercise.
# Generators

Say we want to have a "list" of all numbers starting from 0.
A naive approach would be

```python
def integers():
    result = []
    current = 0
    while True:
        result.append(current)
        current += 1
    return result
```

This of course doesn't work: the loop never ends.
In essence, running this function will just eat up your RAM at high speed.

But thanks to iterators, we can deal with infinite sequences!

```python
class Integers:
    def __init__(self):
        self.__current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__current += 1
        return self.__current
```

Implementing it as an iterator class is not straightforward, especially if the logic becomes more involved.
Since iterators are quite a common pattern in code, many programming languages, among which Python, provide an easier way to implement iterators.
Python offers help in the form of _generator functions_, or _generators_.

To better understand generators, think of what iterators actually do: they're nothing more than objects that return a "list" one element at a time.
It's like having a function, but which instead of returning one value, it should be able to return many.
And that is exactly what generators do.

```python
def integers():
    current = 0
    while True:
        yield current
        current += 1
```

This looks an awful lot like a function, but notice the `yield`.
The presence of this `yield` is what promotes this function to a generator function.

When a (regular) function `return`s a value, the function ends there and then, and all local variables are cleaned up.
Control goes back to the caller, who receives whatever value has been returned by the function.

`yield` works differently: it does also interrupt the function, but all local variables are still kept in memory.
What's more: the generator also remembers the exact location where the execution ended.
This allows a generator to be _resumed_, meaning that it will continue just after the `yield`.

The idea is that when we call a generator function, we get an iterator object.
When we call `next` on this iterator, the generator function's body is executed until the first `yield` is encountered.
Whatever is `yield`ed is used as the result of `next`.
Thus the generator generated the first element of the sequence.

In order to get the second element, we call `next` a second time on the iterator.
Execution of the generator's body _resumes_ and it will run until it encounters a second `yield`.
This produces the second value of the sequence and is returned by `next`.

## Example

Let's add some `print`s to make it clear what gets executed when.

```python
def integers():
    print("Init")
    current = 0
    print("Starting loop")
    while True:
        print(f"Yielding {current}")
        yield current
        print(f"Incrementing current from {current} to {current+1}")
        current += 1

>>> ns = integers()
# Nothing is printed! The body as NOT executed


# Let's see what ns contains
>>> ns
<generator object integers at 0x00000273D689F148>
# This is actually an iterator (i.e., it implements __iter__ and __next__)


# We ask for the first element in the sequence
>>> next(ns)
Init
Starting loop
Yielding 0
0
# The generator's body has only now actually started executing
# It ran until the first yield
# 0 is the value that it yielded and is what is returned by `next(ns)`
# Make sure to understand that the first three lines are printed,
# whereas the last (0) is the return value of next(ns)


# Let's ask for the second element
>>> next(ns)
Incrementing current from 0 to 1
Yielding 1
1
# As you can see, the execution has resumed immediately after the yield
# The local variable current is incremented
# Then it loops back and yields 1


>>> next(xs)
Incrementing current from 1 to 2
Yielding 2
2

>>> next(xs)
Incrementing current from 2 to 3
Yielding 3
3
```

## Finite Generator

In our example, the generator goes on forever.
But what would happen in this case?

```python
def foo():
    yield 1
    yield "deux"
    yield "three"
```

Here, the function only `yield`s three values.

```python
>>> iterator = foo()
>>> next(iterator)
1

>>> next(iterator)
"deux"

>>> next(iterator)
"three"

>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

The fourth time `next` is called, there are no more `yield`s in the generator function.
This is seen as the end of the sequence, and `StopIteration` is raised to signal this.

## Summary

The central idea behind generator is that they are used to define a sequence of values.
We distinguish two facets: _defining_ a generator and _using_ a generator.

### Defining

A generator is a function that `yield`s each value of the sequence.

### Usage

Calling a generator function produces an iterator object.
We can use `next` repeatedly to retrieve each value of the sequence in turn.

## Task

Define a generator `repeat(value)` that generates an infinite repetition of the same `value`.

```python
>>> iterator = repeat(5)
>>> next(iterator)
5

>>> next(iterator)
5

>>> next(iterator)
5

>>> next(iterator)
5
```
# Cycle Revisited

Write a generator function `cycle(xs)` that repeats the elements from `xs` endlessly.

```python
>>> xs = cycle('abcd')
>>> itertools.islice(xs, 10)  # Take 10 first elements
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
```
# Fizz Buzz

[Fizz Buzz](https://en.wikipedia.org/wiki/Fizz_buzz) is a classic problem that tends to pop up in interview questions.
The idea is very simple:

* Start with a list of strings representing numbers: `['1', '2', '3', '4', ...]`.
* If the number if divisible by 3, the string should be replaced by `'fizz'`.
* If the number is divisible by 5, replace it by `'buzz'`.
* If the number is divisible by both 3 and 5, it should become `'fizzbuzz'`.

The first few items of this list are therefore `['1', '2', 'fizz', '4', 'buzz', 'fizz', ...]`.

Write a generator function that produces an infinite list that follows the rules set out above.
# RLE

[Run Length Encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) is a very simple compression algorithm.
Say we have the string `'aaaaaaaabbbbbcccccccc'`.
It consists of

* 8 `a`'s
* 5 `b`'s
* 7 `c`'s

This sums up to 20 bytes.
We can rewrite this as `[('a', 8), ('b', 5), ('c' 7)]`, which amounts to 6 bytes of data.
(Admittedly we do make some simplifications, but we don't want to get into the gnarly technical details.)

Even though our rewritten form is much more compact, no information is lost: given only `[('a', 8), ('b', 5), ('c' 7)]`, we can reconstruct the original string exactly.

No compression algorithm is perfect though: there will always be inputs for which "compression" will actually _increase_ the size of your file.
In the case of RLE, this occurs when there are no runs of the same character.
If we apply RLE on `'abcde'`, we would get `[('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)]`, which is double the size of the original!
In other words, RLE only works well on very specific kinds of inputs, which is why it's not often used (fax machines do use it for example.)

## Tasks

Write a _generator_ function `rle_encode(data)` with the following specifications:

* The parameter `data` can be an iterable or an iterator.
  (This shouldn't add any extra complexity to your code.)
* `data` is a sequence of chars, i.e., strings of length 1.
* `rle_encode` should return an iterator that produces pairs `(char, count)` as explained above.

Write a _generator_ function `rle_decode(data)`:

* The parameter `data` can be an iterable or an iterator.
  (This shouldn't add any extra complexity to your code.)
* `data` is a sequence of pairs `(char, count)`.
* `rle_decode` should return an iterator that produces chars (strings of length one.)

`rle_decode(rle_encode(data))` should generate the same characters as in `data`.
# Generator Expressions

Previously, we discussed three kinds of comprehensions:

* List comprehensions: `[expr for x in xs]`.
* Set comprehensions: `{expr for x in xs}`.
* Dictionary comprehensions: `{key: value for x in xs}`.

There's one more kind of comprehension, namely the _generator expression_.
Its syntax is `(expr for x in xs)` and it produces the same items as `[expr for x in xs]`, except for the fact that instead of computing all elements immediately and storing them in memory, the generator expression returns an iterator that will produce the elements one by one.

## Usage

Previously, we discussed functions such as `min`, `max`, `sum`, `all`, `any`, etc.
Each of them are happy to receive an iterable (or an iterator).
Typically, you would pass them a list:

```python
lowest_weight = min([person.weight for person in people])

total_cost = sum([item.price for item in shopping_basket])

passed = all([student.grade(course) >= 10 for course in student.courses])
```

While this approach is certainly correct, it can be a bit inefficient:

* first of list is constructed in memory
* this list is passed to a function (`min`, `sum`, `all`)
* the list is thrown away

If `people`, `shopping_basket` or `student.courses` contain many elements, a lot of memory could have been allocated.
Using iterators, however, would avoid this overhead: only one element at a time needs to reside in memory:
Such iterators can be constructed using generator comprehensions:

```python
lowest_weight = min((person.weight for person in people))

total_cost = sum((item.price for item in shopping_basket))

passed = all((student.grade(course) >= 10 for course in student.courses))
```

Python allows you to omit the comprehensions parentheses in such cases:

```python
lowest_weight = min(person.weight for person in people)

total_cost = sum(item.price for item in shopping_basket)

passed = all(student.grade(course) >= 10 for course in student.courses)
```

## Tasks

* Define a function `is_prime(n)` that checks if `n` is a prime number.
* Define a function `primes()` that returns an iterator of all primes.

```python
>>> is_prime(5)
True

>>> is_prime(6)
False

>>> ps = primes()
>>> next(ps)
2

>>> next(ps)
3

>>> next(ps)
5

>>> next(ps)
7
```
# Pairwise

The [`itertools`](https://docs.python.org/3/library/itertools.html) module contains many iterator-centric functionality.
One of the functions in this module is [`pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise).

```python
>>> from itertools import pairwise
>>> list(pairwise(range(5)))
[(0, 1), (1, 2), (2, 3), (3, 4)]
```

Rely on it to solve the exercise below.

## Task

Say that you have a map with several cities.
To keep things simple, the cities are simply numbered: `0`, `1`, `2`, etc.

There is a road between every two cities.
You can query the distance between two cities `a` and `b` using `distance(a, b)`.

A _path_ is a sequence of cities, for example, `[0, 5, 3, 4]`.
The total distance of a path is the sum of all the lengths of the roads between the cities: `distance(0, 5) + distance(5, 3) + distance(3, 4)`.

We ask of you to write a function `total_distance(path, distance)` which computes the total distance of `path`.

* The `path` parameter is an iterator of cities.
* The `distance` parameter is a function that you can use to determine the distance between two cities.
# Traveling Salesman Problem

The [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP) is a well known problem in the world of computer science.
The problem goes as follows: you are given a list of cities and the distances between them.
You are a traveling salesman starting in some given city.
You must then find the shortest tour that visits every city exactly once and then returns back to your starting city.

There is no known efficient algorithm to solve this problem: you can simply generate every possible path, compute its total distance, and return the path with the smallest total distance.

## Task

Write a function `find_shortest_path(distance, city_count)`:

* `distance` is a function that you can use to determine the distance between to cities.
  For example, `distance(0, 1)` returns the distance between cities `0` and `1`.
* `city_count` is the number of cities.
  The city numbers are `0`, `1`, ..., `city_count-1`.
* `find_shortest_path` should return a list of city indices representing the shortest possible tour.
  The path should always start and end in city `0`.

For example, say `city_count` is 4.
The possible tours are

* `[0, 1, 2, 3, 0]`
* `[0, 1, 3, 2, 0]`
* `[0, 2, 1, 3, 0]`
* `[0, 2, 3, 1, 0]`
* `[0, 3, 1, 2, 0]`
* `[0, 3, 2, 1, 0]`

Use `distance` to compute the total distance of each tour, and return the tour with the smallest total distance.

**Hint** Look for a useful function in [`itertools`](https://docs.python.org/3/library/itertools.html).
# RLE Revisited

Using [`itertools`](https://docs.python.org/3/library/itertools.html) and generator comprehensions you can write a much simpler solution for RLE.

Rewrite `rle_encode` and `rle_decode`.
# Testing

When writing code, correctness should always be your primary concern.
Your code can be efficient, modular and elegant, but if it doesn't produce the right results, it's of little use to anyone.

Since correctness is so important, there are many tools that aid you in achieving it:

* Static typing
* Verification tools
* Assertions
* Correctness proofs
* Writing tests

Each of these approaches has its own strengths and weaknesses.
Combining them is often possible ([Swiss cheese model](https://en.wikipedia.org/wiki/Swiss_cheese_model)), allowing us to combine strengths and avoid weaknesses.
In this series of exercises we will focus on writing tests and assertions, as these methods are prevalent in the industry (together with static typing, but that's for another time.)

## Good Tests

How does one write _good_ tests?
What can make a test good anyway?
What would be the difference with a bad test?

There are many different opinions of how to write tests.
Many different approaches exist, and each approach has their zealots that claim that their approach is the best.

We won't advocate a specific approach here.
Instead, we will ask ourselves the question, what makes a good test?
What qualities should it have?
Once we know how that, we will be able to judge whether tests are well written and how to improve them if needed.

### Automation

Some people, when writing code, like to perform quick manual tests:

```python
def some_function(x):
    # ...

print(some_function(5))
print(some_function(77))
```

They run the code and see if the right values are being outputted.
If so, the `print`s are removed and their attention turns to the next function/class/...

This is a _horrible_ approach to testing.
Don't do it.

If you're going to write testing code, you might as well not remove it, because that actually requires extra effort.
Simply group your testing code in a separate file, and keep it there, ready to be run.

People who remove tests assume that

* their tests are exhaustive and that they've just shown their code is 100% bug free, so no need to ever test it again; and
* their code will never need to be modified in any way (e.g., an optimization, an extra optional parameter, etc.)

Those assumptions are more often than not wrong.
So keep your tests.

Another major weakness of the example above is that it requires manual checking: `some_function`'s return values are printed out but need to be checked each time.
Instead, include the expected value in the tests:

```python
assert some_function(5) == 100
assert some_function(77) == 678
```

This way, it becomes the machine's job to perform the checking.

In short, you want to be able to simply run the tests and get a 100% pass rate.
Testing should require no more work from you than that.

### Fine Grained Tests

An airplane is a complex piece of machinery.
In the cockpit, there's plenty of little screens and lights giving the pilots feedback on the airplane's current status.
When something goes wrong, it is crucial that pilots are made aware of the problem as quickly as possible: typically something will light up, probably also make some buzzing sound to attract attention.
Not only that, the pilot also needs to know _where_ the issue is located: are they low on kerosene?
Has the front fallen off?
Is there a gremlin on the wings?
By knowing what exactly is wrong, the pilot can take immediate action to rectify the situation, like... flying to the nearest kerosene station.
(The writer is not a trained pilot, he's doing the best he can, okay?)

Similarly, a piece of code often often has many ways to go wrong.
Running the tests should give us a clear overview of what went wrong, but also of what went right.
The more precise this overview, the easier it will be to identify the culprit.

A test should ideally only be able to fail for only one reason.
If a single test can fail for ten different reasons, then there's ten different things to investigate if that test fails.
Our goal will be to keep the "reasons for failure" of every test as low as possible, so that if a test fails, we know exactly where to look for the responsible code.

### Readable Tests

When a test fails, you'll want to be able what exactly was being tested:

* If objects are involved, what state were they in?
* What action was performed?
* What was the expected result and what was the actual result?

### Fast Running Tests

In practice, tests are run quite often:

* As will be explained in the section about regression testing, tests are run after every little code change.
* Tests can also be run live, i.e., continuously in the background as you write code.
* The development process is also often set up (using [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) or [GitHub actions](https://github.com/features/actions)) to automatically run tests before allowing you to commit your changes to the master/main branch.

Depending on the project, there can also be _many_ tests to run.
In other words, you want the tests to run fast.

### Isolated Tests

Tests should always be run in isolation.
By this we mean that tests should not be able to affect each other's results.
The order in which the tests are run should not matter, and tests should be able to be run in parallel without affecting the outcome.


## Pytest

Pytest is the testing framework we rely on in this course.
We briefly explain what it does, exactly.

As you know, running `pytest` will cause the tests defined in `tests.py` to be run.
We [configured](https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-python_files) it that way: if you look at `pytest.ini` in your repository's root directory, you'll find

```text
python_files =
    tests.py
    *_tests.py
```

which tells Pytest which files to search for tests.

Inside these files, Pytest collects all functions that start with `test`.
This is the [default setting](https://docs.pytest.org/en/7.1.x/reference/reference.html#confval-python_functions).

Each test function is run.
A test function that returns normally (i.e., no exception) is considered to have passed.
Therefore, in order to tell Pytest a test failed, you need to throw an exception.

While you can throw an assertion manually, we strongly suggest to rely on `assert`:

```python
def test_something():
    assert condition
```

If `condition` evaluates to a falsey value, an `AssertionError` will be thrown.

If you rely on `assert`, Pytest will be able to recognize the checks and rewrite your code slightly to allow for better feedback.
For example, compare these two tests:

```python
def test_1():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    assert expected == actual


def test_2():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    if actual != expected:
        raise AssertionError()
```

Running the tests produces the following feedback:

```bash
$ pytest
FF                                                   [100%]
===================== FAILURES ============================
______________________ test_1 _____________________________

    def test_1():
        actual = [1, 2, 3]
        expected = [1, 2, 4]
>       assert expected == actual
E       assert [1, 2, 4] == [1, 2, 3]
E         At index 2 diff: 4 != 3
E         Use -v to get more diff

tests.py:4: AssertionError
______________________ test_2 _____________________________
    def test_2():
        actual = [1, 2, 3]
        expected = [1, 2, 4]
        if actual != expected:
>           raise AssertionError()
E           AssertionError

tests.py:11: AssertionError
============== short test summary info =====================
FAILED tests.py::test_1 - assert [1, 2, 4] == [1, 2, 3]
FAILED tests.py::test_2 - AssertionError
2 failed in 0.09s
```

As you can see, `test_1` provides useful information: it shows you the values of `actual` and `expected`.
Pytest even points out how exactly they differ: in our case, the elements with index 2 are unequal.

We'll discuss more of its capabilities as we progress.

## Task

Say we need to write a function `overlapping_intervals(interval1, interval2)` that checks whether the given intervals overlap.
We represent intervals using pairs.
The interval represented by the tuple `(left, right)` contains all values `x` for which `left <= x <= right`.
For example, the intervals `(2, 5)` and `(3, 8)` do overlap: they have `2` and `3` in common.
Conversely, `(0, 4)` and `(6, 9)` do not overlap.
Note that `(0, 4)` and `(4, 0)` do not overlap: the second interval is empty since there exist no `x` for which `4 <= x <= 0`.

Let's implement this function.
Create a file `ìntervals.py` and copy the code below into that file:

```python
def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if one of interval2's bounds fall inside interval1
    return left1 <= left2 <= right1 or left1 <= right2 <= right1
```

This is a nontrivial function, so we better test it.
Create a file `tests.py` and copy this test into that file:

```python
from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
```

Run the tests using `pytest` as usual.
They should pass.

However, `overlapping_intervals`'s implementation is actually faulty: the tests are incomplete.
Your task is

* Add more `assert`s to the test.
  Try to think of as many cases as you can.
  Make sure to check cases where the expected result is `True` and cases where the expected result is `False`.
* Try to understand what's wrong with `overlapping_intervals`'s implementation.
* Fix `overlapping_intervals`.
* Run your own tests again and make sure they pass.
  If not, go back to fixing `overlapping_intervals`.
* Run our tests by using `pytest -x verify.py`.
  If these don't all pass, go back to step 1.

> You should always commit all files you were tasked to update.
> In the past, this was limited to `student.py`, but now you should add `intervals.py` and `tests.py`.
# Parametrized Tests

In the previous exercise, we instructed you to write tests for a function `overlapping_intervals` as a series of `assert`s in a test function:

```python
def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    # ...
```

We previously mentioned how a test should ideally only be able to fail for one single reason.
Here however, we bundled multiple `assert`s in one test, each of which can be a reason for failure.

Imagine we have ten such `assert`s in a single test.
If the first `assert` were to fail, it would throw an exception, causing the test to  be interrupted and the remaining `assert`s to get skipped.
This throws away potentially valuable information: it might be interesting to whether the other checks pass or fail.

We can easily remedy this by putting each `assert` in its own test:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

## Improving Reporting

`pytest` generates a summary after having run all tests.
It gives you a nice overview of which tests have failed.
Let's run the tests with a faulty implementation of `overlapping_intervals`:

```python
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - assert False
FAILED tests.py::test_overlapping_intervals2 - assert not True
```

As you can see, the summary is not very useful.
Some people might suggest we give the tests better names:

```python
def test_overlapping_intervals_1_5_overlaps_with_3_6():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals_2_5_does_not_overlap_with_7_10():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

This way, when running the tests, you get a better overview of what failed:

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals_1_5_overlaps_with_3_6 - assert False
FAILED tests.py::test_overlapping_intervals_2_5_does_not_overlap_with_7_10 - assert not True
```

There are some downsides to this approach though:

* Python (like most other languages) imposes many restrictions on how we can name our functions.
  For example, a test named `test that interval (1, 5) overlaps with interval (3, 6)` would be more readable, but it's disallowed due to it containing spaces, parentheses and commas.
* We add redundancy: both the test and the test's name contain the same information about the intervals' bounds.
* It prevents us from parameterizing our tests (see later.)

A better approach would be to equip the `assert` with an error message:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6)), "Interval (1, 5) overlaps with interval (3, 6)"

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10)), "Interval (2, 5) does not overlap with interval (7, 10)"
```

Running the tests then gives

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - AssertionError: Interval (1, 5) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals2 - AssertionError: Interval (2, 5) does not overlap with interval (7, 10)
```

This has not rid us from redundancy though.
Fortunately, this is easily fixed:

```python
def test_overlapping_intervals1():
    interval1 = (1, 5)
    interval2 = (3, 6)
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"

def test_overlapping_intervals2():
    interval1 = (2, 5)
    interval2 = (7, 10)
    assert not overlapping_intervals(interval1, interval2), f"Interval {interval1} does not overlap with interval {interval2}"
```

## `@Parametrize`

Writing tests certainly seem to involve a lot of copy pasting: the tests shown above are near identical.
We would like to make the tests more compact.
Ideally, we would like to only have to write down what's essential to every test case and not have any kind of boilerplate code.

Pytest allows us to _parametrize_ tests.
Let's do this step by step.

First, notice the two local variables `interval1` and `interval2` we introduced to avoid redundancy.
Let's turn these into parameters:

```python
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

Okay, the test has halved in size, but how does the test know what values to use for `interval1` and `interval2`?
We can reintroduce these as follows:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

The `parametrize` decorator takes two parameters:

* The first is a string with the parameter names.
  These _must_ be the same as the test function's parameters.
  It will become clear later why this is necessary.
* The second is a list of tuples of values to be assigned to the parameters.
  In the example, we tell Pytest to assign `(1, 5)` to `interval1` and `(3, 6)` to `interval2`.

We are not restricted to only one tuple of values:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"
```

This generates five tests for you.
Running `pytest` produces

```bash
$ pytest
[left out detailed reports]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1[interval10-interval20] - AssertionError: Interval (1, 5) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval11-interval21] - AssertionError: Interval (1, 5) overlaps with interval (5, 6)
FAILED tests.py::test_overlapping_intervals1[interval12-interval22] - AssertionError: Interval (1, 10) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval13-interval23] - AssertionError: Interval (6, 8) overlaps with interval (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval14-interval24] - AssertionError: Interval (5, 7) overlaps with interval (4, 8)
```

Let's have two parametrized tests: one for overlapping intervals, one for nonoverlapping intervals:

```python
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"Interval {interval1} overlaps with interval {interval2}"


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 2), (3, 4)),
    ((1, 5), (5, 1)),
    ((8, 9), (6, 7)),
    ((8, 9), (6, 7)),
])
def test_nonoverlapping_intervals(interval1, interval2):
    assert not overlapping_intervals(interval1, interval2), f"Interval {interval1} does not overlap with interval {interval2}"
```

## Task

Copy the contents of `starter.py` to `parentheses.py`.
The function `matching_parentheses(string)` receives a string containing only parentheses (`'('` and `')'`).
It checks that all parentheses are matched, i.e., that every `(` has a matching `)`.

* Write two parametrized test functions in `tests.py`: one for cases where `True` should be returned, and one for `False`.
  Rely on `@parametrize` to specify inputs.
* Run your tests.
  They should fail as `matching_parentheses` contains bugs.
* Fix `matching_parentheses` in `parentheses.py`.
* Run your tests (`$ pytest`).
* Run our tests (`$ pytest verify.py`).
  If those fail, go back to step 1.
# Approx

In a file `mystatistics.py`, write a function `average(ns)` that given a list `ns` of numbers, computes the average.
The average equals the sum of `ns` divided by the length of `ns`.

In `tests.py`, write a parametrized test with two parameters: `ns` and `expected`.
Make sure to include the case `([0.1, 0.1, 0.1], 0.1)`.

Run your tests.
We expect them to fail.

## Floating Points

Real numbers can be infinitely long: think of &pi;, or even just 1/3 = 0.333333...
A machine can't afford to represent infinitely long numbers, so they cut them off after a certain number of digits.
However, this causes a loss of precision.

Say, for example, that a machine works in decimal and that it can only store 3 digits.
We expect 1 / 3 * 3 to be equal to 1.

If we divide 1 by 3, we should get 0.33333333... but it will be cut off after 3 digits: 0.333.
When we multiply this by 3, we get 0.999, which is not equal to 1.

These kinds of rounding errors happen all the time.
In applications involving many numerical computations (e.g., physics engines in games), it is crucial to take these errors into account.
There's even a [separate field of mathematics](https://en.wikipedia.org/wiki/Numerical_analysis) that specializes in finding ways of keeping the impact of rounding errors to a minimum.

A computer works in binary.
Values that seem okay in decimal (such as `0.1`) cannot be represented exactly in binary.
For example,

```python
>>> sum([0.1] * 10)
0.9999999999999999

>>> sum([0.1] * 10) == 1
False

>>> 1 - sum([0.1] * 10)
1.1102230246251565e-16
```

So, if we are to write tests involving floating point numbers, we have to take into account that the results might be a bit off.
Luckily, this is easy to solve.
If we expect a specific value `expected` and have a certain result `actual`:

```python
# Troublesome: we expect exact results
assert expected == actual

# Allows for an error margin
assert abs(expected - actual) < 0.0001
```

`abs(expected - actual) < 0.0001` expresses that `expected` and `actual` should be "more or less equal": we tolerate differences up to `0.0001`.

Pytest offers a [helper function](https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.approx) to make this even easier:

```python
from pytest import approx

assert approx(expected) == actual
```

If needed, you can specify a custom tolerance:

```python
assert approx(expected, abs=0.1) == actual
```

Here we allow for a large margin of error: `expected` and `actual` can differ up to `0.1`.
This might come in handy for tests, where we are typically not interested in specifying values of up to 7 digits:

```python
# Urgh, so many digits
assert approx(3.14159265) == pi

# Good enough for our purposes
assert approx(3.14, abs=0.01) == pi
```

Now, rely on `approx` to make your tests pass.
Go for a precision of `abs=0.01`.
# Exceptions

When calling a function with invalid arguments, the function will raise an exception.
This aspect of its behavior should also be tested.

## Book

In `book.py`, write a class `Book` with two readonly properties: `title` and `isbn`.
The following rules must be enforced:

* `title` must not be empty.
* `isbn` must be a valid ISBN number (see below)

If either of the arguments is invalid, a `RuntimeError` must be thrown.


Usage example:

```python
# Valid Book creation
>>> book = Book('Watchmen', '978-1779501127')

# Invalid title
>>> book = Book('', '978-1779501127')
RuntimeError

# Invalid ISBN
>>> book = Book('Watchmen', '978-1779501128')
RuntimeError
```

### ISBN Validity

The ISBN of a book consists of 13 digits, which can be separated by spaces or dashes (`-`).
Additionally, in order to detect mistakes, the last digit acts as a checksum.

The checksum algorithm goes as follows:

* Let's say we store the digits in an array `digits`.
  This array has length 13.
* Multiply the odd-indexed digits by 3.
* Take the sum of `digits`.
* This sum must be divisible by 10.

For example, consider the valid ISBN `978-1779501127`.
The `digits` array is `[9, 7, 8, 1, 7, 7, 9, 5, 0, 1, 1, 2, 7]`.
Multiplying the odd-indexed digits yields `[9, 21, 8, 3, 7, 21, 9, 15, 0, 3, 1, 6, 7]`.
The sum is `9 + 21 + 8 + 3 + 7 + 21 + 9 + 15 + 0 + 3 + 1 + 6 + 7 = 110`
This number is divisible by 10, meaning the ISBN is valid.

## Testing

In `tests.py`, write three parametrized tests:

* `test_valid_creation` that create books with valid `title` and `isbn`.
* `test_creation_with_invalid_title` that create books with an invalid `title`.
* `test_creation_with_invalid_isbn` that create books with an invalid `isbn`.

But how does one assert that an exception is thrown?
Pytest offers the following construct:

```python
import pytest


def test_raises_exception():
    with pytest.raises(ExceptionClass):
        # code that should throw an ExceptionClass
```

Keep the code inside the `with` block to a minimum.
The more code there is, the more potential sources of exceptions there are.
You want to make sure it's the right function that raises the exception.

In order to write the tests, you'll need both valid and invalid ISBNs.

* You can easily find valid ISBNs online.
* Modifying a single digit of a valid ISBN gives an invalid ISBN.
* Having more or less than 13 digits also invalidates an ISBN.

Make sure that you check all possible ways that an ISBN can be invalid.
For example, if you only check for exceptions using ISBNs with 14 digits, then you don't know if an exception will be thrown if an ISBN with a faulty checksum is used.

You can check your work using our own tests:

```bash
$ pytest verify.py
```
# Verification

Tests typically have the form "if I give this input, then I expect this output".
This basically means that you are actually first solving the problem yourself and then expect the algorithm to agree with you.
Solving the problem yourself is not necessarily easy, so you will limit yourself to simple cases where manual solving requires little effort from your part.
This can be a bit risky: maybe your algorithm contains a bug that only shows up in more complex cases.
In this case, your tests will not catch this bug.

But maybe there are ways to avoid having to solve the problem yourself.

## Turning Things Around

Consider a function that computes the square root of a number.
Of course, you can simply use `x**0.5`, but let's pretend for the moment we're working on a platform that does not have a built-in square root operation.
We could write tests as follows:

```python
@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (4, 2),
    (9, 3),
    (16, 4),
    (100, 10),
    (2, 1.41421356),
    (5785, 76.059187)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

However, we can easily generate this data.
We may not have `sqrt` built-in, but surely we have multiplication.
We could start off with the expected value (say `7`), square it (`49`) and then specify that `sqrt(49)` should return `7`.

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in [1, 2, 3, 4, 10, 1.41421356, 76.059187]
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

We can make easily increase the number of inputs:

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in range(1000)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

Now we only consider integers.
We add some extra computation to it so as to also test using floating point numbers.
In the code below we picked `0.73` at random.

```python
@pytest.mark.parametrize('n, expected', [
    (x * x, x) for x in (x * 0.73 for x in range(1000))
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(expected) == actual
```

> You might wonder why we don't actually generate random numbers using the `random` class?
> You should never have any randomness to your tests: tests need to be reproducible.
> Once you have a failing test, you need to be able to rerun that exact same test.
> You don't want to allow it to spontaneously disappear.

## Slow Solving, Fast Verification

Some problems are hard to solve, but easy to verify.
This is the case with our square root example: we can easily check the result of `sqrt(x)` by squaring it and comparing it to `x`:

```python
@pytest.mark.parametrize('n', [
    n for n in range(1000)
])
def test_sqrt(n, expected):
    actual = sqrt(n)
    assert approx(actual * actual) == n
```

Again we can generate many tests without having to do much work.

## Tasks

Let's implement our own sorting function: you'll implement an algorithm known as [merge sort](https://en.wikipedia.org/wiki/Merge_sort).
It involves three steps.

### `split_in_two`

First, we'll need a function `split_in_two(ns)` that splits a list `ns` halfway.

```python
>>> split_in_two([1, 2, 3, 4, 5, 6])
([1, 2, 3], [4, 5, 6])
```

If the input list has an odd number of elements, one of the halves will have to contain one more element than the other half.
You are free to choose with half.
Implement this function in `mergesort.py`.

In `tests.py`, write a parametrized test function `test_split_in_two`:

* `test_split_in_two` should have one parameter, namely the list to be split.
* Use `@parametrized` to pass it lists whose length range from 0 to, say, 100.
* These input lists should contain distinct elements.
  For example, say your implementation of `split_in_two` contains a bug and splits `[a, b, c, d]` into `([a, b], [a, b])`.
  If your test uses `[0, 0, 0, 0]` as input, you'll get back (`[0, 0], [0, 0]`), which is correct.
  The bug remained unnoticed.
  However, if instead you use `[0, 1, 2, 3]`, then the bug will become apparent as you'll get `([0, 1], [0, 1])` instead of `([0, 1], [2, 3])`.
* Please don't hardcode a hundred lists.
  It is trivial to generate a hundred lists with distinct elements.
* Don't hardcode expected results either.
  Instead, have the test check two things:
  * If `split_in_two(ns)` returns `(left, right)`, then `left + right` should be equal to `ns`.
  * `left` and `right`'s lengths should differ maximally by one.

### `merge_sorted`

`merge_sorted(left, right)` expects two parameters.
Both `left` and `right` are guaranteed to be _sorted_ lists.
`merge_sorted` must efficiently combine the two lists into one big sorted list:

```text
# Pseudocode
# Warning: might be incomplete!
result = []
i = points to start of left
j = points to start of right

while i has not reached end of left and j has not reached end of right
    if left[i] < right[j]:
        add left[i] to result
        move i one position to the right
    else:
        add right[j] to result
        move j one position to the right
```

Elements are added one by one to `result`.
At each step, we need to determine which is the next element to add.
Since `result` itself must be sorted, we must find the next smallest element.
Since `left` and `right` are sorted, we know that we can find the smallest element at the start of each list.
We compare `left[0]` with `right[0]`.
Say `left[0]` is the smaller of the two values, we then copy that value to `result`.
We also need to remember that in the following iteration, we need to look at `left[1]` instead of `left[0]`.

Implement `merge_sorted` based on the explanation above.
Write a parametrized test `test_merge_sorted`.
The test should have two parameters: `left` and `right`.
You can use multiple `@parametrize` decorators:

```python
@pytest.mark.parametrize('left', [
    [],
    [1],
    # ...
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    # ...
])
def test_merge_sorted(left, right):
    # ...
```

Pytest will then call `test_merge_sorted` with all possible combinations of values for `left` and `right`.

* You can hardcode values for `left` and `right`.
* Remember to only specify _sorted_ lists.
* Try to think of special cases:
  * The empty list.
  * A list with gaps in it (e.g. `[4, 10, 15]`.)
  * A list containing the same value more than once (e.g. `[2, 5, 5, 9]`).
* Specify at least 5 possible values for both `left` and `right`, so that it total there are at least 25 combinations in total.

Have the test check the result by asserting that `test_merge_sorted(left, right) == sorted(left + right)`.

> If you're wondering why not simply use `sorted(left + right)` as implementation for `test_merge_sorted`: you could, but it wouldn't work as fast.
  Here we are actually comparing results of a slow algorithm with that of a fast algorithm.
  This idea will be revisited in a later exercise.

### `merge_sort`

`merge_sort(ns)` receives a list and returns the same list, but with its elements sorted.
It does not modify `ns` in any way.

It works as follows:

* It splits `ns` in two, say `left` and `right`.
* It recursively sorts `left` and `right`.
  Let's call the results `sorted_left` and `sorted_right`.
* `sorted_left` and `sorted_right` are merged using `merge_sorted_lists`.

As always with recursion, you also need to know when to stop.
Ask yourself the question which cases are trivially solved.
Hint: what should happen if `merge_sort` receives the empty list?

Implement `merge_sort` as described above.
Write a parametrized test named `test_merge_sort`.
The test function should have two parameters:

* `expected`, a sorted list.
* `ns`, an unsorted permutation of `expected`, i.e., it contains the same elements but not necessarily in the same order.

Use `@parametrized` to feed it pairs of `expected` and `ns`:

* Start by manually picking an arbitrary sorted list.
  This will be used as value for `expected`.
* Use `itertools.permutations` to generate all permutations.
  These will be used as values for `ns`.

For example, you can pick `[1, 2, 3]` as `expected`.
Then, rely on `itertools.permutations` to generate `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]` and `[3, 2, 1]`.
`@parametrized` can then be used to have `test_merge_sort` called six times:

```python
test_merge_sort(expected=[1, 2, 3], ns=[1, 2, 3])
test_merge_sort(expected=[1, 2, 3], ns=[1, 3, 2])
test_merge_sort(expected=[1, 2, 3], ns=[2, 1, 3])
test_merge_sort(expected=[1, 2, 3], ns=[2, 3, 1])
test_merge_sort(expected=[1, 2, 3], ns=[3, 1, 2])
test_merge_sort(expected=[1, 2, 3], ns=[3, 2, 1])
```

Use multiple sorted starting lists: use the empty list, a list with the same element occurring more than once, etc.
For each of these lists, generate all permutations and feed them to `test_merge_sort`.
Make sure not to make these lists too long as otherwise the number of permutations will grow too large.
Six elements should be a good maximum length.

The test will be trivial to implement: it receives `expected` and `ns`, so it only needs to sort `ns` using `merge_sort` and compare the result to `expected`.

### Final Step

Run our tests to thoroughly check that your functions are implemented correctly.

```bash
$ pytest -x verify.py
```
# Reference Implementation

In a past exercise, we asked you to write a function `merge_sorted(ks, ns)`.
The test looked a bit like this:

```python
@pytest.mark.parametrize(...)
def test_merge_sorted(ks, ns):
    assert merge_sorted(ks, ns) == sorted(ks + ns)
```

The merging functionality was essentially implemented twice:

* `merge_sorted` itself used a more efficient algorithm.
* `sorted(ks + ns)` is a simple but inefficient way to achieve the same.

This idea of having to implementations can come in handy when implementing complex algorithms.
Typically the same problem can be solved in many ways, either using simple but slow algorithms, or using more complex but fast algorithms.
In these circumstances, it can be useful to implement both a simple slow and and a complex fast algorithm and having the tests compare their results:

```python
@pytest.mark.parametrize(...)
def test_some_functionality(inputs):
    expected = simple_but_slow(inputs)
    actual = complex_but_fast(inputs)
    assert expected == actual
```

## Tasks

A `Student` is defined as

```python
class Student:
    def __init__(self, id):
        self.id = id
```

You are given a list of `Student` objects.
It is guaranteed that the `Student`s appear in order of increasing `id` and that all `Student`s have distinct `id`s.
Your job will be to write code that that returns the `Student` whose `id` equals a given `target_id`.
If no such `Student` exists, `None` should be returned.

You want the search to be as efficient as possible.
Below we explain two algorithms: a slow one (but trivial to implement) and a fast one (but trickier to implement.)
To solve this exercise, you'll need to complete these steps:

* Implement the slow algorithm (linear search).
* Implement the fast algorithm (binary search).
* Write tests that thoroughly check that both algorithms produce the same results.

### Linear Search

A linear search does not make use of the fact that the list is sorted by `id`.
It simply starts with the first `Student` and checks its `id`.
If it equals `target_id`, it has found the right `Student` object and returns it.
If not, the algorithm moves on to the next in line.
If the end of the list is reached without finding the student with `id == target_id`, then `None` is returned.

Write a function `linear_search(students, target_id)` that implements this algorithm.
Put this in the file named `search.py`.

### Binary Search

Say we play a game where we pick a number between 0 and 100 and you need to guess it in as few tries as possible.
After each guess, we tell you if our secret number is lower or higher than your guess.

In order to play optimally, your first guess should be 50.
If we say our number is higher, your next guess should be 75, etc.
In other words, you should always guess the halfway number.

Let's try to write this down more formally.
At the beginning of the game, you know that the number will lie between 0 and 100, i.e., in the interval `[0, 100]`.
Computing the middle gives 50, which is your next guess.
Our feedback is "Higher!".
This lets you shrink the interval to `[51, 100]`.
You again compute the middle, which gives 75 (we assume you round down).
If we answer "Lower!", you know that the new interval becomes `[51, 74]`.

Use this same principle to find the correct `Student` object:

* You'll need to keep track of an interval of indices.
  Initially, all indices from `0` to `len(students) - 1` are potential candidates.
  Simply use two variables (e.g., `left` and `right`) to keep track of the bounds of this interval.
* Compute the index in the middle of this interval.
* Look up the `Student` at this index and compare its `id` with `target_id`.
* If `id == target_id` your search is finished, otherwise you'll need to update either `left` or `right` to reflect the fact that the interval has been halved in two.

Implement this as `binary_search(students, target_id)`.
Also put this in the file named `search.py`.

## Testing

Now write a parametrized test in `tests.py`.
It should have two parameters: `students` and `target_id`.

Make sure to include as all special cases you can think of:

* No `Student` with `id == target_id` occurs in the list.
* The `Student` to be found is the first in the list.
* The `Student` to be found is the last in the list.
* The `Student` to be found is in the list, but neither the first or last.
* The `Student`s' `id`s can be consecutive or have gaps in them.
* The `Student` list is empty.
* `target_id` should simply range from a low id (lower than the minimum student id) to a high id (higher than the maximum student id).
# Tasklist

In this exercise, we'll have you write two classes that will be used as working example for the next few exercises.

We do not provide any way to validate your work, as you'll be writing your own tests later on.

## `Task`

In a file `tasks.py`, write a class `Task`.

* It has a readonly property `description` that is initialized using a constructor parameter.
* It has a readonly property `due_date` that is initialized using a constructor parameter.
* It has a settable field `finished` which is initially set to `False`.

To represent dates, we use the standard `date` class from the [`datetime` module](https://docs.python.org/3/library/datetime.html).

Example usage:

```python
>>> from datetime import date
>>> task = Task('bake birthday cake', date(2023, 10, 1))
>>> task.description
'bake birthday cake'

>>> task.due_date
datetime.date(2023, 10, 1)

>>> task.finished
False

>>> task.finished = True
>>> task.finished
True
```

## `TaskList`

A `TaskList` keeps track of a list of `Task`s.
It offers the following functionality:

* `TaskList()` creates an empty task list.
* `task_list.add_task(task)` adds a `Task` to the list.
  The `Task`'s `due_date` must be in the future.
  In case its `due_date` is in the past, a `RuntimeErrror` should be thrown.
* `len(task_list)` gives the number of tasks in the list.
* `task_list.finished_tasks` returns a list of all finished tasks, i.e., those tasks whose `task.finished` is `True`.
* `task_list.due_tasks` returns a list of all unfinished tasks, i.e., those tasks whose `task.finished` is `False`.
* `task_list.overdue_tasks` returns a list of all unfinished tasks whose `task.due_date` is in the past.

In order to implement the `overdue_tasks` property, you'll need the following `date` functionality:

* You can use `<` to compare dates. If `date1 < date2` evaluates to `True`, this means that `date1` takes place before `date2`.
* Getting today's date (i.e., the date at the time the code is executed) is done using `date.today()`.

Example usage:

```python
>>> from datetime import date, timedelta
>>> tasks = TaskList()
>>> len(tasks)
0

>>> tomorrow = date.today + timedelta(days=1)
>>> yesterday = date.today - timedelta(days=1)

# Adding task with due_date in past is forbidden
>>> task_in_past = Task('some description', yesterday)
>>> tasks.add_task(task_in_past)
RuntimeError

# Adding task with due_date in future works
>>> task = Task('some description', tomorrow)
>>> tasks.add_task(task)
>>> len(tasks)
1

>>> tasks.finished_tasks
[]

>>> tasks.due_tasks
[task]                 # not exactly what's shown, but we simplified for the sake of clarity

>>> tasks.overdue_tasks
[]

# Wait 2 days...

>>> tasks.finished_tasks
[]

>>> tasks.due_tasks
[task]

>>> tasks.overdue_tasks
[task]

>>> task.finished = True
>>> tasks.finished_tasks
[task]

>>> tasks.due_tasks
[]

>>> tasks.overdue_tasks
[]
```

Implement this class in the same file `tasks.py`.
# Dependency Injection

In the previous exercise, you implemented the classes `Task` and `TaskList`.
We now want to write some tests.
Let's focus on `TaskList`'s `overdue_date` functionality.
We expect the following behavior:

```python
from datetime import date, timedelta


def test_task_becomes_overdue():
    tomorrow = date.today + timedelta(days=1)
    task = Task('some description', tomorrow)
    tasks = TaskList()

    tasks.add_task(task)

    # Wait 2 days...

    assert [task] == tasks.overdue_tasks
```

Make sure you understand the code above:

* We first create a `Task` that's due tomorrow.
* At this time, the task is not considered to be overdue, as its `due_date` is still in the future.
* We wait two days (and don't do to complete the task).
* The `Task` becomes *overdue*: we're past its `due_date`.
  It should now appear in the `overdue_tasks` list.

The test shown above has a rather large flaw: it has to wait for two days in order for the `Task` to become overdue.
We really don't want to have to wait that long.
As mentioned earlier, tests should run *fast*.

We could of course choose to pick a better due date, one just one microsecond in the future.
There are two problems with this:

* We are working with the `date` class.
  This class does not know anything smaller than a day.
  We would have to use the `datetime` class which combines date and time of day.
* In other contexts, the time delay simply cannot be chosen.
  For example, a game's rules might state that building a certain unit takes a full minute.
  A test would then have to wait this full minute, which is still unacceptably long.

We could also actually change the date your computer is set on, quickly check `overdue_tasks` and then set the date back.
This would be a horrible idea though as all other software running on the machine might get very confused.
But allowing us to change date would be so very handy...

Your code for `TaskList` probably looks a bit like this:

```python
class TaskList:
    # ...

    @property
    def overdue_tasks(self):
        return [
            task for task in self.__tasks
            if not task.finished and task.due_date < date.today()
        ]
```

This code relies on `date.today()`.
This method directly returns the machine's date.
The only ways to influence what it returns is to actually wait, or to change your computer's date.
We can, however, introduce an _indirection_: what if we develop our _own_ `today()` method?

## `Calendar`

In `calendars.py`, write a new class `Calendar`.
It has a single property: `today`.
It returns today's date, i.e., `date.today()`.

Next, have `TaskList` receive a `Calendar` object at creation.
It stores this `Calendar` in a private field and relies on it wherever it needs today's date.

Example usage:

```python
>>> calendar = Calendar()
>>> calendar.today
# shows today's date
```

After these changes, everything should still work exactly as before.

## `CalendarStub`

Also in `calendars.py`, now write another class `CalendarStub`.

* To the outside world, it should work the same as `Calendar`, i.e., it should have a member named `today`.
* It gives the user complete control over the date returned by `today`.

Example usage:

```python
# The constructor allows picking our own date
>>> calendar = CalendarStub(date(2000, 1, 1))
>>> calendar.today
datetime.date(2000, 1, 1)

# We can change the date as we see fit
>>> calendar.today = date(2001, 1, 1)
>>> calendar.today
datetime.date(2001, 1, 1)
```

## Dependency Injection

Our original `TaskList` code directly used `date.today()` to determine the current date.
There was no way to "parametrize" this: the link between `TaskList` and `date.today()` was hardcoded.

[Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) is simply the idea that if a class depends on something, that this dependency shouldn't be hardcoded.
Instead, the dependency should be configurable, for example using constructor parameters.
We achieved this by introducing the calendar classes.

```python
>>> calendar = Calendar()
>>> task_list = TaskList(calendar)
```

This effectively states "`TaskList`, please use this `calendar` object to determine the current date".
Put differently, we were able to "inject" the dependency.
It makes code more modular, which increases reusability and testability.

We now have two calendars:

* `Calendar` will be used in production, that is, the code that ends up running on the end user's machine.
* `CalendarStub` will come in handy during testing as it allows us to easily set the date.

## Other Examples

There are many cases where dependency injection can be useful:

* Say you write a game involving dice and your code relies on [`random.randint()`](https://docs.python.org/3/library/random.html#random.randint) to generate random numbers between `1` and `6`.
  However, this makes testing arduous: you want to be able to simulate certain rolls, so the tests will start having to roll the dice until a certain outcome is reached.
  Instead, you can introduce `RandomDice` and `ControlledDice` classes where the former returns actual random values while the latter can be configured to return certain dice rolls.
* The built-in `print` and `input` should typically not be used directly as again you would be hardcoding the destination and source of your IO.
  What if the data should be received/sent on a network instead?
  Again, an intermediate object can help out here.
* When your application has external dependencies such as a database, being able to work with smaller fake in-memory databases can simplify testing a lot.

## Testing

In a separate file `tests.py`, write the test `test_task_becomes_overdue` that performs the same checks as the code shown at the top of this file.
Run the test and make sure it passes.
# Arrange Act Assert

Let's add some structure to our tests.
By following a convention, we will improve the readability and overall quality of our tests.

Let us take a look at a possible implementation for `test_task_becomes_overdue` from the previous exercise:

```python
def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)
    calendar.today = next_week
    assert [task] == task_list.overdue_tasks
```

We can distinguish three stages:

* **Arrange** The first stage gathers all necessary objects that will be necessary for the test.
* **Act** The second stage performs the operation whose consequences need to be checked.
* **Assert** The third stage checks that the operation has had the desired effects.

We can make these three stages more explicit:

```python
def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == task_list.overdue_tasks
```

It can also be useful to clearly identify which object it is we're testing.
In our case, `task_list` is at the center of attention: it is this object that we're testing the behavior of.
To make this explicit, we can adopt the convention of using the name `sut` which stands for *system under test*:

```python
def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks
```

Note that these conventions are just that: conventions.
They don't magically make your tests perfect, and it's not always possible or beneficial to follow them to the letter.

Remember that updating your code can make the tests unexpectedly fail.
You will need to inspect the failing tests to understand what exactly goes wrong, after which you can pinpoint the location in the code that contains a bug and fix it.
Adopting a consistent structure make tests easier to understand.

> In case you are wondering why we set `today` to `date(2000, 1, 1)` instead of `date.today()`: tests must be 100% deterministic and always check the same things every time they're run.
> Using `date.today()` would have the tests run on different values each day.
> If you want the tests to run for different values of `today`, you should use parametrized tests.

## Tasks

Add the following tests:

* `test_creation` creates a new `TaskList` and checks the initial values of `len(task_list)`, `due_tasks`, `overdue_tasks` and `finished_tasks`.
* `test_adding_task_with_due_day_in_future` adds a `Task` whose `due_date` is set in the future.
* `test_adding_task_with_due_day_in_past` adds a `Task` whose `due_date` is in the past.
  It should expect a `RuntimeError` to be thrown.
* `test_task_becomes_finished` adds a `Task`, then sets its `finished` member to `True`.
  The `Task` should have moved from `task_list.due_tasks` to `task_list.finished_tasks`.
# Setup

Take a look at the `tests.py` in the solutions folder of the *previous* exercise.
The Arrange sections have much in common:

* A `today` date is created.
* A new `CalendarStub` initialized on `today`.
* A `TaskList` is made in most.

We would like to factor out this common code.
One way to achieve this is to rely on the `setup_function` function.

When launced, Pytest will scan your `tests.py` for test functions (as configured in `pytest.ini`).
To determine whether a function is a test function, Pytest looks at the name: all functions whose name start with `test_` are identified as tests.
Pytest will then call each of these test functions in *some* order.

Now, Pytest also looks for a function named `setup_function`.
Before running a test, Pytest will call `setup_function`.
Similarly, you can also have a function named `teardown_function`.
This will be called *after* each test.

For example, say we have the following definitions in `tests.py`:

```python
def setup_function():
    # ...

def teardown_function():
    # ...

def test_1():
    # ...

def test_2():
    # ...

def test_3():
    # ...
```

Pytest will then call these functions in the following order:

* ``setup_function()``
* `test_1()`
* `teardown_function()`
* ``setup_function()``
* `test_2()`
* `teardown_function()`
* ``setup_function()``
* `test_3()`
* `teardown_function()`

The `setup_function` function can be used to gather all code common in all tests.
If you're wondering why `setup_function` is called before *each* test instead of just once: we want each test to start with fresh objects.
Nothing prevents a test from modifying these objects, meaning that a change made in `test_1` could affect the outcome of `test_2`.
This is something that must be avoided at all costs: remember the Test Isolation goal we set out for ourselves.

Conversely, `teardown_function` can be useful to perform clean up: delete files that were created by the tests, close database connections, etc.

## Implementing `setup_function`

As an example, we show how you can rely on `setup_function` to create the `today` date.

```python
def setup_function():
    global today
    today = date(2000, 1, 1)


def test_whatever():
    calendar = CalendarStub(today)
    # ...
```

Notice the `global` declaration in `setup_function`.
Without `global`, `today` would simply be a local variable and therefore not visible to `test_whatever`.

## Task

Clean up your own tests (or our own solution's tests if that's easier) by relying on `setup_function`.
Inside this `setup_function` function, create `today`, `tomorrow`, `yesterday`, `calendar` and `sut`.
Adapt your tests so as to make use of these shared variables.

Run the tests to make sure everything still works.
# Fixtures

We used `setup_function` to factor out common code.
However, it has some serious shortcomings.

> But why did we bother explaining `setup_function` instead of immediately offering the better solution?
> Well, other testing frameworks only provide the `setup_function` approach, and you might always encounter tests that still rely on `setup_function` in older code.

One weakness of the `setup_function` is that it can quickly become a place where all Arrange stages of the tests are combined.
Ideally, `setup_function` should only create objects needed by *all* tests, but this rule is too rigid to follow in practice:
Following the rule strictly would prevent you from writing tests that don't use *all* objects created by `setup_function`, which is silly.
So instead, the `setup_function` will grow and, in the worst case, end up being the union of all Arrange stages of the tests.

Having a large `setup_function` has two major disadvantages:

* The more a `setup_function` does, the more chance it has to fail.
  If a single line of code raises an exception, *none* of the tests will be able to run.
  This kind of chain reaction has to be avoided at all costs.
* It slows things down unnecessarily.

A better solution is to rely on Pytest's `@fixture` functionality:

```python
import pytest


@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)


def test_calendar_stuff(calendar):
    # do stuff with calendar
```

Here's how it works:

* Pytest identifies `test_calendar_stuff` as a test.
* It looks at the test function's parameter list and finds `calendar`.
  This is the test's way of saying "I require a `calendar` do perform my job."
* It looks for `@fixture`s with the same name.
* It finds the function `calendar` that has been tagged as a fixture.
  Just like with the test function, it uses parameters to convey what its dependencies are.
  `calednar` needs the fixture named `today`.
* Pytest will then look for a `@fixture` named `today`.
* It finds it, sees there are no parameters (hence no dependencies) and simply calls the function.
  This returns a `date` object.
* This `date` object is then passed as argument to the function `calendar`.
  This function uses it to create a new `CalendarStub`.
* Thhis `CalendarStub` is then passed to `test_calendar_stuff`, which can use it to perform some checks.

In short, tests (and fixtures) can declare their dependencies using parameters.
Pytest will then automatically call the corresponding `@fixture` and pass its return value as arguments.
A test/fixture can have as many dependencies it wants.

`@fixture`s solve the shortcomings mentioned above: only those fixtures that are mentioned in the parameter list will be created.
This will cause the tests to run faster, but most importantly, no tests will fail due to errors occurring in unrelated code.

## Task

Update the `TaskList` tests so as to use `@fixture` instead of `setup_function`.
Create fixture functions for

* `today`
* `tomorrow`
* `yesterday`
* `calendar`
* `sut`

Declare the necessary dependencies using parameters.
This includes both "test depends on fixture" and "fixture depends on other fixture".
# Factory Functions

Consider the following tests:

```python
@pytest.fixture
def task(tomorrow):
    return Task('xxx', tomorrow)

# more code

def test_task_creation(task, tomorrow):
    assert task.description == 'xxx'
    assert task.due_date == tomorrow
    assert task.finished == False
```

While `test_task_creation` passes and is quite to the point, it suffers from a lack of readability.
The problem is that the initial values for each member (`xxx`, `tomorrow` and `False`) have been chosen somewhere outside the test.
If the test fails, we'd have to look around our code to find out what the values actually should be.
In other words, the test isn't self contained.

## Descriptive Variable Names

We can alleviate this problem a bit by using a more descriptive variable name:

```python
@pytest.fixture
def unfinished_task_due_by_tomorrow(tomorrow):
    return Task('xxx', tomorrow)

# more code

def test_task_creation(unfinished_task_due_by_tomorrow, tomorrow):
    assert unfinished_task_due_by_tomorrow.due_date == tomorrow
    assert unfinished_task_due_by_tomorrow.finished == False
```

The test feels a lot less arbitrary now.
It's not just some "task", it's an *unfinished task due by tomorrow*!
Sadly, the description is still missing.
Should we change the name to `unfinished_task_due_by_tomorrow_described_as_xxx`?
It's obvious that this approach can become very impractical very quickly.

## Mutable Fixtures

Another issue arises when we start modifying our fixtures.

```python
@pytest.fixture
def unfinished_task(tomorrow):
    return Task('xxx', tomorrow)


def test_task_becomes_finished(sut, unfinished_task):
    # Arrange
    sut.add_task(unfinished_task)

    # Act
    unfinished_task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [unfinished_task] == sut.finished_tasks
```

The test receives an unfinished task, but then sets it to finished.
We end up with a variable `unfinished_task` that contains a finished `Task`.
The second `assert` does not make sense: it states that the list of finished tasks contains an unfinished task.
Such misleading names ought to be avoided at all costs.

On the one hand, the variable's name should convey all important information.
The test doesn't care about the task's description or its due date, but in order for the test to make sense it is crucial that the task be unfinished.
So, the rule above tells us that we should use the name `unfinished_task`.

On the other hand, a basic variable naming rule says to pick a name that, at all times, describes the value accurately.
We know we have a task, so the name should at least include the word `task`.
However, during its lifetime the task goes from unfinished to finished, meaning the name must remain vague enough and can't mention anything about its "finishedness".

Quite a dilemma we've got on our hands.

## Factory Functions

Factory functions are functions whose sole purpose is to create an object.
Here is how we can use them:

```python
def create_unfinished_task():
    return Task('xxx', date(2000, 1, 1))


def test_task_becomes_finished(sut):
    # Arrange
    task = create_unfinished_task()
    sut.add_task(unfinished_task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
```

This approach has the same advantages as `@fixture`: no unneeded objects are created.
It also solves the problem we described above:

* The factory function has an accurate and precise name:
  * It makes clear that the returned task is unfinished.
  * It doesn't convey any extra information that would be irrelevant to the test.
* The variable name at no point contradicts the variable's value.

## Flexible Factory Function

Different tests might need different kinds of tasks.
While it is possible to create distinct factory functions (`create_finished_task`, `create_unfinished_task`, `create_task_due_tomorrow`, etc.), a single parametrized factory function might be preferable:

```python
def create_task(*, description='default description', due_date=None, finished=False):
    due_date = due_date or date(2000, 1, 1)
    task = Task(description, due_date)
    if finished:
        task.finished = True
    return task


def test_task_becomes_finished(sut):
    # Arrange
    task = create_task(finished=True)
    sut.add_task(unfinished_task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
```

This factory function allows you to only mention the relevant properties for the `Task` to be created.
It automatically fills in with defaults for the other members.

> The `*` in `create_task`'s parameter list forces callers to use keyword arguments, i.e., `create_task('description')` is invalid, but `create_task(description='description')` is okay.

## Summary

We've discussed three ways of factoring out shared dependencies:

* `setup_function`
* `@fixture`
* Factory functions

`setup_function` is generally discouraged as it provides [no advantages](https://docs.pytest.org/en/7.3.x/explanation/fixtures.html#improvements-over-xunit-style-setup-teardown-functions) compared to the latter two approaches.
Whether to use `@fixture` or factory functions can be a matter of opinion.
Try to keep in mind what makes a good test and decide based on that.

We'd like to add that [pytest's fixtures](https://docs.pytest.org/en/7.3.x/explanation/fixtures.html#about-fixtures) have some extra functionality we didn't discuss:

* We can [parametrize](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#parametrizing-fixtures) fixtures so that they yield multiple values.
  A test requesting this fixture will be run multiple times, once for each of these values.
* Fixtures that provide resources that need to be cleaned up (e.g., database connections need closing, temporary files need to be deleted, ...) can easily specify [teardown](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#yield-fixtures-recommended) logic.
* [Smart caching](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#fixtures-can-be-requested-more-than-once-per-test-return-values-are-cached)
* [Scoping](https://docs.pytest.org/en/7.3.x/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session) to reuse fixtures across classes/modules/packages.

## Task

Replace the fixtures by factory functions.
Also make use of `create_task` for tests that need a `Task`.
# Assertions

You've been using `assert` to perform checks in your tests.
But what exactly does `assert` do?

```python
assert condition, message
```

can be translated

```python
if not condition:
    raise AssertionError(message)
```

No big surprises here.
However, there's slightly more to it than that.

## Debug vs Release Builds

The only language your processor understands is machine code.
However, writing machine code directly is *very* hard.
For this reason, we developed programming languages such as C, C++, Python, Ruby, C#, Java, JavaScript, etc.
Code written in these languages need to be translated into machine code.
Programs performing these translations are called [interpreters](https://en.wikipedia.org/wiki/Interpreter_(computing)) or [compilers](https://en.wikipedia.org/wiki/Compiler).
They do differ in the approach they take, but we won't go into detail here.
From now on, we'll use the word "compile" and "compiler" to mean "translate" and "translator program".

A common misconception is the belief that the compilation from programming language to machine code happens "literally", i.e., word-for-word translations, without changes.
In reality, compilers have a lot of freedom:

* They can eliminate [dead code](https://en.wikipedia.org/wiki/Dead_code), i.e., code that is never used.
* They can change the order of instructions as this can potentially make the program run faster.
  This can be as basic as swapping two statements but can be as advanced as modifying your loops.
  Of course, this only happens if the compiler can determine it does not change the observable behavior of the program.
* If your code evaluates the same expression twice, a compiler can choose to reuse to result of the first evaluation.
* Algorithms can be rewritten into a more efficient, behaviorally equivalent form.

The compiled form might barely bear any resemblance to your original code.
An advantage of this is that your program will run faster and consume less memory than if executed "literally".
A downside, however, is that it can make debugging much harder.
To find a bug, you might want to execute your code step by step using a debugger, but if all instructions have been reordered or even rewritten, this might not be possible anymore.

For this reason, we make the distinction between a debug build and a release build:

* In the debug build, no optimizations are made.
  The code is compiled in a very straightforward manner, and possibly extra metadata is added to assist you in debugging.
* In a release build, all optimizations are turned on and none of the debugging aids are present.
  This is the build the end user will receive.

For example, in a language like C++ the gap between debug and release build is huge.
In the debug build, plenty of checks are made so as to catch bugs quickly.
In the release build, no checks are made, as it is assumed the code is bug free.
As a result, the release build often runs 10 to 100 times faster.

In Python, the difference between debug and release build is much smaller, almost nonexistent even.
The most significant difference is how [`assert`s are executed](https://docs.python.org/3/reference/simple_stmts.html#assert): in release mode the `assert`s are ignored.

Say the following code is stored in `demo.py`:

```python
assert False, 'Failure!'
```

Running it gives

```bash
$ py demo.py
AssertionError: Assertion failure!
```

However, running it in release mode (called optimized mode in Python) gives

```bash
$ py -O demo.py
# Nothing happens
```

It is therefore crucial that you do not rely on `assert` for anything that actually impacts behavior.
`assert` is merely to be used as a debugging aid.
For the purposes of testing, using `assert` is of course safe: there's no reason to run tests is release build.

## When to Use `assert`

`assert` can be used in regular code, i.e., not testing code, to perform self-checks.
For example, the code for `max` could look as follows:

```python
def max(ns):
    result = ns[0]
    for n in ns:
        if n > result:
            result = n

    # Check that result is an element of the given list
    assert result in ns
    # Check that all values in the given list are not greater than result
    assert all(n <= result for n in ns)

    return result
```

Here's another example: the function `median` checks its result before returning it.
There could still be a bug in the algorithm despite the `assert` condition being true, but that's okay: partial checks are valuable too.

```python
def median(ns):
    sorted_ns = sorted(ns)
    if len(ns) % 2 == 0:
        right_of_center = len(ns) // 2
        left_of_center = right_of_center - 1
        result = (sorted_ns[left_of_center] + sorted_ns[right_of_center]) / 2
    else:
        center = len(ns) // 2
        result = sorted_ns[center]

    # Check that there are as many elements "below" result as there are elements "above" result
    assert sum(1 for n in ns if n <= result) == sum(1 for n in ns if n >= result)
    return result
```

## `assert` vs Tests

`assert`s in regular code perform plenty of checks as the program is running.
While they perform a job very similar as that of tests, they do *not* replace tests.
They're just an extra way of checking your code.

## Task

`starter.py` contains (correct) code for merge sort.
Copy it to `student.py`.
Add `assert`s where you can.
If an `assert` condition becomes complex, don't hesitate to define a separate function for it, which the `assert` can then call.
Compare it with our solution.
Make sure to understand what each `assert` checks.



**Alright, now you go ahead and extract all of the important theory from this long text, and add possibly a little bit of extra information and at the end a little cheatsheet I can use for my exam.**






