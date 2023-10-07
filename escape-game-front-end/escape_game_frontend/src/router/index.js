import {createRouter, createWebHistory} from 'vue-router'
import SignUp from '../components/SignUp.vue'
import LogIn from '../components/LogIn.vue'
import GameList from '../components/GameList.vue'
import GameDetails from '../components/GameDetails.vue'
import UpdateAccount from '../components/UpdateAccount.vue'

const routes = [
    {
        path: "/",
        name: 'LogIn',
        component: LogIn
    },
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
        path: '/update-account',
        name: 'UpdateAccount',
        component: UpdateAccount
    },
    {
        path: '/games',
        name: 'GameList',
        component: GameList
    },
    { 
        path: '/game-details',
        name: 'GameDetails',
        component: GameDetails
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router