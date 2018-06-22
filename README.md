# meetup-security-lvl1

## Exercise 1

When an application asks you to create a password, you can often read something like **8 characters at least with at least one digit and one uppercase letter**. This exercise's purpose is show that it is really a minimum.

### Statement of work

Within a group of two, the first person creates a password containing 5 characters which can be a lowercase letter or a digit.
The second person tries to guess the password. The solution we are looking for is nicknamed `brute force`. It is about computing all possible solutions.

### Example

- First person puts his password to guess into a variable
```
#!/bin/bash
read -s MY_PASSWORD
```
- Second person writes his code trying to guess what is in this environment variable.
```
python guess.py
Found : your password was xxx12
```

### Main facts

- Each character of this kind of password has 36 possibilities.
- Using a 5 characters-long password means more than 60 millions of possibilities and yet only a few seconds are required to compute them all ...
