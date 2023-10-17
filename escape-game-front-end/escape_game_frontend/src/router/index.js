import {createRouter, createWebHistory} from 'vue-router'
import SignUp from '../components/SignUp.vue'
import LogIn from '../components/LogIn.vue'
import GameList from '../components/GameList.vue'
import GameDetails from '../components/GameDetails.vue'
import UpdateAccount from '../components/UpdateAccount.vue'
import store from '../store/index.js'
import StepDetails from '../components/StepDetails.vue'
import ScenarioDetails from '../components/ScenarioDetails.vue'
import UpdateNode from '../components/UpdateNode.vue'
import CreateNode from '../components/CreateNode.vue'

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
        path: '/update-account',
        name: 'UpdateAccount',
        component: UpdateAccount,
        meta: { requiresLogin: true }
    },
    {
        path: '/games',
        name: 'GameList',
        alias: ['/games', '/'],
        component: GameList,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:id',
        name: 'GameDetails',
        component: GameDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/step/:stepId',
        name: 'StepDetails',
        component: StepDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId',
        name: 'ScenarioDetails',
        component: ScenarioDetails,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId/node/:nodeId',
        name: 'UpdateNode',
        component: UpdateNode,
        meta: { requiresLogin: true }
    },
    { 
        path: '/games/:gameId/scenario/:scenarioId/node/new/:parentNodeId',
        name: 'CreateNode',
        component: CreateNode,
        meta: { requiresLogin: true }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

router.beforeEach((to, from, next) => {
    // ecrire une methode qui checke la validité du token à terme
    if (to.matched.some(record => record.meta.requiresLogin) && store.state.isAuthenticated === false) {
        store.commit("setGlobalError", "You need to log in before you can perform this action.")
        next("/login")
    } else {
        next()
    }
})