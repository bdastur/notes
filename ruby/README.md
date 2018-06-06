# Ruby Notes:

## Variables in Ruby:
* Local Variables:
  * Scope is local to a method.
  * Not available outside the method.
  * Beging witha lowercase letter or _

* Instance Variables:
  * Available across methods for any particular instance or object.
  * Instance variables are preceded by a (@) followed by the variable name.

* Class Variables:
  * Belong to the class.
  * Available across different objects.
  * Preceded by a (@@) followed by the variable name.

* Global Variables:
  * Available globally across classes.
  * Preceded by a $ sign.


NOTE: In ruby, you can access value of any variable or constant by putting a '#'
      character before the variable or constant.

```
simple_string = "Test string"
puts "Print simple string: #{simple_string"

```

NOTE: You can substitute the value of any Ruby expression into a string 
      using the sequence #{ expr }.
```
puts "Multiplication: #{2 * 4 * 4}"
```


