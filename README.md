
# **Super case converter 2000**

### Quick start

___

First, install the library

```
pip3 install super-case-converter-2000
```

include in your project

```python
from converter import case
```

## Methods
# snake

Convert string to '*snake case*' string

#### alias
- c_case

```python
snake(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```
#### Example
```python
string_camel = "stringCase"

string_snake = case.snake(string=string_camel)

# alias
string_c_case = case.c_case(string=string_camel)

print(string_snake, string_c_case)
```

##### Output
```console
string_case string_case
```

#### Example
```python
string_custom = "string!!case"

string_snake = case.snake(string=string_custom, replaceSeparator='!!')

# alias
string_c_case = case.c_case(string=string_custom, replaceSeparator='!!')

print(string_snake, string_c_case)
```

##### Output
```console
string_case string_case
```


# camel
Convert string to '*camel case*' string

```python
camel(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```

#### Example
```python
string_snake = "string_case"

string_camel = case.camel(string=string_snake)

print(string_camel)
```

##### Output
```console
stringCase
```

#### Example
```python
string_custom = "string!!case"

string_camel = case.camel(string=string_custom, replaceSeparator='!!')

print(string_camel)
```

##### Output
```console
stringCase
```

# pascal
Convert string to '*pascal case*' string
#### alias
- capital_camel


```python
pascal(string: str = "", replaceSeparator: Optional[str] = None) -> str:

```

#### Example
```python
string_snake = "string_case"

string_pascal = case.pascal(string=string_snake)

# alias
string_capital_camel = case.capital_camel(string=string_snake)

print(string_pascal, string_capital_camel)
```

##### Output
```
StringCase StringCase
```
#### Example
```python
string_custom = "string!!case"

string_pascal = case.pascal(string=string_custom, replaceSeparator='!!')

print(string_pascal)

```
##### Output
```
StringCase
```

# kebab
Convert string to '*kebak case*' string

#### alias
- kebabm
- caterpillar
- dash
- hyphen
- lisp
- spinal
- css

```python
kebab(string: str = "", replaceSeparator: Optional[str] = None) -> str:

```

#### Example
```python
string_snake = "string_case"

string_kebab = case.kebab(string=string_snake)

# alias
string_caterpillar = case.caterpillar(string=string_snake)

print(string_kebab, string_caterpillar)
```

#### Output
```
string-case string-case
```

#### Example
```python
string_custom = "string!!case"

string_kebab = case.kebab(string=string_custom, replaceSeparator='!!')

print(string_kebab)
```

#### Output
```
string-case
```

# flat
Convert string to '*flat case*' string
```python
flat(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```

#### Example
```python
string_snake = "string_case"

string_flat = case.flat(string=string_snake)

print(string_flat)
```

#### Output
```
stringcase
```
#### Example
```python
string_custom = "string!!case"

string_flat = case.flat(string=string_custom, replaceSeparator='!!')

print(string_flat)
```

#### Output
```
stringcase
```

# raw
Convert string to '*raw case*' string
```python
raw(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```

#### Example
```python
string_snake = "string_case"

string_raw = case.raw(string=string_snake)

print(string_raw)
```

#### Output
```
string case
```
#### Example
```python
string_custom = "string!!case"

string_raw = case.raw(string=string_custom, replaceSeparator='!!')

print(string_raw)
```

#### Output
```
string case
```

# path
Convert string to '*path*' string
```python
path(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```

#### Example
```python
string_snake = "string_case"

string_path = case.path(string=string_snake)

print(string_path)
```

#### Output
```
string/case
```

#### Example
```python
string_custom = "string!!case"

string_path = case.path(string=string_custom, replaceSeparator='!!')

print(string_path)
```

#### Output
```
string/case
```

# piped
Convert string to '*piped*' string
```python
piped(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```

#### Example
```python
string_snake = "string_case"

string_piped = case.piped(string=string_snake)

print(string_piped)
```

#### Output
```
string|case
```

#### Example
```python
string_custom = "string!!case"

string_piped = case.piped(string=string_custom, replaceSeparator='!!')

print(string_piped)
```

#### Output
```
string|case
```

# title
Convert string to '*title case*' string
```python
title(string: str = "", replaceSeparator: Optional[str] = None) -> str:
```


#### Example
```python
string_snake = "string_case"

string_title = case.title(string=string_snake)

print(string_title)
```

#### Output
```
String Case
```

#### Example
```python
string_custom = "string!!case"

string_title = case.title(string=string_custom, replaceSeparator='!!')

print(string_title)
```

#### Output
```
String Case
```

# custom

Convert string to '*custom separator*' string


```python
custom(string: str = "", separator: str = "",replaceSeparator: Optional[str] = None) -> str:
```


#### Example
```python
string_snake = "string_case"

string_custom = case.custom(string=string_snake, separator='<#>')

print(string_custom)
```

#### Output
```
string<#>case
```

#### Example
```python
string_custom = "string!!case"

string_custom = case.custom(string=string_custom, separator='<#>', replaceSeparator='!!')

print(string_custom)
```

#### Output
```
string<#>case
```

# custom_between

Convert string to '*custom between*' list of strings

```python
custom_between(string: str = "", open: str = "", close: Optional[str] = None, replaceSeparator: Optional[str] = None) -> list:

```

#### Example
```python
string_snake = "string_case"

list_custom_between = case.custom_between(
  string=string_snake,
  open='<',
  close='>'
)

print(list_custom_between)
```

#### Output
```
['<string>', '<case>']
```

#### Example
```python
string_custom = "string!!case"

list_custom_between = case.custom_between(
  string=string_custom,
  open='<',
  close='>',
  replaceSeparator='!!'
)

print(list_custom_between)
```

#### Output
```
['<string>', '<case>']
```

# sentence
Convert string to '*sentence case*' string or list of strings
```python
sentence(string: str = "", listMode: bool = False, capitalize: bool = False, upper: bool = False, replaceSeparator: Optional[str] = None) -> Union[str, list]:

```

#### Example
```python
string_snake = "string_case"

string_sentence = case.sentence(string=string_snake)

print(string_sentence)
```

#### Output
```
String case
```

#### Example
```python
string_snake = "string_case"

string_sentence_capitalize = case.sentence(string=string_snake, capitalize=True)

print(string_sentence_capitalize)
```

#### Output
```
String Case
```

#### Example
```python
string_snake = "string_case"

string_sentence_upper = case.sentence(string=string_snake, upper=True)

print(string_sentence_upper)
```

#### Output
```
STRING CASE
```

#### Example
```python
string_snake = "string_case"

list_sentence = case.sentence(string=string_snake, listMode=True)

print(list_sentence)
```

#### Output
```
['String', 'case']
```
