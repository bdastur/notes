#!/usr/bin/ruby

# A print statement.
puts "Hello Ruby"

=begin
This is a multiline
comment, spanning multiple
lines
=end


# Data types and variables.
## Declaring a variable.
simple_str = "This is a test string"  # A trailing comment.
simple_num = 434                      # A trailing comment.

$var1 = 43400

puts "Simple String: #{simple_str}, Number: #{simple_num}\n"
puts "Global variable var1: #$var1"


###########################################################
# Defining a class.
class Employee
    # Specifying an attr_reader or attr_accessor,
    # will create a getter for the given variable 'employee_id'
    attr_reader :employee_id
    @@employee_count = 0
    @@company_name = "Acme Corp"

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

# Using the Double colon operator.
# FIXME: company_name = ::Employee.company_name

employee_2 = Employee.new(123, "John Doe")
employee_3 = Employee.new(324, "David")

employee_1.display_class_instance_variables()


class Test
    def get_some_value(id)
        test_key = {
            "EncryptedKey" => 3232,
            "KEY_ID" => "some random arn"
        }
    rescue TypeError
        puts "Typeerror"
        retry

        enable_something(test_key['KEY_ID'])
        return test_key
    end

    def enable_something(key)
        puts "enablethis #{key}"
    end

end

testobj = Test.new()
valobj = testobj.get_some_value(42)
puts "value obj: #{valobj}"

###########################################################

# You can substitute the value of any Ruby expression into a string 
# using the sequence #{ expr }.
puts "Multiplication: #{2 * 4 * 4}"

###########################################################
# Arrays.

simple_arr = [ 1, 3, 4, 5, 6]
puts "array: #{simple_arr}, index 1: #{simple_arr[1]}"
simple_arr.each do |i|
    puts i
end

# If the array is not initalized, values will be nil.
new_arr = Array.new(20)
puts "array size: #{new_arr.size}, array len: #{new_arr.length}, arr: #{new_arr}"

new_arr_1 = Array.new(20, "test")
puts "array size: #{new_arr_1.size}, array len: #{new_arr_1.length}"

############################################################
# Hashes.

simple_hash = {"employee_id" => 2424, "employee_name" => "behzad", "age" => 40}
puts "Simple hash: #{simple_hash}"

simple_hash.each do |key, value|
    puts "key: #{key}, value: #{value}"
end

puts "Emp name: #{simple_hash['employee_name']}"


############################################################
# Methods.











