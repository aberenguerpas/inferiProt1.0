import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
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
        
  
    },
    {
      path: '/useCases',
      name: 'useCases',
      component: () => import('../views/UseCasesView.vue'),
    },
    {
      path: '/useCases/bonoconsumo',
      name: 'useCase-bonoconsumo',
      component: () => import('../views/UseCasesDetailView.vue'),
    },
    {
      path: '/providers',
      name: 'providers',
      component: () => import('../views/ProvidersView.vue'),
    },
    {
      path: '/providers/:name/',
      name: 'providersDetails',
      component: () => import('../views/ProvidersDetailView.vue'),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: () => import("../views/NotFoundView.vue"),
  },

  ]
})

export default router
