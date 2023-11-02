import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  linkActiveClass: "active",
  scrollBehavior(to, from, savedPosition) {
  return { top: 0 }
  },
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
      path: '/login',
      name: 'login',
      component: () => import('../views/LogIn.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: ()=> import('../views/Register.vue')
    },
    {
      path: "/:pathMatch(.*)*",
      name: "NotFound",
      component: () => import("../views/NotFoundView.vue"),
  },

  ]
})

export default router
