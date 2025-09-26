# Python Arithmetic Guide: Order of Operations ✨

In Python (and mathematics in general), the **order of operations** determines how expressions are evaluated. Remember it with **PEMDAS**:

**🔹 P – Parentheses `()`**  
Operations inside parentheses are evaluated first.

**🔹 E – Exponents `**`**  
Handles powers and roots next.

**🔹 M / D – Multiplication `*` & Division `/`**  
Evaluated from **left to right**.

**🔹 A / S – Addition `+` & Subtraction `-`**  
Finally, addition and subtraction are evaluated from **left to right**.

> ✅ Following this order ensures your Python calculations are accurate and predictable.

**help() displays two things:**

the header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument we can describe as number. Additionally, we can optionally give a separate argument which could be described as ndigits.
A brief English description of what the function does.

"""
===========================================================
                  PYTHON DECORATORS - THEORY
===========================================================

🔹 1. Introduction
    - A decorator in Python is simply a function that takes another 
      function as input and extends or modifies its behavior.
    - It allows us to add extra features to existing code 
      without changing the original function.
    - Think of it as "wrapping" a function with additional logic.

🔹 2. Why Use Decorators?
    ✅ Code reusability (write once, use everywhere).
    ✅ Keep functions clean (no need to edit original code).
    ✅ Useful for logging, authentication, timing, caching, etc.
    ✅ Follows DRY principle (Don’t Repeat Yourself).

🔹 3. How Do They Work?
    - A decorator is a higher-order function.
    - It usually defines an inner function (called a wrapper).
    - The wrapper adds extra behavior before/after the target function.
    - Finally, the decorator returns this wrapper.

    Example (conceptually):
        @decorator_function
        def my_function():
            pass

    Equivalent to:
        my_function = decorator_function(my_function)

🔹 4. Steps of a Decorator
    1. Define a decorator function.
    2. Inside it, create a wrapper function.
    3. Add extra code before/after calling the original function.
    4. Return the wrapper function.
    5. Use '@decorator' above the target function.

🔹 5. Real-Life Analogy
    - Imagine you are drinking tea ☕.
    - The tea (main function) is the same.
    - But you can add sugar, milk, or ginger (decorators).
    - The base tea does not change, but its behavior (taste) is enhanced.

===========================================================
"""
