#!/usr/bin/ruby

# A print statement
puts "Hello Ruby"

# Data types and variables.
## Declaring a variable.
simple_str = "This is a test string"
simple_num = 434

puts "Simple String: #{simple_str}, Number: #{simple_num}\n"



# Defining a class.
class Employee
    # Specifying an attr_reader or attr_accessor,
    # will create a getter for the given variable 'employee_id'
    attr_reader :employee_id
    @@employee_count = 0

    def initialize (id, name)
        @employee_name = name
        @employee_id = id
        @@employee_count += 1

    end

    def display_class_instance_variables ()
        puts "  Employee name:  #@employee_name"
        puts "  Employee id: #@employee_id"
        puts "  Employee count: #@@employee_count"
    end
end

# Initialize a new employee object.
employee_1 = Employee.new(2333, "behzad")

# One way of accessing instance variables.
emp_name = employee_1.instance_variable_get(:@employee_name)
puts "Name: #{emp_name}"

# Another way. In this case we had setup a getter using attr_reader
puts "Employee id: #{employee_1.employee_id}"

# Get class variables.
emp_count = Employee.class_variable_get(:@@employee_count)
puts "count: #{emp_count}"


employee_2 = Employee.new(123, "John Doe")
employee_3 = Employee.new(324, "David")


employee_1.display_class_instance_variables()

