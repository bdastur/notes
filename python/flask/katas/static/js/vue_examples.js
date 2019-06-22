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

