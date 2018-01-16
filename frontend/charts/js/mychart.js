$(function () {
	Highcharts.setOptions({
		chart: {
			backgroundColor: {
				linerGradient: [0, 0, 300, 300],
				stops: [
					[0, 'rgb(255,255,255)'],
					[1, 'rgb(240,240,255)']
				]
			},
			borderWidth: 2,
			plotBackgroundColor: 'rgba(255,255,255,.9)',
			plotShadow: true,
			plotBorderWidth: 1
		}
	})

			    var myChart = Highcharts.chart('container', {
			        chart: {
			            type: 'bar'
			        },
			        title: {
			            text: 'Fruit Consumption'
			        },
			        xAxis: {
			            categories: ['Apples', 'Bananas', 'Oranges']
			        },
			        yAxis: {
			            title: {
			                text: 'Fruit eaten'
			            }
			        },
			        series: [{
			            name: 'Jane',
			            data: [1, 0, 4]
			        }, {
			            name: 'John',
			            data: [5, 7, 3]
			        }]
			    });
			});
			
				

$(function () { 
			    var myChart = Highcharts.chart('chart-compare-fruits', {
			        chart: {
			            type: 'bar'
			        },
			        title: {
			            text: 'Fruit Consumption'
			        },
			        xAxis: {
			            categories: ['Apples', 'Bananas', 'Oranges']
			        },
			        yAxis: {
			            title: {
			                text: 'Fruit eaten'
			            }
			        },
			        series: [{
			            name: 'Jane',
			            data: [1, 0, 4]
			        }, {
			            name: 'John',
			            data: [5, 7, 3]
			        }]
			    });
			});

$(function () { 
			    var myChart = Highcharts.chart('chart-compare-fruits-2', {
			        chart: {
			            type: 'bar'
			        },
			        title: {
			            text: 'Fruit Consumption'
			        },
			        xAxis: {
			            categories: ['Apples', 'Grapes', 'Oranges']
			        },
			        yAxis: {
			            title: {
			                text: 'Fruit eaten'
			            }
			        },
			        series: [{
			            name: 'Jane',
			            data: [1, 0, 4]
			        }, {
			            name: 'John',
			            data: [5, 7, 3]
			        }]
			    });
			});
