var cost_value = []

var planetChartData = {
	type: 'line',
	data: {
		labels: ['January', 'February', 'March', 'April', 'May', 'June'],
		datasets:[{
			label: 'My first dataset',
			backgroundColor: '#f6d1c4',
			borderColor: '#772953',
			data: cost_value
		}]
    },
    options: {}
}


Vue.component('line-chart', {
	template: "<div id='app3'><canvas id='chart22'></canvas></div>",
    data (){
	    return {
            planetChartData: planetChartData,
	    }
    },
	methods:{
		createChart(chartId, chartData) {
			const ctx = document.getElementById(chartId);
		    const myChart = new Chart(ctx, {
		        type: chartData.type,
		        data: chartData.data,
		        options: chartData.options,
		    });
		}
	},
	mounted () {
		this.createChart('chart22', this.planetChartData)
	}
})

new Vue({
	el: "#app3",
	data: {
		cost_value: [4, 1, 2, 2, 2, 3]
	}
})


/*
var ctx = document.getElementById("chart2").getContext('2d');
var cost_data = [2, 3, 5, 2, 3, 1]

var chart = new Chart(ctx, {
	type: 'line',
	data: {
		labels: ['January', 'February', 'March', 'April', 'May', 'June'],
		datasets:[{
			label: 'My first dataset',
			backgroundColor: '#f6d1c4',
			borderColor: '#772953',
			data: cost_value
		}]
	},
	options: {}

})
console.log("cost: " + cost_value)
*/


/*
var ctx = document.getElementById("chart2").getContext('2d');
new Vue({
    el: "#app2",
    data: {

            cost: "... loading",
            chart: new Chart(ctx, {
				type: 'line',
					data: {
						labels: ['January', 'February', 'March', 'April', 'May', 'June'],
						datasets:[{
							label: 'My first dataset',
							backgroundColor: '#f6d1c4',
							borderColor: '#772953',
							data: cost_value
						}]
					},
					options: {}
            })

    },
    created () {
            axios.get("http://localhost:5000/costs")
            .then(response => {
                console.log("ressponse" + response)
                this.cost = response.data
                cost_value = response.data
                console.log("cost: " + cost_value)
                this.renderChart(this.data, this.options)
            })
            .catch(error => {
                    console.log("Errror: " + error.message)
                    this.users = "Therer was an errrorr in getting users" + error.message
            })
    }
})
*/





var ctx1 = document.getElementById("chart1").getContext('2d');

var chart = new Chart(ctx1, {
	type: 'line',
	data: {
		labels: ['January', 'February', 'March', 'April', 'May', 'June'],
		datasets:[{
			label: 'My first dataset',
			backgroundColor: '#f6d1c4',
			borderColor: '#772953',
			data: [3, 2, 3, 4, 5, 6]
		}]
	},
	options: {}

})


/*
var ctx = document.getElementById("chart2").getContext('2d');
var cost_data = [2, 3, 5, 2, 3, 1]

var chart = new Chart(ctx, {
	type: 'line',
	data: {
		labels: ['January', 'February', 'March', 'April', 'May', 'June'],
		datasets:[{
			label: 'My first dataset',
			backgroundColor: '#f6d1c4',
			borderColor: '#772953',
			data: cost_value
		}]
	},
	options: {}

})
console.log("cost: " + cost_value)
*/

















