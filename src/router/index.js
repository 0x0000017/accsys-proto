//client/src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Home from '../components/Inventory.vue';
import Inventory from '../components/Inventory.vue';
 
Vue.use(Router);
 
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/inventory',
      name: 'Inventory',
      component: Inventory,

    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});