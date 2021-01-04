import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'                    

Vue.prototype.$axios = axios;
Vue.config.productionTip = false
Vue.use(ElementUI);

// new Vue({
//   render: h => h(App),
// }).$mount('#app')

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
