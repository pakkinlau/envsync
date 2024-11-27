# envsync

`envsync` is creating a apt-get experience for python packages, to automatically update the content of requirements.txt and synchronize the virtual environments of any Python projects with Git hooks.

## Installation

You can install envsync from PyPI:

```
pip install envsync
```

## Usage


To initialize a local Git repository with the necessary hooks, run:

```
envsync /path/to/local_git_repo_folder
```

This command will set up the following hooks:

* `post-checkout`: Updates `requirements.txt` whenever you checkout a new branch or commit.
* `pre-commit`: Prevents committing files larger than 100MB.
* `post-merge`: Updates the virtual environment if `requirements.txt` changes after a merge.

## Contributors
Pak Kin LAU: https://github.com/pakkinlau
Alex MASON: https://github.com/amason445


## License 
This project is licensed under the MIT License.
