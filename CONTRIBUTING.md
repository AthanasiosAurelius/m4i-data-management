# How to contribute

This repository is managed by Aurelius Enterprise.

## Preamble
If you have found a bug, please [file an issue](https://gitlab.com/m4i/m4i-data-management/-/issues/new). The team will evaluate the problem and incorporate a planned fix onto the backlog if appropriate.

## Coding conventions
Please observe the following coding conventions:

### Editorconfig
Code style conventions for this repo are enforced through the `.editorconfig`.

#### Install EditorConfig
To enable `.editorconfig` for your editor, please follow these steps:

##### Visual Studio
Editorconfig is enabled in Visual Studio by default.

##### Visual Studio Code
Please install the plugin [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

##### Vim
```bash
mkdir -p ~/.vim/pack/local/start
cd ~/.vim/pack/local/start
git clone https://github.com/editorconfig/editorconfig-vim.git
```

## Testing
This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and then execute the `pytest` command from the project root folder.

```bash
pytest
```

Unit tests are grouped per module.
Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.

## Submitting changes
When working on a change, please observe the following guidelines:

### Starting off
When you want to start making changes, please check out the `master` branch into a separate `feature-branch`. Feature branches follow the following naming conventions:

- It must be descriptive of the feature or user story you're working on
- It includes a user story number where applicable
- Words are separated using `kebab-case`

The following example checks out the `master` branch into the  `1234-my-feature-branch`, and creates the feature branch if it doesn't yet exist:

```bash
git checkout -b 1234-my-feature-branch main
```

### Commiting work in progress
Please use your `feature-branch` to commit your work while it is in progress.

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

```bash
git commit -m "A brief summary of the commit

A paragraph describing what changed and its impact."
```

### Submitting changes
To submit the changes in your `feature-branch` to the `master` branch, please send a [merge request](https://gitlab.com/m4i/m4i-data-management/-/merge_requests/new).

#### Merge request conventions
A merge request should consist of the following:

- A reference to the feature or user story on the DMP backlog
- References to any applicable design documents.
- A short description of your proposed solution.

#### Review criteria
Merge requests are subject to peer review and need at least `1` approval before being allowed to merge. The following criteria generally apply:

- The merge request includes all the necessary information as described above
- New code must be covered by unit tests
- All existing unit tests must be updated to reflect the changes
- New code must be covered by documentation in accordance with the guidelines
- All existing documentation must be updated to reflect the changes
- All unit tests must pass

#### Merge policies
Furthermore, the following policies apply for pull requests to the `master` branch:

- Pull requests to main need at least `1` approval before being allowed to merge.
- Stale approvals are automatically dismissed.
- The only merge strategy allowed is squash merge.
- Merged branches will be automatically deleted.
