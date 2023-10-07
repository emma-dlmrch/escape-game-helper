import {createRouter, createWebHistory} from 'vue-router'
import SignUp from '../components/SignUp.vue'
import LogIn from '../components/LogIn.vue'
import GameList from '../components/GameList.vue'

const routes = [
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/login',
        name: 'LogIn',
        component: LogIn
    },
    {
        path: '/games',
        name: 'GameList',
        component: GameList
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router