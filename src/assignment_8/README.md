# Assignment Observations

This assignment focuses primarily on creating venvs' to resolve the dependency errors and how poetry can be used to do the same efficiently.

### Task 1 & Task 2
- Implemented two simple python scripts one to depend on click 7.0 and the other to depend on click 8.0
- When using the global environment the conflicts arises for `app_b` as it requires click 8.0
- When upgraded using `pip --upgrade` the `app_a` faced the conflicts.
- In order to overcome this issue Python provides a way to overcome the issue by providing the virtual environments.
- This virtual environment is very much like a container that holds the dependencies for the particular files that are executed under the environment which is active.
- To demonstrate this I created `venv_app_a` for `app_a` and `venv_app_b` for `app_b`, and installing click version 7 in environment a and click 8 in environment b
- To execute the scripts the scripts should be run on respective environment.
- This removes all the conflicts related to dependency versions.


### Task 3 & Task 4
- Implemented the starter script provided in the assignment documentation.
- Tried `pip install pandas==1.1.0 numpy==1.19.0 matplotlib==3.3.0` which raises error because it requires `Python 3.8` as the dependency.
- In order to overcome the error creating a separate environment is suggested.
- The traditional method using `pip` will throw error because it supports minimal Dependency resolution but `poetry` supports full resolution.
- The poetry also locks the known good versions of the dependency in the lock file.
- The poetry also treats python version itself as an dependency.
- To change the python version for the environment I used `poetry env use <Python38.exe_path>`
- After this the `poetry add pandas==1.1.0 numpy==1.19.0 matplotlib==3.3.0` can be executed successfully to add the dependency for the environment.
- Now this resolves the full dependency graph and makes the script executable only in the newly created environment.

### Setup for task 1 & 2
```
    python -m venv venv_app_a
    venv_app_a\Scripts\activate
    ython -m pip install click==7.0 (8.0 for app_b)
```
