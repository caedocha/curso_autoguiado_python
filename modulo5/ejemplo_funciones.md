# Ejemplos de Funciones

## Función que no recibe parametros ni devuelve valores de retorno

```python
def say_hello():
    print("hello world!")

say_hello()
```

## Función que recibe parámetros

```python
def say_hello(name):
    greeting = "Hello there! My name is " + name
    print(greeting)

say_hello("Carlos")
```

## Función que devuelve valores de retorno

```python
def say_hello():
    greeting = "Hello there! My name is Carlos"
    return greeting

prit(say_hello())
```

## Función que recibe parámetros y devuelve valores de retorno

```python
def say_hello(name):
    greeting = "Hello there! My name is " + name
    return greeting

print(say_hello("Carlos"))
```
