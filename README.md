# ofxstatement-revolut-italian

This is a plugin for use with [ofxstatement](https://github.com/kedder/ofxstatement) package. It implements
a parser for the Revolut CSV-formatted(italian) bank statement.

The CSV isn't very machine readable, so we need to do some ugly string
parsing to figure out the different field values.

Issue reports and pull requests welcome.

This module is based on the Osuuspankki ofxstatement parser found at
https://github.com/koodaamo/banking.statements.osuuspankki

## Installation

### From source
```
git clone https://github.com/chiuky/ofxstatement-revolut.git
python3 setup.py install
```

## Configuration options


| Option        | Description                                                                                                                                    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `account`     | Define the account of this bank statement                                                                                                      |
| `currency`    | The base currency of the account                                                                                                               |
| `date_format` | The date format in the bank statement. Note that you have to use double `%`-marks in the settings file like this: `date_format = %%b %%d %%Y` |
| `locale`      | The locale of the csv file to parse. Note that you have to use a locale currently installe on your machine.For this plugin default is :it_IT   |


### Usage

You can check that ofxstatement is working by running:

$ ofxstatement list-plugins
You should get a list of your installed plugins.

After installation, the usage is simple:

$ ofxstatement convert -t <plugin-name> bank_statement.csv statement.ofx
The resulting statement.ofx is then ready to be imported into a personal accounting system.

### useful links
schema of generated file
https://schemas.liquid-technologies.com/ofx/2.1.1

ofxstatement
https://github.com/kedder/ofxstatement

for advanced configuration
https://github.com/kedder/ofxstatement#advanced-configuration



