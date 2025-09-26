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
===============================================================
                🚀 📌Decorators In Python🚀
===============================================================

📌 1. What is a Decorator?
---------------------------------------------------------------
- A decorator is a function in Python that allows you to modify 
  or extend the behavior of another function or class 
  without changing its source code.
- In simple words:
      "A decorator is a wrapper around a function."

---------------------------------------------------------------
📌 2. Why Do We Use Decorators?
---------------------------------------------------------------
✅ Add extra functionality to functions without editing them.  
✅ Keep code clean and maintainable.  
✅ Reuse logic (Don’t Repeat Yourself - DRY Principle).  
✅ Commonly used for:
    - Logging
    - Authentication
    - Measuring execution time
    - Access control
    - Debugging

---------------------------------------------------------------
📌 3. How Do Decorators Work?
---------------------------------------------------------------
- A decorator is a higher-order function (takes another function as input).
- Inside it, we define a **wrapper function**.
- The wrapper adds extra behavior before and/or after 
  the original function call.
- Finally, the decorator returns this wrapper.

Syntax:
    @decorator_function
    def my_function():
        pass

This is equivalent to:
    my_function = decorator_function(my_function)

---------------------------------------------------------------
📌 4. Steps to Create a Decorator
---------------------------------------------------------------
1️⃣ Define a decorator function.  
2️⃣ Inside it, define a wrapper function.  
3️⃣ Add any extra logic in wrapper.  
4️⃣ Call the original function inside wrapper.  
5️⃣ Return the wrapper.  
6️⃣ Use '@decorator' above the target function.  

---------------------------------------------------------------
📌 5. Real-Life Analogy
---------------------------------------------------------------
Imagine you have a cup of tea ☕:
- Base tea = Original function  
- Sugar, milk, lemon = Decorators  
- The tea (function) stays the same, but its taste (behavior) changes.  

---------------------------------------------------------------
📌 6. Key Takeaway
---------------------------------------------------------------
👉 A decorator = Function + Extra Features (without touching original code)  

===============================================================
"""
