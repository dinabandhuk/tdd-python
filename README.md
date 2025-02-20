# Test driven development in python
Test driven development in python.\
**Based on [Obey the testing GOAT](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)**

![testingGoat](./images/obey_the_testing_goat.png)\
**Always obey the testing goat. He is watching**

## Error Encountered
```bash
 raise NoSuchDriverException(msg) from err
selenium.common.exceptions.NoSuchDriverException: Message: Unable to obtain driver for firefox; For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location
```
- Solution is to install [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox .
- I chose to `cargo install geckodriver` instead because it manages packaging and installation. Make sure your system has rust cargo installed.

## Concepts
- Unit test --> from a programmer's perspective, verify correctness of internals
- Functional test --> from a user's perspective, verify it delivers what is demandeds

- Continue from [here](https://www.obeythetestinggoat.com/book/chapter_04_philosophy_and_refactoring.html)
