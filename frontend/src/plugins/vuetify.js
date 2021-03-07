import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify)



const vuetify = new Vuetify({
    theme: {
        themes: {
            light: {
                primary: colors.cyan.darken1,
                secondary: colors.lime,
                accent: colors.shades.black,
                error: colors.red.accent3,
                card1:colors.red,
                card2:colors.yellow,
                card3:colors.orange,
                card4:colors.green,
                card5:colors.pink,
                card6:colors.cyan,
                card7:colors.blue,
            },
            dark: {
                primary: colors.blue.lighten3,
            },
        },
    },
})
export default vuetify