# Homework solution

in order run the code in vscode I run this in comand line to run mlserver frist 

```batch
mlflow ui --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts
```

After that I develop the following run specs on vscode

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run Data Prep",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/homeworks/hw2/homework/preprocess_data.py",  // Adjust the path if necessary
            "args": [
                "--raw_data_path", "${workspaceFolder}/src/homeworks/hw2/data",   // Replace with your actual raw data path
                "--dest_path", "${workspaceFolder}/src/homeworks/hw2/data-process"           // Replace with your actual destination path
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/src/homeworks/hw2"
        },
        {
            "name": "Python: Run Data train",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/homeworks/hw2/homework/train.py", 
            "args": [
                "--data_path", "${workspaceFolder}/src/homeworks/hw2/data-process",  
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/src/homeworks/hw2"
        },
        {
            "name": "Python: Run Data hyper",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/homeworks/hw2/homework/hpo.py", 
            "args": [
                "--data_path", "${workspaceFolder}/src/homeworks/hw2/data-process",
                "--num_trials", "10"  
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/src/homeworks/hw2"
        },
        {
            "name": "Python: Run model registry",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/homeworks/hw2/homework/register_model.py", 
            "args": [
                "--data_path", "${workspaceFolder}/src/homeworks/hw2/data-process",
                "--top_n", "5"  
            ],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/src/homeworks/hw2"
        }
    ]
}
```
The results that I got are in homework answere!

