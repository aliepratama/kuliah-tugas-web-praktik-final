import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import BriefGenerator from '../views/BriefGenerator.vue'
import DesignRater from '../views/DesignRater.vue'
import Payment from '../views/Payment.vue'
import History from '../views/History.vue'

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home,
        },
        {
            path: '/login',
            component: Login,
        },
        {
            path: '/register',
            component: Register,
        },
        {
            path: '/brief',
            component: BriefGenerator,
        },
        {
            path: '/rater',
            component: DesignRater,
        },
        {
            path: '/payment',
            component: Payment,
        },
        {
            path: '/history',
            component: History,
        },
    ]
});