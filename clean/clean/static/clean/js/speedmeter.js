class Speedmeter{
	constructor(id, unit="Km/h", value = 50, zeroValue = 0, endValue = 100, pointerColor = "black", backgroundSteps = [10, 30, 70, 90, 100], backgroundColor = ["red", "orange", "yellow", "green", "darkgreen"]){
		var html = '<div class="chart-container" style="position: relative">';
		var percentValue = value/(endValue-zeroValue)*100;
		html = html + '<canvas id="'+ id +'-potencia" style="position: absolute"></canvas>';
		html = html + '<canvas id="'+ id +'-pbackground"></canvas>';
		html = html + '</div>';
		html = html + '<div class="row">';
		html = html + '<div class="col-3">' +  zeroValue + '</div>';
		html = html + '<div class="col-6 text-center"><h2 style="margin: -50px" id="'+ id + '-speedvalue">' + (percentValue*(endValue-zeroValue)/100 + zeroValue).toFixed(0) + ' ' + unit + '</h2></div>';
		html = html + '<div class="col-3">' +  endValue + '</div>';
		html = html + '</div>';
		$('#'+id).html(html);
		/*Renderiza o ponteiro */
		var step1 = 400*percentValue/100;
		var step2 = 400 - step1;
		var potenciaId = id + "-potencia";
		var ctx = document.getElementById(potenciaId); 
		var data = {
			datasets: [{
				data: [step1, 2, step2],
				backgroundColor: ["rgba(0,0,0,0)", pointerColor, "rgba(0,0,0,0)"],
				borderColor: ["rgba(0,0,0,0)", "rgba(0,0,0,0)","rgba(0,0,0,0)"],
			}],
		};
		var options = {
			responsive: true,
			cutoutPercentage: 20,
			rotation: Math.PI,
			circumference: Math.PI,
			legend: {
				position: "bottom",
				fullWidth: true,
			},
			tooltips:{
				enabled: false,
			},

		}; 
		var myPointerChart = new Chart(ctx, {
    		type: 'doughnut',
    		data: data,
    		options: options
    	});
    	/* Cria o background do speedmeter */
    	var pbackgroundId = id + "-pbackground";
    	var steps = [backgroundSteps[0] , backgroundSteps[1]-backgroundSteps[0], backgroundSteps[2]-backgroundSteps[1], backgroundSteps[3]-backgroundSteps[2], backgroundSteps[4]-backgroundSteps[3] ]
    	var ctx = document.getElementById(pbackgroundId);
		var data = {
			datasets: [{
				data: steps,
				backgroundColor: backgroundColor,
				borderColor: backgroundColor,
			}],
		};
		var options = {
			responsive: true,
			cutoutPercentage: 60,
			rotation: Math.PI,
			circumference: Math.PI,
			legend: {
				position: "bottom",
				fullWidth: true,
			},
			animation: {
				duration: 0
			}

		}; 
		var myBackgroundChart = new Chart(ctx, {
    		type: 'doughnut',
    		data: data,
    		options: options
    	});
	}
}

function speedMeterChangeValue(id, percentValue, pointerColor="black"){

	var step1 = 400*percentValue/100;
	var step2 = 400 - step1;
	var potenciaId = id + "-potencia";
	var ctx = document.getElementById(potenciaId); 
	var data = {
		datasets: [{
			data: [step1, 2, step2],
			backgroundColor: ["rgba(0,0,0,0)", pointerColor, "rgba(0,0,0,0)"],
			borderColor: ["rgba(0,0,0,0)", "rgba(0,0,0,0)","rgba(0,0,0,0)"],
		}],
	};
	var options = {
		responsive: true,
		cutoutPercentage: 0,
		rotation: Math.PI,
		circumference: Math.PI,
		legend: {
			position: "bottom",
			fullWidth: true,
		},
		tooltips:{
			enabled: false,
		},

	}; 
	var myPointerChart = new Chart(ctx, {
    	type: 'doughnut',
    	data: data,
    	options: options
    });
}