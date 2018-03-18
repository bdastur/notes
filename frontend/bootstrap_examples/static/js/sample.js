 var AppView = Backbone.View.extend ({
    // el - stands for element. Every view has an element associated with HTML content, will be rendered.
    el: '#container',

    // template which has the placeholder 'who' to be substituted
    // later.
    template: _.template("<h3>Hello <%= who %></h3>"),

    // It's the first function called when this view is instantiated.
    initialize: function() {
       this.render();
    },

    // $el - it's a cached jQuery object (el), in which you can use jQuery functions to push content.

    //Like the Hello TutorialsPoint in this case.
    render: function() {
       //this.$el.html("Hello TutorialsPoint!!!");
       this.$el.html(this.template({who: "Behzad!"}));
    }
 });

 var appView = new AppView();



var SecondAppView = Backbone.View.extend ({
    // el - stands for element. Every view has an element associated with HTML content, will be rendered.
    el: '#container-2',

    // template which has the placeholder 'who' to be substituted
    // later.
    template: _.template("<h3>Hello <%= who %></h3>"),

    // It's the first function called when this view is instantiated.
    initialize: function() {
       this.render();
    },

    events: {
	    'click': 'handle_click'
    },

    handle_click: function() {
	    console.log("Click handled!");
	    this.$el.html(Math.random());
	    alert("Alerted!");
    },

    // $el - it's a cached jQuery object (el), in which you can use jQuery functions to push content.

    //Like the Hello TutorialsPoint in this case.
    render: function() {
       //this.$el.html("Hello TutorialsPoint!!!");
       this.$el.html(this.template({who: "Behzad Dastur!"}));
    }
 });

 var secondappView = new SecondAppView();


 var button1 = $('<button>test</button>');

 var ThirdAppView = Backbone.View.extend ({
    // el - stands for element. Every view has an element associated with HTML content, will be rendered.
    //el: '#container-3',

    tagName: 'div',
    id: 'thirdcontainer',

    // template which has the placeholder 'who' to be substituted
    // later.
    template: _.template("<h3>Hello <%= who %></h3>"),

    // It's the first function called when this view is instantiated.
    initialize: function() {
	   this.$el.html(Math.random());
       this.render();
       console.log("ThirdView");
    },

    events: {
	    'click': 'handle_click'
    },

    handle_click: function() {
	    console.log("Click handled!");
	    this.$el.html(Math.random());
	    alert("Alerted!");
    },

    // $el - it's a cached jQuery object (el), in which you can use jQuery functions to push content.

    //Like the Hello TutorialsPoint in this case.
    render: function() {
       //this.$el.html("Hello TutorialsPoint!!!");
       this.$el.html(this.template({who: "Behzad Dastur III!"}));
    }
 });

var thirdView = new ThirdAppView({el: button1});
thirdView.setElement(button1);
thirdView.render();

console.log(thirdView.el);

