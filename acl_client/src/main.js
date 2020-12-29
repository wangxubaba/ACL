import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'                    
import hljs from 'highlight.js'
import 'highlight.js/styles/googlecode.css'
 //样式文件
Vue.directive('highlight',function (el) {
  let blocks = el.querySelectorAll('pre code');
  blocks.forEach((block)=>{
    hljs.highlightBlock(block)
  })
})
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
