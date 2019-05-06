import 'vuetify/dist/vuetify.min.css';
import pt from 'vuetify/lib/locale/pt';
import Vuetify from 'vuetify';
import Vue from 'vue';
import App from './App.vue';
import {
    router,
    store,
} from './config';

Vue.use(Vuetify, {
    theme: {
        primary: '#0A420E',
        secondary: '#00838F',
        accent: '#9c27b0',
        error: '#f44336',
        warning: '#ffeb3b',
        info: '#2196f3',
        success: '#4caf50',
    },
    lang: {
        locales: { pt },
        current: 'pt',
    },
});

Vue.config.productionTip = false;

const main = new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App),
}).$mount('#app');
