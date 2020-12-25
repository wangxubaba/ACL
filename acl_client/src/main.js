import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import iView from 'iview';
import router from './router'               
import 'iview/dist/styles/iview.css';       

Vue.prototype.$axios = axios;
Vue.config.productionTip = false
Vue.use(iView);

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
