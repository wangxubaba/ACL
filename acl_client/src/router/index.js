import Vue from 'vue'
import Router from 'vue-router'
import ConnectPage from "@/pages/ConnectPage";
import ConfigurePage from "@/pages/ConfigurePage";
import TopologyPage from "@/pages/TopologyPage";
import ValidationPage from "@/pages/ValidationPage";
import HomePage from "@/pages/HomePage";

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
    },
    {
      path: '/topology',
      name: 'TopologyPage',
      component: TopologyPage
    },
    {
      path: '/validation',
      name: 'ValidationPage',
      component: ValidationPage
    },
    {
      path: '/home',
      name: 'home',
      component: HomePage
    
    }

  ]
})
