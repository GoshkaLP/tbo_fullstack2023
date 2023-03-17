import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
import LMarkerCluster from 'vue2-leaflet-markercluster';
import 'leaflet.markercluster/dist/MarkerCluster.css';
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';
import 'leaflet.markercluster/dist/leaflet.markercluster';

import VueApexCharts from 'vue-apexcharts'


Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueApexCharts)

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-marker-cluster', LMarkerCluster);
Vue.component('apex-chart', VueApexCharts)

Vue.config.productionTip = false

document.addEventListener("gesturestart", function (e) {
  e.preventDefault();
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

