import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterView from '@/components/RegisterView.vue'
import ProductView from "@/components/ProductView.vue";

const routes = [
    {
        path: '/',
        name: 'Login',
        component: LoginView
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView
    },
    {
        path: '/products',
        name: 'Products',
        component: ProductView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router