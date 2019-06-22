new Vue({
    el: "#app1",
    data: {
	    order: 1,        //means ascending
	    dams: [
		    {name: 'Nurek dam', country: 'Tajikistan', electricity: 4333},
		    {name: 'Hover dam', country: 'USA', electricity: 45000},
		    {name: 'Guri dam', country: 'Venezuela', electricity: 40388}
	    ]
    },
    computed: {
	    sortByElectricity() {
		    return this.dams.sort((d1, d2) => (d2.electricity - d1.electricity) * this.order)
	    }
    },
    methods: {
	    sort() {
		    this.order = this.order * -1
	    }
    }
})


new Vue({
    el: "#app2",
    data: {
	    isNight: false
    },
    computed : {
	    isNightComputed() {
		    var hours = new Date().getHours();
		    console.log("hours: " + hours);
		    return(hours < 7)
	    }
    }
})

new Vue({
    el: "#app3",
    data: {
	    users: "... loading",
	    users1: ["rick", "pink", "Coors"],
	    users2: {
		    "rick": {
			    "age": 43
		    }
	    }
    },
    created () {
	    axios.get("http://localhost:5000/users")
	    .then(response => {
		    console.log("ressponse" + response)
		    this.users = response.data
		    console.log("User: " + this.users['jake']['age'])
	    })
	    .catch(error => {
		    console.log("Errror: " + error.message)
		    this.users = "Therer was an errrorr in getting users" + error.message
	    })
    },
    computed: {
	    getUsers() {
		    console.log("GetUsers: " + this.users1)
		    return this.users1
	    }
    }
})
