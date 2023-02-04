import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active",
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/ResultsView.vue'),
      

    },
    {
        path: '/details/:id/',
        name: 'details',
        component: () => import('../views/DetailsView.vue'),
        
  
    }
  ]
})

export default router
