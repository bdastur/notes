
'use strict';

var app = {}; // create namespace for our app

//--------------
// Models
//--------------
app.Todo = Backbone.Model.extend({
    defaults: {
        title: 'this is a test title',
        completed: false
    },
    initialize: function() {
	    console.log("This model is initialized!");
	    this.on('change', function() {
		    console.log("- Vaules for this mode have changed");
	    });
	    this.on('all', function() {
		   console.log("-- all events triggered!");
	    });
	    this.on('change:title', function(){
            console.log('Title value for this model has changed.');
        });
    }
});

//--------------
// Collections
//--------------
app.TodoList = Backbone.Collection.extend({
    model: app.Todo,
    localStorage: new Store("backbone-todo")
});

// instance of the Collection
app.todoList = new app.TodoList();

//--------------
// Views
//--------------

// renders individual todo items list (li)
app.TodoView = Backbone.View.extend({
    tagName: 'li',
    template: _.template($('#item-template').html()),
    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        return this; // enable chained calls
    }
});

// renders the full list of todo items calling TodoView for each one.
app.AppView = Backbone.View.extend({
    el: '#todoapp',
    initialize: function () {
        this.input = this.$('#new-todo');
        app.todoList.on('add', this.addAll, this);
        app.todoList.on('reset', this.addAll, this);
        app.todoList.fetch(); // Loads list from local storage
    },
    
    events: {
        'keypress #new-todo': 'createTodoOnEnter'
    },
    
    createTodoOnEnter: function(e){
        if ( e.which !== 13 || !this.input.val().trim() ) { // ENTER_KEY = 13
            return;
        }
        app.todoList.create(this.newAttributes());
        this.input.val(''); // clean input box
    },
    
    addOne: function(todo){
        var view = new app.TodoView({model: todo});
        $('#todo-list').append(view.render().el);
    },
    
    addAll: function(){
        this.$('#todo-list').html(''); // clean the todo list
        app.todoList.each(this.addOne, this);
    },
    
    newAttributes: function(){
        return {
            title: this.input.val().trim(),
            completed: false
        }
    }
});

//--------------
// Initializers
//--------------   

app.appView = new app.AppView(); 

