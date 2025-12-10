# Python Coding Standards and Guidelines
### **Naming Conventions**

*   Avoid single-character names like `l`, `O`, `I`.
*   Use short, lowercase names. Underscores if needed.
*   Use `PascalCase` for class names
*   Use PascalCase with `_T` suffix (e.g., `ContextManager_T`).
*   Use PascalCase with `Error` suffix.    
*   Use `snake_case` for variables and functions
*   Prefix non-public with `_`, and use `__` for name mangling.
*   Use `UPPER_CASE` for constants
    
* * *

### **Programming Recommendations**

**Boolean & None Checks**
*   Use `is None` / `is not None` for `None` checks
    
*   Use `if cond:` / `if not cond:`. We don't have to compare with True or False. Check for true → `if A:`, false → `if not A:`
    
*   Use `if not seq:` for empty sequences.
    
**Exception Handling**
*   Be specific. Avoid bare `except:`.

*   Use `try-except` for expected errors only. Do error handling with known errors and raise some custom exceptions if needed.
    
*   Always think of fail cases and proper error messages – app shouldn’t break
    
*   Use `with` or `finally` to manage resources
    
**Code Documentation**
    
*   Document the application setup, features in README
*   Comments for implementation details. 
*   Write meaningful docstrings for all public modules, classes, and functions
*   Prefer clean, readable code over excessive commenting
*   Remove unused params from docs

* * *

### **Code Structure and Design**

**Modularity & Readability**
*   The code should be readable, modular and scalable
    *   Adhere SOLID principles
        
    *   Identifiers should be meaningful
        
    *   All functions should be strongly typed
        
*   Keep functions short, focused and testable functions
    
*   One purpose per function
    
*   identifiers (variables, class or function names etc) should be named meaningfully and should be easily understandable to a developer who is not familiar with the codebase
    
*   Organize related functions/classes logically
    
*   Separate concerns using modules and packages
    
*   Avoid deep nesting
    
*   Use blank lines to separate logical blocks and this will improve readablity
    
*   Follow PEP 8 style guidelines
    
*   Limit lines to 79–80 characters
    
*   Use 4-space indentation
    
*   Avoid overly clever or compressed code
    
*   Avoid complex syntax
    
*   Proper branch naming
    
*   Have some default values in a separate file
    
*   Remove unused code wherever not used to ensure maintainability
    
*   Stick with single quote or double quote for strings
    
*   This indentation should be good – keep line length per PEP or use new lines per argument
    
*   Use keyword arguments to improve code readability.

*   Use spell checker extension
    
**Efficiency & Optimization**
*   The code should be well optimized
    *   Use efficient data structures and algorithms
        
    *   Optimize memory (e.g., `yield`)
        
    *   Use concurrency/parallels where applicable
        
    *   Use caching for API responses
        
*   Use list comprehensions
    
*   Use generators for large data
    
*   Avoid unnecessary memory usage with some objects like client connections
    
*   Use `enumerate()` instead of `range(len(...))`
    
*   Use `zip()` to iterate multiple sequences
    
*   Use tuple unpacking (`a, b = b, a`)
    
*   while building APIs response time in crucial, efficient caching must be used without bloating the memory, possible things needs to be pre computed on server start.

*   If any two I/O bound tasks can be executed concurrently, should be executed concurrently.
*   If any two intense compuations can be executed parallely, should be decided to execute parallely or not considering the time to spawn new process.

**Immutability**
*   Use tuples, mapping proxy, frozenset, frozen pydantic models where applicable.
    
**Pydantic Usage**
*   Strong validations with `@field_validator`, `@model_validator`.
    
**Resource & Import Handling**
*   Use `with` statement for resource management
    
*   Avoid using `import *`
    
*   Always use named arguments
    
*   Remove unused imports
    
*   Group imports: standard → third-party → local
    
*   Have order for import statements: in-built → installed → project modules
    
*   Specified package should be present in poetry
    

* * *

### **Function Design**

*   All functions including private functions should be strongly typed
    
*   Add type hints and default parameters if applicable
    
*   Use `None` as return type hint when applicable
    
*   Define positional arguments first, then optional
    
*   Avoid too many parameters
    
*   Use early returns to reduce nesting
   

* * *

### **Testing**

*   Test cases should include expected behaviour, error handling, and corner cases
    
*   Write unit tests for critical paths
    
*   Use fixtures for setup/teardown
    
*   Use parametrizations
    
*   Tests should be readable and maintainable
    
*   Mock external systems
    

* * *

### **Logging & Debugging**

*   Give meaningful error in user end, as we don't need these detailed errors, but we need the original error logged with full trace, use `logger.exception`.
    
*   Configure log level with `DEBUG` as default, so developer can easily debug in development and use logger to log errors.
    
*   If FastAPI server, run in DEBUG (reload)
    
*   Have good log messages
    

* * *

### **Environment & Setup**

*   Add default env in `.env.example` wherever applicable
    
*   Avoid quotes and spaces in env to compatible with docker env
    
*   Add Dockerfile and docker-compose for easy setup in developer end
    

* * *

### **Code Formatting & Style**

*   Use auto code formatters
    
*   Triple quotes are for multiline comments – avoid them for short ones

*    Make small (atomic) commits whenever possible
    

* * *