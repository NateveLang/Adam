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

```python
print("Hello, World!")
```

#### Is prime? program

```python
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

n = ninput("Enter a number: ")

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

### Variables

This language uses variables. For declaring variables, you just need to write the name of the variable and the value of the variable.

For example:

```python
a = 1                          ~ Interger ~
b = 1.0                        ~ Float ~
c = 1 + 2j                     ~ Complex ~
d = "hello"                    ~ String ~
e = True                       ~ Boolean ~
f = [1,2,3]                    ~ List ~
g = (1,2)                      ~ Tuple ~
h = Vector([1,2,3])            ~ Vector ~
i = Polynomial("1 +2x +x^2")   ~ Polynomial ~
j = Matrix("""          
| 1 1 2 3 4 |
| 0 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
| 1 1 2 3 4 |
""")                           ~ Matrix ~
```

Nateve allows data type as Integer, Float, Complex, Boolean, String, List, Tuple, None, Vector, Polynomial and Matrix.

### Lists

The Lists allow to use all the data types before mentioned, as well as lists and functions.

Also, they allow to get an item through the next notation:

```python
value_list = [1,2,3,4,5,6,7,8,9]
value_list[0]       ~ Output: 1 ~
value_list[0 : 4]   ~ Output: [1,2,3,4] ~
```

> The struct of **List Call** is `example_list[<Start> : <End> + 1]`

### Functions

For declaring a function, you have to use the next syntax:

``` Python
def example_function(<argument1>, <argument2>, ...) {
    <sentence1>
    <sentence2>
    ...
    return <Return Value>
}  
```

### Conditionals

Regarding the conditionals, the syntax structure is:

``` Python
if <Condition> {
    <Consequence>
}
elif <Condition> {
    <Other Consequence>
}
...
else {
    <Default Consequence>
}
```

For example:

``` Python
if x <= 1 and x % 3 == 0 {
    a = 0
}
elif x == 9 {
    a = 1
}
else {
    a = 2
}
```

## Some Examples

```python
~ Quick Sort ~
def qsort(l) {
    if (l == []) {return []}
    else{
        pivot = l[0]
        less = qsort(l[1:].filter(lambda x: x < pivot))
        greater = qsort(l[1:].filter(lambda x: x >= pivot))
        return less + [pivot] + greater
    }
}
```

## Feedback

I would really appreciatte your feedback. You can submit a new issue.

## Contribute

This is an **opensource** project, everyone can contribute and become a member of the community of **Nateve**.

## Why be a member of the SigmaF community?

### 1. A simple and understandable code

The source code of Adam is made with Python 3.8, a language easy to learn, also good practices are a priority for this project.

### 2. A great potencial

This project has a great potential to be the next programming language for education, to develop the quantum computing, and to develop the AI.

### 3. Simple

One of the main purposes of this programming language is to create an easy-to-learn language, which at the same time is capable of being used for many different purposes.

### 4. Respect for diversity

Everybody is welcome, it does not matter your genre, experience or nationality. Anyone with enthusiasm can be part of this project. Anyone from the most expert to the that is beginning to learn about programming, marketing, design, or any career.

## How to start contributing?

There are multiply ways to contribute, since sharing this project, improving the brand of SigmaF, helping to solve the bugs or developing new features and making improves to the source code.

- **Share this project**: You can put your star in the repository, use the topic [nateve](https://github.com/topics/nateve) or talk about this project. You can use the hashtag #Nateve in Twitter, LinkedIn or any social network too.
  
- **Improve the brand of Nateve**: If you are a marketer, designer or writer, and you want to help, you are welcome.
  
- **Help to solve the bugs**: if you find one bug notify us an issue. On this we can all improve this language.
  
- **Developing new features**: If you want to develop new features or making improvements to the project, you can do a fork to the `dev` branch (here are the ultimate develops) working there, and later do a [`pull request`](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to `dev` branch in order to update **Nateve**.
