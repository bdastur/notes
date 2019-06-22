/*
 * In this recepie we declared our component just above the Vue instance that will
 * use it. The component is in the same scope as the Vue root instance.
 */
Vue.component('light-bulb', {
	template: `
	<div class="light-bulb">
	<p> Eureka!</p>
	</div>
	`
})

new Vue({
	el: "#app1"
})

/*
 * Registering the component locally.
 */
var lightBulb = {
	template: `
	 <div class="light-bulb">
	   <p> Eureka 2!</p>
	</div>
	`
}

new Vue({
	el: "#app2",
	    components: {
		"light-bulb": lightBulb
	}
})

 /*
  * Passing data to components.
  */
Vue.component("sound-icon", {
    template: `
        <span>{{soundEmojis[level]}}</span>
	`,
	props: {
		level: {
			required: true,
			default: 1,
			validator(value) {
				return value >= 0 && value <=3
			}
		}
	},
	data () {
		return {
			soundEmojis: ["0", "\>", ">", ">>"]
		}
	}
})

new Vue({
	el: "#app3",
	data:{
		soundLevel: 0
	}
})


/*
 * Making components talk to each other.
 */

var line = 0

Vue.component("blabber", {
	template: "<p>{{ dialogue[currentLine]}}</p>",
	data () {
		return {
			currentLine: 0,
			dialogue: [
				"hello",
				"how are you?",
				"fine thank-you."
			]

		}
	},
	mounted () {
		setInterval(() => {
			this.currentLine = line % this.dialogue.length
			line += 1
		}, 2000)

	}
})


new Vue({
	el: "#app4"
})




















