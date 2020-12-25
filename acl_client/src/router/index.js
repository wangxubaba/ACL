import Vue from 'vue'
import Router from 'vue-router'
import ConnectPage from "@/pages/ConnectPage";
import ConfigurePage from "@/pages/ConfigurePage";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/connect',
      name: 'ConnectPage',
      component: ConnectPage
    },
    {
      path: '/configure',
      name: 'ConfigurePage',
      component: ConfigurePage
    }
  ]
})
