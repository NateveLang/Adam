# Adam

Adam is a Nateve Programming Language compiler developed using Python.

## Nateve

Nateve is a new general domain programming language open source inspired by languages like Python, C++, JavaScript, and Wolfram Mathematica.

Nateve is an compiled language. Its first compiler, Adam, is fully built using Python 3.8.

### Options of command line (Nateve)

1. `build`: Transpile Nateve source code to Python 3.8
2. `run`: Run Nateve source code
3. `compile`: Compile Nateve source code to an executable file (.exe)
4. `run-init-loop`: Run Nateve source code with an initial source and a loop source
5. `set-time-unit`: Set Adam time unit to seconds or miliseconds (default: milisecond)
6. `-v`: Activate verbose mode

## Nateve Tutorial

In this tutorial, we will learn how to use Nateve step by step.

### Step 1: Create a new Nateve project

```cmd
$ cd my-project
$ COPY CON main.nateve
```

#### Hello World program

```Nateve
print("Hello, World!")
```

#### Is prime? program

```Nateve
def is_prime(n) {
    if n == 1 {
        return False
    }
    for i in range(2, n) {
        if n % i == 0 {
            return False
        }
    }
    return True
}

n = intput("Enter a number: ")

if is_prime(n) {
    print("It is a prime number.")
}
else {
    print("It is not a prime number.")
}
```

### Comments

If you want to comment your code, you can use:

```Nateve
~ This is a single line comment ~

~
    And this a multiline comment
~
```

## Under construction...

### Let Statements

This language does not use variables. Instead of variables, you can only declare static values.

For declaring a value, you must use `let` and give it a value. For example:

``` sql
let a = 1        -- Interger
let b = 1.0      -- Float
let c = "string" -- String
let d = true     -- Boolean
let e = [1,2,3]  -- List
let f = (1,2)    -- Tuple
...             
```

SigmaF allows data type as Integer, Float, Boolean, and String.

### Lists

The Lists allow to use all the data types before mentioned, as well as lists and functions.

Also, they allow to get an item through the next notation:

``` sql
let value_list = [1,2,3,4,5,6,7,8,9]
value_list[0]       -- Output: 1
value_list[0, 4]    -- Output: [1,2,3,4]
value_list[0, 8, 2] -- Output: [1, 3, 5, 7]
```

> The struct of **List CAll** is `example_list[<Start>, <End>, <Jump>]`

### Tuples

The tuples are data structs of length greater than 1. Unlike lists, they allow the following operations:

``` sql
(1,2) + (3,4)      -- Output: (4,6)
(4,6,8) - (3,4,5)  -- Output: (1,2,3)
(0,1) == (0,1)     -- Output: true
(0,1) != (1,3)     -- Output: true
```

To obtain the values of a tuple, you must use the same notation of the list. But this data structure does not allow ranges like the lists (only you can get one position of a tuple).

E.g.

```Haskell
let t = (1,2,3,4,5,6)
t[1] -- Output: 2
t[5] -- Output: 6
```
And so on.

### Operators

> **Warning**: SigmaF have **Static Typing**, so it does not allow the operation between different data types.

These are operators:
| Operator             | Symbol |
|----------------------|--------|
| Plus                 |    +   |
| Minus                |    -   |
| Multiplication       |    *   |
| Division             |    /   |
| Modulus              |    %   |
| Exponential          |   **   |
| Equal                |   ==   |
| Not Equal            |   !=   |
| Less than            |    <   |
| Greater than         |    >   |
| Less or equal than   |   <=   |
| Greater or equal than |   >=   |
| And                  |   &&   |
| Or                   |  \|\|  |
<br/>

> The operator of negation for Boolean was not included. You can use the `not()` function in order to do this.

### Functions

For declaring a function, you have to use the next syntax:

``` Python
let example_function = fn <Name Argument>::<Argument Type> -> <Output Type> {
    => <Return Value>
}  
```

> (For return, you have to use the => symbol)

For example:

``` sql
let is_prime_number = fn x::int, i::int -> bool {
    if x <= 1 then {=> false;}
    if x == i then {=> true;}
    if (x % i) == 0 then {=> false;}
    => is_prime_number(x, i+1);
}

printLn(is_prime_number(11, 2)) -- Output: true
```

### Conditionals

Regarding the conditionals, the syntax structure is:

``` Python
if <Condition> then {
    <Consequence>
}
else{
    <Other Consequence>
}
```

For example:

``` Python
if x <= 1 || x % i == 0 then {
    false;
}
if x == i then {
    true;
}
else {
    false;
}
```

## Some Examples
``` sql
-- Quick Sort
let qsort = fn l::list -> list {

	if (l == []) then {=> [];}
	else {
		let p = l[0];
		let xs = tail(l);
		
		let c_lesser = fn q::int -> bool {=> (q < p)}
		let c_greater = fn q::int -> bool {=> (q >= p)}

		=> qsort(filter(c_lesser, xs)) + [p] + qsort(filter(c_greater, xs));
	}
}

-- Filter
let filter = fn c::function, l::list -> list {
	if (l == []) then {=> [];} 

    => if (c(l[0])) then {[l[0]]} else {[]} +  filter(c, tail(l));
}

-- Map
let map = fn f::function, l::list -> list {
	if (l==[]) then {=> [];}
	
	=> [f(l[0])] + map(f, tail(l));
}


```

To know other examples of the implementations, you can go to [e.g.](egs)

---
## Feedback
I would really appreciatte your feedback. You can submit a new issue, or reach out me on [Twitter](https://twitter.com/fabianmativeal).

# Contribute

This is an **opensource** project, everyone can contribute and become a member of the community of **SigmaF**.

## Why be a member of the SigmaF community?

### 1. A simple and understandable code

The source code of the interpreter is made with Python 3.8, a language easy to learn, also good practices are a priority for this project.

### 2. A great potencial

This project has a great potential to be the next programming language of the functional paradigm, to development the AI, and to development new metaheuristics.

### 3. Scalable development

One of the mains approaches of this project is the implementation of TDD from the beggining and the development of new features, which allows scalability.

### 4. Simple and power

One of the main purposes of this programming language is to create an easy-to-learn functional language, which at the same time is capable of processing large amounts of data safely and allows concurrence and parallelism.

### 5. Respect for diversity

Everybody is welcome, it does not matter your genre, experience or nationality. Anyone with enthusiasm can be part of this project. Anyone from the most expert to the that is beginning to learn about programming, marketing, design, or any career.

## How to start contributing?

There are multiply ways to contribute, since sharing this project, improving the brand of SigmaF, helping to solve the bugs or developing new features and making improves to the source code.

- **Share this project**: You can put your star in the repository, or talk about this project. You can use the hashtag #SigmaF in Twitter, LinkedIn or any social network too.
  
- **Improve the brand of SigmaF**: If you are a marketer, designer or writer, and you want to help, you are welcome. You can contact me on Twitter like @fabianmativeal if you are interested on doing it.
  
- **Help to solve the bugs**: if you find one bug notify me an issue. On this we can all improve this language.
  
- **Developing new features**: If you want to develop new features or making improvements to the project, you can do a fork to the `dev` branch (here are the ultimate develops) working there, and later do a [`pull request`](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to `dev` branch in order to update **SigmaF**.