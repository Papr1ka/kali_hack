import { createRouter, createWebHistory } from 'vue-router'
import EnterView from '../views/EnterView.vue'
import ProfileView from '../views/ProfileView.vue'
import VacanciesView from '../views/VacanciesView.vue'
import MyVacanciesView from '../views/MyVacanciesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: EnterView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/vacancies',
      name: 'vacancies',
      component: VacanciesView,
    },
    {
      path: '/my-vacancies',
      name: 'my-vacancies',
      component: MyVacanciesView,
    }
  ],
})

export default router
