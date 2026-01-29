## Processing the message from the user
- This project is developed to demonstrate the use of click to get the input from the user and process the message either locally or in the remote server.


### Setup guide:
- Install the `assignment_10-1.0.0-py3-none-any.whl`.
- If the wheel file is not available then `poetry build` -->> under dist you will find `assignment_10-1.0.0-py3-none-any.whl`
- After installation use `start-server` to start the gRPC server.
- Then you can use the command `emit-message` to use the application to process the message.

```
Options:
  -m, --message TEXT       Message to be repeated. Use double quotes on Windows if
                       the message contains spaces.
  -c, --count INTEGER  Number of times the words must be printed.
  -g, --use-grpc           Sends the message and count to the gRPC server.
  -h, --help           To show the help message.
```
