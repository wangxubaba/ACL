import Vue from 'vue'
import Router from 'vue-router'
import ConnectPage from "@/pages/ConnectPage";
import ExperimentPage from '@/pages/ExperimentPage'
import IntroducePage from '@/pages/IntroducePage'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/connect',
      name: 'ConnectPage',
      component: ConnectPage
    },
    {
      path:'/experiment',
      name:'experiment',
      component: ExperimentPage
    },{
      path:'/introduce',
      component: IntroducePage
    }

  ]
})
