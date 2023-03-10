import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from "@/views/MapView.vue";
import AnalyticsView from "@/views/AnalyticsView.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'map',
    component: MapView
  },
  {
    path: '/analytics',
    name: 'analytics',
    component: AnalyticsView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
