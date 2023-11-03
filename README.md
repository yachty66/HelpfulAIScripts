# Helpful AI Scripts

This Python package contains a collection of scripts that leverage AI to accelerate your daily workflows. The package is easy to use and can be installed on any system with Python.

## Installation

To install the package, navigate to the directory containing the `setup.py` file and run the following command:

```bash
pip install -e .
```


This will install the package in editable mode, which means you can make changes to the package's code without having to reinstall the package each time.

## Usage

Once the package is installed, you can import it in your Python scripts like any other package. For example, to use the `github_issue_history` script, you can do:

```python
from helpful_ai_scripts.github_issue_history.core import main

main()
```

You can also use the scripts directly from the command line. For example, to use the `github_issue_history` script, you can do:

```bash
python -c "from helpful_ai_scripts.github_issue_history.core import main; main()"
```

## Scripts

Currently, the package includes the following scripts:

- `github_issue_history`: Fetches and formats the history of a GitHub issue.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.

## Contact

If you have any questions or feedback, please feel free to contact the author.

## Acknowledgements

This project uses the GitHub API to fetch issue history. For more information about the GitHub API, please refer to the [official documentation](https://docs.github.com/en/rest/overview/libraries-for-the-rest-api).
